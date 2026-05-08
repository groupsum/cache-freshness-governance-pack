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

`cache-freshness-governance-pack` is an SSOT Registry pack for HTTP caching, freshness, validators, cache directives, stale response behavior, targeted cache policy, and CDN-facing cache governance.

It gives product, platform, reliability, and edge-delivery teams a shared set of Architecture Decision Records (ADRs) and Specifications (SPECs) for cache behavior. Centralizing these requirements lets teams apply the same freshness and caching decisions across many services, APIs, sites, and CDNs while keeping local implementation work traceable to reviewed standards.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed ADRs and SPECs for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents. `ssot-registry` applies those documents to a project registry so teams can trace product requirements from decision, to specification, to implementation, to tests and release evidence.

This makes governance portable. A project can adopt the pack, synchronize the documents, list the active requirements, and connect local features or tests to the shared IDs.

## Why This Pack Exists

Caching looks simple until products need predictable freshness, validator behavior, stale response policy, CDN-specific directives, cache observability, and consistent release review. The same `Cache-Control` or `ETag` mistake can create stale pages, overloaded origins, broken rollback paths, misleading CDN behavior, and confusing customer experiences.

This pack helps teams:

- apply reviewed HTTP caching and freshness requirements across projects
- align origin, shared cache, browser, and CDN behavior around the same governed IDs
- turn RFC and IETF review into reusable ADRs and SPECs
- connect cache policy decisions to implementation, tests, and release evidence
- make edge-delivery reviews more consistent for APIs, web apps, static assets, and content platforms

## Domain Focus

The pack focuses on product and platform domains where cache behavior affects correctness, performance, reliability, and user trust:

- HTTP cache policy for sites, APIs, and service responses
- freshness calculation, max-age policy, and expiry behavior
- validators such as `ETag`, `Last-Modified`, and conditional requests
- `Cache-Control`, `Expires`, `Age`, and `Vary` governance
- stale response controls such as `stale-while-revalidate` and `stale-if-error`
- immutable/versioned asset response policy
- targeted cache control and `CDN-Cache-Control`
- cache diagnostics through `Cache-Status`
- cache grouping and invalidation requirements
- structured field syntax for cache extensions
- IETF, RFC, and IANA registry target review for cache/freshness surfaces

## Included ADRs

- `adr:0900` cache/freshness standards targets are reviewed before governance inclusion

## Included SPECs

- `spc:0900` cache/freshness governance target review

## Standards Review Targets

The first release includes a standards target inventory for cache/freshness review. It covers current core candidates, supporting candidates, historical/superseded context, and non-IETF watchlist items. Review the inventory on GitHub:

[Cache/Freshness RFC and IETF Target Inventory](https://github.com/groupsum/cache-freshness-governance-pack/blob/master/docs/standards/cache-freshness-rfc-ietf-targets.md)

The current review set includes RFC 9111, RFC 9110, RFC 5861, RFC 8246, RFC 9213, RFC 9211, RFC 9875, RFC 9651, and related IANA cache registries.

## Install With uv

Install the pack into a project environment:

```bash
uv add cache-freshness-governance-pack
```

Install it alongside the SSOT Registry CLI:

```bash
uv add ssot-registry cache-freshness-governance-pack
```

Run without adding dependencies to a project:

```bash
uvx --from ssot-registry --with cache-freshness-governance-pack ssot --help
```

## Install With The SSOT Registry Pack CLI

Pack-enabled SSOT Registry environments can install and synchronize packs through the pack command surface:

```bash
uvx --from ssot-registry ssot pack install cache-freshness-governance-pack
uvx --from ssot-registry ssot pack sync . cache-freshness-governance-pack
```

## Use With The SSOT Registry CLI

After the pack is installed in the same environment as `ssot-registry`, synchronize ADRs and SPECs into a target repository:

```bash
uv run ssot adr sync .
uv run ssot spec sync .
```

Review the synchronized governance surface:

```bash
uv run ssot adr list .
uv run ssot spec list .
uv run ssot spec get . --id spc:0900
```

Use the IDs from this pack when linking project features, tests, claims, and release evidence in your local `.ssot` registry.

## Programmatic Usage

```python
from cache_freshness_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-0900-cache-freshness-governance-target-review.yaml")
print(text[:120])
```

## Resources

- GitHub repository: [groupsum/cache-freshness-governance-pack](https://github.com/groupsum/cache-freshness-governance-pack)
- PyPI package: [cache-freshness-governance-pack](https://pypi.org/project/cache-freshness-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
