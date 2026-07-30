#!/usr/bin/env python3
import json, ssl, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
resources = json.loads((ROOT / 'data' / 'resources.json').read_text(encoding='utf-8'))
headers = {
    'User-Agent': 'SKN-Public-Link-Check/0.2 (+https://github.com/Casden0129/Soldier-Knowledge-Network)'
}
ctx = ssl.create_default_context()


def check(resource):
    if not resource.get('automatedLinkCheck', False):
        return resource['id'], 'SKIP', 'restricted or manual-only', False

    url = resource['url']
    req = urllib.request.Request(url, headers=headers, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=12, context=ctx) as response:
            code = response.getcode()
            return resource['id'], str(code), response.geturl(), code >= 400
    except urllib.error.HTTPError as exc:
        # Official sites often reject HEAD. Retry a small GET before confirming failure.
        try:
            retry = urllib.request.Request(url, headers={**headers, 'Range': 'bytes=0-1024'})
            with urllib.request.urlopen(retry, timeout=12, context=ctx) as response:
                return resource['id'], str(response.getcode()), response.geturl(), False
        except Exception as retry_error:
            confirmed = exc.code in (404, 410)
            return resource['id'], f'HTTP {exc.code}', str(retry_error), confirmed
    except Exception as exc:
        return resource['id'], 'WARN', str(exc), False


results = []
with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(check, resource) for resource in resources]
    for future in as_completed(futures):
        results.append(future.result())

results.sort(key=lambda item: item[0])
failed = [item for item in results if item[3]]
report = ROOT / 'link-check-report.md'
lines = [
    '# SKN public link check',
    '',
    'Automated results are indicators only. Authentication, bot protection, CAC, VPN, and Army-network restrictions require human review.',
    '',
    '| Resource | Result | Detail |',
    '|---|---:|---|',
]
for resource_id, result, detail, _ in results:
    safe_detail = str(detail).replace('|', '/')[:180]
    lines.append(f'| `{resource_id}` | {result} | {safe_detail} |')
report.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))

if failed:
    print(f'\nConfirmed {len(failed)} public 404/410 failures.', file=sys.stderr)
    sys.exit(1)
