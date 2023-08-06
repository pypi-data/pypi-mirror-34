import json

from federation.hostmeta.parsers import (
    parse_nodeinfo_document, parse_nodeinfo2_document, parse_statisticsjson_document, parse_mastodon_document)
from federation.utils.network import fetch_document

HIGHEST_SUPPORTED_NODEINFO_VERSION = 2.0


def fetch_mastodon_document(host):
    doc, status_code, error = fetch_document(host=host, path='/api/v1/instance')
    if not doc:
        return
    try:
        doc = json.loads(doc)
    except json.JSONDecodeError:
        return
    return parse_mastodon_document(doc, host)


def fetch_nodeinfo_document(host):
    doc, status_code, error = fetch_document(host=host, path='/.well-known/nodeinfo')
    if not doc:
        return
    try:
        doc = json.loads(doc)
    except json.JSONDecodeError:
        return

    url, highest_version = '', 0.0

    if doc.get('0'):
        # Buggy NodeInfo from certain old Hubzilla versions
        url = doc.get('0', {}).get('href')
    elif isinstance(doc.get('links'), dict):
        # Another buggy NodeInfo from certain old Hubzilla versions
        url = doc.get('links').get('href')
    else:
        for link in doc.get('links'):
            version = float(link.get('rel').split('/')[-1])
            if version > highest_version and version <= HIGHEST_SUPPORTED_NODEINFO_VERSION:
                url, highest_version = link.get('href'), version

    if not url:
        return

    doc, status_code, error = fetch_document(url=url)
    if not doc:
        return
    doc = json.loads(doc)
    return parse_nodeinfo_document(doc, host)


def fetch_nodeinfo2_document(host):
    doc, status_code, error = fetch_document(host=host, path='/.well-known/x-nodeinfo2')
    if not doc:
        return
    try:
        doc = json.loads(doc)
    except json.JSONDecodeError:
        return
    return parse_nodeinfo2_document(doc, host)


def fetch_statisticsjson_document(host):
    doc, status_code, error = fetch_document(host=host, path='/statistics.json')
    if not doc:
        return
    try:
        doc = json.loads(doc)
    except json.JSONDecodeError:
        return
    return parse_statisticsjson_document(doc, host)
