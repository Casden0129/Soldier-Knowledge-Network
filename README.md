# Soldier Knowledge Network — Starter Site

A static prototype for an independent, unofficial Soldier resource directory.

## What is included

- Responsive homepage
- Search and category filtering
- Resource cards loaded from `data/resources.json`
- Access labels and last-verified dates
- Study Center placeholders
- Army/DoD non-endorsement disclaimer
- No login, database, analytics, cookies, or sensitive-data collection

## Recommended repository name

`soldier-knowledge-network`

## Upload to GitHub using the website

1. Create a new GitHub repository.
2. Name it `soldier-knowledge-network`.
3. Choose **Public** if you want transparent community contributions, or **Private** while developing.
4. Add a short description.
5. Do not initialize it with another README if you plan to upload every file in this package.
6. Open the repository and choose **Add file → Upload files**.
7. Upload the contents of this folder, including the `data` folder.
8. Commit the files to the `main` branch.

Important: upload the files themselves at the repository root. Do not upload the outer
`soldier-knowledge-network-starter` folder as an extra level.

## Connect the repository to Cloudflare Pages

1. Open Cloudflare.
2. Go to **Workers & Pages**.
3. Choose **Create application → Pages → Connect to Git**.
4. Authorize GitHub and grant access only to this repository.
5. Select `soldier-knowledge-network`.
6. Use these settings:

   - Production branch: `main`
   - Framework preset: `None`
   - Build command: leave blank, or use `exit 0`
   - Build output directory: `.`

7. Choose **Save and Deploy**.
8. Cloudflare will assign a URL similar to:
   `soldier-knowledge-network.pages.dev`

Every future commit to `main` will trigger a new deployment.

## Add or edit resources

Open `data/resources.json`. Each listing uses this format:

```json
{
  "name": "Resource name",
  "category": "Personnel",
  "description": "Plain-language purpose.",
  "url": "https://official-source.example/",
  "access": "CAC required",
  "lastVerified": "Month DD, YYYY",
  "keywords": ["search", "terms"]
}
```

Keep the JSON valid:
- Separate entries with commas.
- Use double quotation marks.
- Do not place a comma after the final entry.

## Before sharing Army-wide

- Do not use official Army logos, seals, rank insignia, unit crests, or other protected marks.
- Keep the independent/unofficial disclaimer visible.
- Link to official sources instead of copying controlled or frequently changing content.
- Do not collect CAC data, DoD IDs, personnel records, medical data, CUI, or operational information.
- Establish a documented verification and correction process.
- Complete a name/domain/trademark review before treating the working title as permanent.

## Suggested next files

- `CONTRIBUTING.md` — contributor and source-verification standards
- `SECURITY.md` — reporting security issues
- `PRIVACY.md` — plain-language privacy statement
- `404.html` — custom error page
- `.github/ISSUE_TEMPLATE/broken-link.yml` — structured broken-link reporting
- Automated weekly link checking through GitHub Actions
