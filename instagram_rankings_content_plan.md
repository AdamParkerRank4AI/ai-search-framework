# Instagram Rankings — Automated Content Pipeline

---

## How It Works

Content is written by Claude Code and published to rank4ai.co.uk. The automation picks up from there.

```
CONTENT EXISTS ON SITE (rank4ai.co.uk/rankings/[slug])
    │
    ▼
STEP 1: Canva API generates branded carousel/graphic from the page content
    │
    ▼
STEP 2: Instagram Graph API publishes the graphic + caption + tags + page URL
    │
    ▼
STEP 3: Instagram Graph API publishes to Stories
    │
    ▼
STEP 4: LinkedIn API publishes repurposed text post
    │
    ▼
STEP 5: Notify — flag tagged people for DM follow-up
```

---

## What Already Happens (Claude Code)

- Claude Code writes the full ranking (article, ranked list, methodology, CTA)
- Claude Code writes the Instagram caption (hook, @handles, hashtags, page URL)
- Claude Code writes the DM copy for each tagged person
- Claude Code writes the LinkedIn post version
- All content goes live on rank4ai.co.uk/rankings/[slug]

**The site page is the source of truth. Everything downstream pulls from it.**

---

## APIs That Automate the Rest

| Step | API | What It Does |
|---|---|---|
| Graphic generation | Canva Connect API | Pulls content from site page, fills branded template |
| Instagram posting | Instagram Graph API (Meta) | Publishes carousel + caption + user tags |
| Instagram Stories | Instagram Graph API (Meta) | Publishes Story version |
| LinkedIn posting | LinkedIn Marketing API | Publishes text post with page link |
| Bio link update | Linktree API | Points bio link to latest ranking |
| Tracking | Instagram Insights API + GA4 API | Pulls reach, clicks, page views |

---

## Step 1: Graphic Generation (Canva Connect API)

Input: Ranking title + entries pulled from the live site page

What it does:
- Fills a pre-built Canva template with:
  - Ranking title as headline
  - Numbered entries on each carousel slide
  - Rank4AI branding (logo, colours, fonts)
  - Page URL on the final slide: rank4ai.co.uk/rankings/[slug]
  - @handles overlaid on each entry slide

API call:
```
POST https://api.canva.com/rest/v1/autofills
Template ID: [carousel_template_id]
Data: { title, entries[], url, handles[] }
→ Returns image URLs for each slide
```

Templates to pre-build in Canva:
- Carousel: cover slide → entry slides → CTA slide
- Single image: Top 5 all on one graphic
- Story: vertical format with URL text

---

## Step 2: Instagram Posting (Instagram Graph API)

Input: Images from Step 1 + caption (already written by Claude Code)

API calls (carousel):
```
Step A — Upload each slide:
POST https://graph.facebook.com/v19.0/{ig-user-id}/media
Body: {
  image_url: [hosted image URL],
  is_carousel_item: true,
  user_tags: [{ username: "handle", x: 0.5, y: 0.5 }]
}
→ Returns creation_id per slide

Step B — Create carousel:
POST https://graph.facebook.com/v19.0/{ig-user-id}/media
Body: {
  media_type: "CAROUSEL",
  children: [creation_id_1, creation_id_2, ...],
  caption: [caption from Claude Code output]
}
→ Returns carousel_creation_id

Step C — Publish:
POST https://graph.facebook.com/v19.0/{ig-user-id}/media_publish
Body: { creation_id: carousel_creation_id }
→ Returns published post ID + permalink
```

Caption (already written by Claude Code) includes:
- Hook line
- Numbered list with @handles
- Page URL: rank4ai.co.uk/rankings/[slug]
- Engagement prompt
- Hashtags

---

## Step 3: Instagram Stories (Instagram Graph API)

```
POST https://graph.facebook.com/v19.0/{ig-user-id}/media
Body: {
  image_url: [story image URL from Canva],
  media_type: "STORIES"
}
→ Publish via /media_publish
```

Note: Link stickers not supported via API yet. Workaround: URL baked into the Story image by Canva template + bio link updated via Linktree API.

---

## Step 4: LinkedIn Posting (LinkedIn Marketing API)

Input: LinkedIn post text (already written by Claude Code) + page URL

```
POST https://api.linkedin.com/v2/ugcPosts
Headers: Authorization: Bearer [token]
Body: {
  author: "urn:li:person:{adam-parker-id}",
  lifecycleState: "PUBLISHED",
  specificContent: {
    shareContent: {
      shareCommentary: { text: [LinkedIn text from Claude Code] },
      shareMediaCategory: "ARTICLE",
      media: [{ originalUrl: "rank4ai.co.uk/rankings/[slug]" }]
    }
  },
  visibility: { memberNetworkVisibility: "PUBLIC" }
}
```

---

## Step 5: DM Follow-Up

Instagram API does not allow cold outbound DMs.

What the automation does:
- Generates a DM task list after posting (person name, @handle, pre-written DM copy, post link, page URL)
- Pushes the task list to Slack or email
- Adam sends the DMs manually using the copy Claude Code already wrote

DM copy (already written by Claude Code):
```
Hey [name]

We just featured you in our [ranking title] on Instagram — thought you'd want to see it!

[Instagram post link]

Full ranking here: rank4ai.co.uk/rankings/[slug]

Would love to know your thoughts. Happy to chat about AI search visibility.

Adam
Rank4AI
```

---

## Scheduling

Frequency: 3 rankings per week (Mon / Wed / Fri)

```
Mon → People / Voices category (tag-heavy, outreach play)
Wed → Topic / Lifestyle category (share-heavy, reach play)
Fri → Spicy / Comparison category (engagement play)
```

Orchestration options:
- Simple: Cron job + Python/Node script
- Medium: n8n or Make (Integromat) workflow
- Advanced: Custom FastAPI service with a queue

---

## What's Automated vs Manual

| Task | Who |
|---|---|
| Write content | Claude Code (already done) |
| Publish to site | Claude Code (already done) |
| Generate graphic | Canva API (automated) |
| Post to Instagram | Instagram Graph API (automated) |
| Post to Stories | Instagram Graph API (automated) |
| Post to LinkedIn | LinkedIn API (automated) |
| Update bio link | Linktree API (automated) |
| Send DMs | Adam (manual, using pre-written copy) |
| Track metrics | Insights API + GA4 (automated) |

---

## API Keys & Access Needed

| API | What to Set Up |
|---|---|
| Canva Connect API | App via canva.com/developers, connect to team account |
| Instagram Graph API | Meta Business account + Facebook App + Instagram Professional account, long-lived access token |
| LinkedIn Marketing API | LinkedIn Developer App with Marketing API Product approved |
| Linktree API | API key from Linktree (or equivalent bio link tool) |
| Google Analytics 4 API | Service account with GA4 property access |

---

## Quick Reference

| What | Where |
|---|---|
| Content written | Claude Code |
| Ranking page | rank4ai.co.uk/rankings/[slug] |
| Instagram post | @rank4ai feed (via Instagram Graph API) |
| Instagram Story | @rank4ai Stories (via Instagram Graph API) |
| LinkedIn post | Adam Parker profile (via LinkedIn API) |
| DM task list | Slack / email notification |
| Ranking master list | instagram_ranking_titles.md (this repo) |
