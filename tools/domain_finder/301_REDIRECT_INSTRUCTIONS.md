Hi,

Need 301 permanent redirects set up on these domains. I think bigmouthmedia.co.uk and seocompare.co.uk might already be done, check those first before redoing them.

Leave lloydsfactoring.co.uk alone, no redirect on that one.

Redirect to SEO Compare site:

- seoagencyinuk.co.uk
- bigmouthmedia.co.uk (check first, may already be done)
- latitudedigital.co.uk
- seocompare.co.uk (check first, may already be done)

Redirect to Market Invoice site:

- alexlawriefactors.com
- workingcapitalpartners.co.uk
- hhcashflow.co.uk

How to set each one up:

1. Log into Cloudflare at cloudflare.com
2. Click "Add a site" in the top bar
3. Type in the domain name, for example alexlawriefactors.com
4. Select the Free plan and click Continue
5. Cloudflare will show you two nameservers, something like anna.ns.cloudflare.com and bob.ns.cloudflare.com. Copy both of them.
6. Open a new tab and log into GoDaddy
7. Go to My Products, find that same domain, click DNS
8. Scroll to Nameservers, click Change
9. Select Custom, delete the existing nameservers, paste in the two Cloudflare ones
10. Save and go back to Cloudflare
11. Wait for Cloudflare to confirm the domain is active. Usually takes 1 to 4 hours. Cloudflare will send an email when it is ready.
12. Once active, go to that domain in Cloudflare and click DNS on the left menu
13. Click Add Record
14. Set Type to A, Name to @, Content to 192.0.2.1, make sure the orange cloud icon is ON (it says Proxied), click Save
15. Click Add Record again
16. Set Type to CNAME, Name to www, Content to the domain itself (for example alexlawriefactors.com), make sure the orange cloud is ON, click Save
17. Now click Rules on the left menu
18. Click Redirect Rules
19. Click Create Rule
20. Give it a name like "301 redirect to Market Invoice" or "301 redirect to SEO Compare" depending on which site this domain points to
21. Under "When incoming requests match" select All incoming requests
22. Under "Then" select URL redirect
23. Set Type to Static
24. Set URL to the full destination site URL (the SEO Compare site or Market Invoice site, whichever this domain is assigned to from the lists above)
25. Set Status code to 301
26. Turn on Preserve query string
27. Click Deploy

Do this for all 7 domains listed above, skipping any that are already set up and working.

How to check it is working:

Open Terminal and run this for each domain:

curl -I http://alexlawriefactors.com
curl -I http://www.alexlawriefactors.com
curl -I http://workingcapitalpartners.co.uk
curl -I http://www.workingcapitalpartners.co.uk
curl -I http://hhcashflow.co.uk
curl -I http://seoagencyinuk.co.uk
curl -I http://bigmouthmedia.co.uk
curl -I http://latitudedigital.co.uk
curl -I http://seocompare.co.uk

Every single one should come back with:

HTTP/1.1 301 Moved Permanently
Location: (the correct destination site URL)

If any come back as 302 instead of 301, or show a timeout or error, flag it.

Also open each domain in an incognito browser window and make sure it lands on the correct site.

After setup, keep checking:

Once a week for the first month, then once a month after that, run those curl commands again to make sure they are all still returning 301. If GoDaddy auto-renew fails on any domain the redirect will stop working, so make sure auto-renew is turned on for all of them in GoDaddy.

Let me know once they are all live.

Thanks