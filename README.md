<div align="center">

<h1>cache-freshness-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/cache-freshness-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/cache-freshness-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/cache-freshness-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/cache-freshness-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/cache-freshness-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/cache-freshness-governance-pack.svg"></a>
  <a href="https://pypi.org/project/cache-freshness-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/cache-freshness-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/cache-freshness-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/cache-freshness-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/cache-freshness-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/cache-freshness-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/cache-freshness-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fcache--freshness--governance--pack-181717?logo=github"></a>
</p>

</div>

`cache-freshness-governance-pack` is a small SSOT-compatible document pack for HTTP caching, freshness, validators, stale response controls, targeted cache policy, and CDN-facing cache governance.

It is designed to be published to PyPI and consumed by [`ssot-registry`](https://pypi.org/project/ssot-registry/) as an installable `extension-pack` document source. This repository does not perform downstream mutation itself. Its job is to ship immutable ADR and SPEC artifacts plus manifests that a downstream [`ssot-registry`](https://pypi.org/project/ssot-registry/) runtime can sync into the downstream `.ssot` registry.

The packaged distribution has one document artifact surface: `src/cache_freshness_governance_pack/templates/`. This repository does not package or maintain a parallel `.ssot/registry.json`.

## What is in scope

- upstream ADRs for cache/freshness governance decisions
- upstream SPECs for HTTP cache policy, validators, revalidation, and CDN-facing controls
- review inventories for RFC, IETF, and IANA cache/freshness targets
- packaged manifests for ADR and SPEC discovery
- a minimal Python loader module for runtime consumption

## What is intentionally out of scope

- downstream feature, claim, test, evidence, boundary, or release mutation
- CDN vendor-specific policy beyond standards-targeted governance rows
- runtime cache implementation, purge API implementation, or proxy deployment logic

## Canonical layout

- repo-local source ADRs: `.ssot/adr/`
- repo-local source SPECs: `.ssot/specs/`
- standards target inventory: `docs/standards/cache-freshness-rfc-ietf-targets.md`
- packaged ADR templates: `src/cache_freshness_governance_pack/templates/adr/`
- packaged SPEC templates: `src/cache_freshness_governance_pack/templates/specs/`

The repo-local `.ssot` documents are the authored source files in this repository. The packaged templates and manifests are the only shipped distribution artifact and are derived with:

```bash
python scripts/sync_packaged_docs.py
```

## Programmatic usage

```python
from cache_freshness_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-0900-cache-freshness-governance-target-review.yaml")
print(text[:120])
```

## Initial upstream documents

- `adr:0900` cache/freshness standards targets are reviewed before governance inclusion
- `spc:0900` cache/freshness governance target review

## Review target inventory

Start with [`docs/standards/cache-freshness-rfc-ietf-targets.md`](docs/standards/cache-freshness-rfc-ietf-targets.md). It separates core candidates, supporting candidates, historical/superseded context, and non-IETF watchlist items so ADR and SPEC inclusion can be decided deliberately.
