# Instagram Rankings — Automated Content Pipeline

End-to-end automated workflow for turning ranking titles into published content on rank4ai.co.uk and Instagram, driven by APIs.

---

## The Automated Flow

```
TRIGGER (pick a title from master list)
    │
    ▼
STEP 1: Claude API generates ranking content + caption + DM copy
    │
    ▼
STEP 2: Canva API generates branded carousel/graphic from template
    │
    ▼
STEP 3: WordPress API publishes the ranking page to rank4ai.co.uk/rankings/[slug]
    │
    ▼
STEP 4: Instagram Graph API publishes the graphic + caption + tags + page URL
    │
    ▼
STEP 5: Instagram Graph API publishes to Stories with link sticker
    │
    ▼
STEP 6: LinkedIn API publishes repurposed text post
    │
    ▼
STEP 7: Notify — flag tagged people for DM follow-up
```

---

## APIs Involved

| Step | API | Purpose |
|---|---|---|
| Content generation | Claude API (Anthropic) | Write ranking article, caption, DM copy, hashtags |
| Graphic generation | Canva Connect API | Generate carousel/image from branded template |
| Site publishing | WordPress REST API | Create/update ranking page at rank4ai.co.uk |
| Instagram posting | Instagram Graph API (Meta) | Publish image/carousel, caption, user tags |
| Instagram Stories | Instagram Graph API (Meta) | Publish Story with link sticker |
| LinkedIn posting | LinkedIn Marketing API | Publish text post with link |
| Scheduling | Cron / queue (internal) | Trigger the pipeline on schedule (3x per week) |
| Tracking | Instagram Insights API + GA4 API | Pull reach, clicks, profile visits, page views |

---

## Step 1: Content Generation (Claude API)

**Input:** A ranking title from the master list (instagram_ranking_titles.md) + category metadata

**Claude API generates:**

1. **Ranking article** (for the site page)
   - Title
   - Intro paragraph (2–3 sentences)
   - Ranked list (10 entries, each with name, one-line reason, link)
   - Methodology note
   - CTA

2. **Instagram caption**
   - Hook line
   - Numbered list with @handles
   - Page URL: rank4ai.co.uk/rankings/[slug]
   - Engagement prompt ("Agree? Who's missing?")
   - Hashtag block

3. **DM copy**
   - Personalised warm message per tagged person
   - Includes post link + page URL

4. **LinkedIn post**
   - Reformatted version of the caption for LinkedIn tone

**API call pattern:**
```
POST https://api.anthropic.com/v1/messages
Model: claude-sonnet-4-20250514
System prompt: Rank4AI content voice, ranking format rules, tagging rules
User prompt: "Write a full ranking for: [title]. Category: [category]. Include site article, Instagram caption with @handles, DM template, LinkedIn post."
```

**Output:** JSON with all four content blocks, ready to feed into the next steps.

---

## Step 2: Graphic Generation (Canva Connect API)

**Input:** Ranking title + ranked list from Step 1

**What it does:**
- Fills a pre-built Canva template with:
  - Ranking title as headline
  - Numbered entries on each carousel slide
  - Rank4AI branding (logo, colours, fonts)
  - Page URL on the final slide
  - @handles overlaid on each entry slide

**Template types (pre-built in Canva):**
- Carousel template: cover slide → 10 entry slides → CTA slide
- Single image template: Top 5 all on one graphic
- Story template: vertical format with link placement

**API call pattern:**
```
POST https://api.canva.com/rest/v1/autofills
Template ID: [carousel_template_id]
Data: { title, entries[], url, handles[] }
→ Returns image URLs for each slide
```

**Output:** Image files (PNG/JPG) ready for Instagram upload.

---

## Step 3: Site Publishing (WordPress REST API)

**Input:** Ranking article from Step 1

**What it does:**
- Creates (or updates) a page at rank4ai.co.uk/rankings/[slug]
- Sets the SEO title, meta description, and schema markup
- Adds structured data (ItemList schema) for AI platform indexing

**API call pattern:**
```
POST https://rank4ai.co.uk/wp-json/wp/v2/posts
Headers: Authorization: Bearer [token]
Body: {
  title: "Top 10 Voices in AI Search UK to Follow in 2026",
  slug: "top-10-voices-ai-search-uk-2026",
  content: [rendered HTML from Claude output],
  status: "publish",
  categories: [rankings_category_id]
}
```

**Output:** Live URL → rank4ai.co.uk/rankings/[slug]

---

## Step 4: Instagram Posting (Instagram Graph API)

**Input:** Image files from Step 2 + caption from Step 1

**What it does:**
- Uploads carousel images to Meta's content publishing API
- Publishes the post with caption, hashtags, and user tags
- Tags featured people/brands in the image

**API call pattern (carousel):**
```
Step A — Upload each image as a container:
POST https://graph.facebook.com/v19.0/{ig-user-id}/media
Body: {
  image_url: [hosted image URL],
  is_carousel_item: true,
  user_tags: [{ username: "handle", x: 0.5, y: 0.5 }]
}
→ Returns creation_id per slide

Step B — Create the carousel container:
POST https://graph.facebook.com/v19.0/{ig-user-id}/media
Body: {
  media_type: "CAROUSEL",
  children: [creation_id_1, creation_id_2, ...],
  caption: [full caption with @handles, URL, hashtags]
}
→ Returns carousel_creation_id

Step C — Publish:
POST https://graph.facebook.com/v19.0/{ig-user-id}/media_publish
Body: { creation_id: carousel_creation_id }
→ Returns published post ID
```

