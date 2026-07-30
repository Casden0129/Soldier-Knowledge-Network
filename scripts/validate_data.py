#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
RESOURCES=ROOT/'data'/'resources.json'
SITE=ROOT/'data'/'site.json'
UPDATES=ROOT/'data'/'updates.json'
REQUIRED={"id","name","fullName","category","description","tasks","audiences","sourceType","officialOwner","url","displayDomain","access","network","status","lastVerified","featured","keywords","legacyNames","automatedLinkCheck"}
AUDIENCES={"active-army","army-national-guard","army-reserve","army-civilian","contractor","family-member","retiree-veteran"}
SOURCE_TYPES={"official-army","official-dod","official-federal","army-affiliated-nonprofit","independent","commercial"}
STATUSES={"active","temporarily-unavailable","under-review","redirected","replaced","retired"}
DATE=re.compile(r"^\d{4}-\d{2}-\d{2}$")
errors=[]
def load(path):
    try:return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:errors.append(f"{path}: invalid JSON: {exc}");return []
resources=load(RESOURCES);site=load(SITE);updates=load(UPDATES)
if not isinstance(resources,list):errors.append('resources.json must contain a JSON array');resources=[]
ids=set();urls=set()
for i,r in enumerate(resources):
    label=f"resources[{i}]"
    missing=REQUIRED-set(r)
    if missing:errors.append(f"{label}: missing fields: {', '.join(sorted(missing))}")
    rid=r.get('id')
    if not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$",str(rid)):errors.append(f"{label}: invalid id {rid!r}")
    if rid in ids:errors.append(f"{label}: duplicate id {rid}")
    ids.add(rid)
    url=r.get('url','')
    parsed=urlparse(url)
    if parsed.scheme!='https' or not parsed.netloc:errors.append(f"{label}: URL must use HTTPS: {url}")
    if url in urls:errors.append(f"{label}: duplicate URL {url}")
    urls.add(url)
    if r.get('displayDomain')!=parsed.netloc:errors.append(f"{label}: displayDomain must equal {parsed.netloc}")
    if r.get('sourceType') not in SOURCE_TYPES:errors.append(f"{label}: invalid sourceType {r.get('sourceType')}")
    if r.get('status') not in STATUSES:errors.append(f"{label}: invalid status {r.get('status')}")
    bad=set(r.get('audiences',[]))-AUDIENCES
    if bad:errors.append(f"{label}: invalid audiences: {', '.join(sorted(bad))}")
    if not DATE.match(r.get('lastVerified','')):errors.append(f"{label}: lastVerified must be YYYY-MM-DD")
    for field in ('tasks','audiences','access','keywords','legacyNames'):
        if not isinstance(r.get(field),list):errors.append(f"{label}: {field} must be an array")
    if not isinstance(r.get('featured'),bool):errors.append(f"{label}: featured must be true or false")
    if not isinstance(r.get('automatedLinkCheck'),bool):errors.append(f"{label}: automatedLinkCheck must be true or false")
if not isinstance(site,dict) or not site.get('version'):errors.append('site.json must include version')
if not isinstance(updates,list):errors.append('updates.json must contain an array')
for i,u in enumerate(updates if isinstance(updates,list) else []):
    if not DATE.match(u.get('date','')):errors.append(f"updates[{i}]: date must be YYYY-MM-DD")
    missing={"id","title","summary","date","type","relatedResources"}-set(u)
    if missing:errors.append(f"updates[{i}]: missing {', '.join(sorted(missing))}")
    for rid in u.get('relatedResources',[]):
        if rid not in ids:errors.append(f"updates[{i}]: unknown related resource {rid}")
if errors:
    print('Validation failed:')
    for error in errors:print(f'- {error}')
    sys.exit(1)
print(f'Validation passed: {len(resources)} resources, {len(updates)} updates.')
