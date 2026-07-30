# Installing SKN v0.2.0 in GitHub

These instructions assume the public site is connected to the repository’s `main` branch through Cloudflare Pages.

## 1. Download and extract the package

Extract the ZIP on your computer. Open the extracted folder until you can directly see `index.html`, `styles.css`, `script.js`, `.github`, `data`, `docs`, `pages`, and `scripts`.

Do not upload the ZIP itself. GitHub needs the extracted files and folders.

## 2. Create a development branch

1. Open `Casden0129/Soldier-Knowledge-Network` on GitHub.
2. Select the branch button that currently says `main`.
3. Type `development`.
4. Select **Create branch: development from main**.
5. Confirm the branch selector now says `development`.

Cloudflare Pages should create a separate preview deployment for the branch without replacing the production site.

## 3. Upload the package contents

1. While viewing the `development` branch, select **Add file → Upload files**.
2. Drag all contents of the extracted folder into the upload area. GitHub accepts folders, so the nested structure should be preserved.
3. Confirm the upload includes the `.github`, `assets`, `data`, `docs`, `pages`, and `scripts` folders.
4. Confirm `index.html`, `styles.css`, and `script.js` appear at the repository root.
5. Enter this commit message:

   `release: prepare SKN v0.2.0 foundation and discovery update`

6. Commit directly to the `development` branch.

The package keeps the three original website files at the repository root, so they will be replaced rather than duplicated.

## 4. Confirm the validation workflow

1. Select the **Actions** tab.
2. Open **Validate SKN data**.
3. Confirm the push to `development` completed with a green check.
4. If it fails, open the failed step and copy the validation message before changing anything else.

The scheduled link checker and issue forms become fully active after their files are merged into the default `main` branch.

## 5. Preview through Cloudflare

1. Open Cloudflare → **Workers & Pages** → the SKN project.
2. Open **Deployments**.
3. Find the deployment for the `development` branch.
4. Open its preview URL.

Test the preview:

- Search `ALMS` and confirm **ATIS Learning** appears.
- Search `leave` and confirm **IPPS-A** ranks highly.
- Change the audience to **Army Civilian**.
- Add and remove a favorite.
- Open About, Privacy, Disclaimer, and Updates.
- Resize the browser or test on a phone.
- Confirm all cards show an owner, destination, access note, and verification date.

The **Report a Problem** issue form may not appear until the issue-template files are on the default branch.

## 6. Create the repository labels

Before running the automated link checker, create the labels referenced by the workflows and issue forms.

1. Open **Issues → Labels → New label**.
2. Create the labels listed in `.github/LABELS.md`:
   - `broken-link`
   - `resource-request`
   - `correction`
   - `needs-review`
   - `automated-link-check`
   - `content`
   - `accessibility`
   - `security`
   - `enhancement`

Label colors are your choice.

## 7. Merge into production

1. Select **Pull requests → New pull request**.
2. Set `base: main` and `compare: development`.
3. Use the title:

   `Release SKN v0.2.0 — Foundation and Discovery`

4. In the description, note that search, audience filters, favorites, pages, and mobile behavior were tested.
5. Create the pull request.
6. Review **Files changed** and confirm the validation check passes.
7. Select **Merge pull request → Confirm merge**.

Cloudflare will automatically deploy the merged `main` branch to the public site.

## 8. Test production features

After the production deployment finishes:

1. Open the public site in a private or incognito window.
2. Hard refresh with `Ctrl + F5` if the previous design is cached.
3. Test a **Report a Problem** link and confirm the GitHub issue form opens.
4. Open **Actions → Check public resource links → Run workflow → main → Run workflow**.
5. Download the generated link-check report from the workflow artifacts.
6. Manually review warnings from CAC, bot-protected, authentication-redirecting, VPN, or Army-network resources.

## 9. Keep the development branch

Keep `development` as the preview branch for future releases. Build each new improvement there or in a focused feature branch, preview it in Cloudflare, and merge it into `main` only after testing.

## Important safety boundary

Never upload credentials, CAC data, PII, CUI, medical records, orders, rosters, internal screenshots, or operational information to the repository or its public issues.