**Output:** Live Instagram post ID + permalink.

---

## Step 5: Instagram Stories (Instagram Graph API)

**Input:** Story-format image from Step 2 + page URL

**API call pattern:**
```
POST https://graph.facebook.com/v19.0/{ig-user-id}/media
Body: {
  image_url: [story image URL],
  media_type: "STORIES"
}
→ Publish via /media_publish
```

**Note:** Link stickers are not yet supported via the API. Current workaround: include the URL as text on the Story image itself, and update the bio link to point to the latest ranking page via Linktree API or similar.

---

## Step 6: LinkedIn Posting (LinkedIn Marketing API)

**Input:** LinkedIn post text from Step 1 + page URL

**API call pattern:**
```
POST https://api.linkedin.com/v2/ugcPosts
Headers: Authorization: Bearer [token]
Body: {
  author: "urn:li:person:{adam-parker-id}",
  lifecycleState: "PUBLISHED",
  specificContent: {
    shareContent: {
      shareCommentary: { text: [LinkedIn post text] },
      shareMediaCategory: "ARTICLE",
      media: [{ originalUrl: "rank4ai.co.uk/rankings/[slug]" }]
    }
  },
  visibility: { memberNetworkVisibility: "PUBLIC" }
}
```

**Output:** Live LinkedIn post.

---

## Step 7: DM Follow-Up Notification

**Note:** Instagram DM API (via Messenger Platform) is limited to responding to users who message you first. Automated cold DMs are not supported by the API.

**Workaround — notification system:**
- After Step 4 publishes, the pipeline generates a DM task list:
  - Person name
  - @handle
  - Personalised DM copy (from Step 1)
  - Post permalink
  - Page URL
- This task list is pushed to a simple dashboard or Slack/email notification
- Adam (or team) sends the DMs manually within 24 hours using the pre-written copy

**DM copy template (generated by Claude API in Step 1):**
```
Hey [name]

We just featured you in our [ranking title] on Instagram — thought you'd want to see it!

[Instagram post link]

Full ranking and write-up here: rank4ai.co.uk/rankings/[slug]

Would love to know your thoughts. And if you're interested in AI search visibility, happy to chat.

Adam
Rank4AI
```

---

## Scheduling & Orchestration

**Frequency:** 3 rankings per week (Mon / Wed / Fri)

**Orchestration options:**
- Simple: Cron job triggering a Python/Node script that runs Steps 1–7 in sequence
- Medium: n8n or Make (Integromat) workflow connecting each API step visually
- Advanced: Custom FastAPI service with a queue (pick title → generate → publish → notify)

**Category rotation logic:**
- Don't repeat the same category twice in a row
- Alternate between people-based (tag-heavy) and topic-based (share-heavy) posts
- Weight "Instagram-First Discovery" and "Voices on Instagram" higher in the first month (outreach priority)

**Schedule example:**
```
Mon → People / Voices category (tag-heavy, outreach play)
Wed → Topic / Lifestyle category (share-heavy, reach play)
Fri → Spicy / Comparison category (engagement play)
```

---

## Approval Gate (Optional)

If you want a human review before publishing:

```
STEP 1 (Claude API) → generates content
    │
    ▼
REVIEW → content pushed to dashboard / Slack for Adam to approve or edit
    │
    ▼
APPROVE → triggers Steps 2–7 automatically
```

This keeps the creative control but still automates 90% of the work. The only manual touchpoint is a quick approve/edit before it goes live.

---

## What Gets Automated vs Manual

| Task | Automated | Manual |
|---|---|---|
| Write ranking content | Claude API | Review/approve |
| Generate graphic | Canva API | — |
| Publish to site | WordPress API | — |
| Post to Instagram | Instagram Graph API | — |
| Post to Stories | Instagram Graph API | — |
| Post to LinkedIn | LinkedIn API | — |
| Tag people in post | Instagram Graph API | — |
| Send DMs | — | Adam sends using pre-written copy |
| Update bio link | Linktree API | — |
| Track metrics | Insights API + GA4 | Weekly review |

---

## API Keys & Access Needed

| API | What to Set Up |
|---|---|
| Claude API (Anthropic) | API key from console.anthropic.com |
| Canva Connect API | App via canva.com/developers, connect to team account |
| WordPress REST API | Application password or JWT token for rank4ai.co.uk |
| Instagram Graph API | Meta Business account + Facebook App + Instagram Professional account, long-lived access token |
| LinkedIn Marketing API | LinkedIn Developer App with Marketing API Product approved |
| Linktree API | API key from Linktree (or equivalent bio link tool) |
| Google Analytics 4 API | Service account with GA4 property access |

---

## Quick Reference

| What | Where |
|---|---|
| Ranking master list | instagram_ranking_titles.md (this repo) |
| Full ranking article | rank4ai.co.uk/rankings/[slug] (via WordPress API) |
| Instagram post | @rank4ai feed (via Instagram Graph API) |
| Instagram Story | @rank4ai Stories (via Instagram Graph API) |
| LinkedIn post | Adam Parker profile (via LinkedIn API) |
| DM task list | Dashboard / Slack notification |
| Metrics | Instagram Insights API + GA4 API |
