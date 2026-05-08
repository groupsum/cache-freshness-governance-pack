# Cache/Freshness RFC and IETF Target Inventory

This is the initial review list for the `cache-freshness-governance-pack`. It intentionally separates current core targets from supporting targets, historical context, and non-IETF watchlist surfaces. Final ADR and SPEC inclusion should be decided from this inventory.

## Core RFC Targets

| Target | Status | Why it matters | Initial disposition |
| --- | --- | --- | --- |
| [RFC 9111](https://www.rfc-editor.org/info/rfc9111) HTTP Caching | Internet Standard, IETF httpbis, STD 98 | Defines HTTP caches, cache behavior, freshness, validation, invalidation, `Cache-Control`, `Expires`, `Age`, `Vary`, and cache directive registries. | Include as core SPEC family. |
| [RFC 9110](https://www.rfc-editor.org/info/rfc9110) HTTP Semantics | Internet Standard, IETF httpbis, STD 97 | Defines shared HTTP semantics, validators, conditional request fields, `ETag`, `Last-Modified`, `Date`, `Vary`, selected representations, and status semantics used by caches. | Include as core semantics/validator SPEC family. |
| [RFC 5861](https://www.rfc-editor.org/info/rfc5861) HTTP Cache-Control Extensions for Stale Content | Informational, Independent stream | Defines `stale-while-revalidate` and `stale-if-error`, which are registered cache directives and central to freshness-availability policy. | Include, with status note that it is Informational but registry-backed and referenced by RFC 9111. |
| [RFC 8246](https://www.rfc-editor.org/info/rfc8246) HTTP Immutable Responses | Proposed Standard, IETF httpbis | Defines the `immutable` Cache-Control extension for fresh responses that should not be revalidated during their freshness lifetime. | Include as immutable/versioned-asset SPEC. |
| [RFC 9213](https://www.rfc-editor.org/info/rfc9213) Targeted HTTP Cache Control | Proposed Standard, IETF httpbis | Defines targeted cache-control fields and `CDN-Cache-Control` for CDN-specific cache policy. | Include as CDN/targeted-cache SPEC. |
| [RFC 9211](https://www.rfc-editor.org/info/rfc9211) Cache-Status Header | Proposed Standard, IETF httpbis | Defines `Cache-Status` for standardized cache diagnostics including hit, forward reason, TTL, collapsed forwarding, and detail. | Include as cache observability SPEC. |
| [RFC 9875](https://www.rfc-editor.org/info/rfc9875) HTTP Cache Groups | Proposed Standard, IETF httpbis | Defines response grouping for related stored responses and cache invalidation grouping. | Include as cache grouping/invalidation SPEC. |

## Supporting RFC Targets

| Target | Status | Why it matters | Initial disposition |
| --- | --- | --- | --- |
| [RFC 9651](https://www.rfc-editor.org/info/rfc9651) Structured Field Values for HTTP | Proposed Standard, IETF httpbis | Current Structured Fields specification; needed for parsing cache extensions such as `Cache-Status`, `CDN-Cache-Control`, and `Cache-Groups`. | Include as supporting parser/syntax dependency. |
| [RFC 8941](https://www.rfc-editor.org/info/rfc8941) Structured Field Values for HTTP | Obsoleted by RFC 9651 | Historical syntax reference used by older cache-extension documents. | Historical context only; cite RFC 9651 for new SPECs. |
| [RFC 9530](https://www.rfc-editor.org/info/rfc9530) Digest Fields | Proposed Standard, IETF httpbis | Defines `Content-Digest`, `Repr-Digest`, and related integrity request fields. It is not a freshness validator, but can support representation integrity governance adjacent to cache validation. | Supporting candidate; decide whether integrity belongs in this pack or a separate representation-integrity pack. |
| [RFC 8942](https://www.rfc-editor.org/info/rfc8942) HTTP Client Hints | Experimental, IETF httpbis | Client hints interact with cache key variation through `Vary` and response selection. | Supporting/watchlist; include only if cache-key variation policy is in scope. |
| [RFC 2295](https://www.rfc-editor.org/info/rfc2295) Transparent Content Negotiation in HTTP | Experimental | Defines variant selection mechanisms that historically intersect with caching and `Vary`. | Historical/watchlist. |
| [RFC 2296](https://www.rfc-editor.org/info/rfc2296) HTTP Remote Variant Selection Algorithm | Experimental | Companion to RFC 2295 for variant selection. | Historical/watchlist. |
| [RFC 3229](https://www.rfc-editor.org/info/rfc3229) Delta Encoding in HTTP | Proposed Standard | Defines delta encoding and validator-sensitive transfer behavior for cached representations. | Supporting/watchlist; include if delta or partial representation freshness is needed. |
| [RFC 8288](https://www.rfc-editor.org/info/rfc8288) Web Linking | Proposed Standard | Link relations can advertise alternates, preloads, and metadata that affect cache strategy indirectly. | Supporting/watchlist, not core cache governance. |

## IANA Registry Targets

| Registry | Why it matters | Initial disposition |
| --- | --- | --- |
| [HTTP Cache Directive Registry](https://www.iana.org/assignments/http-cache-directives) | Authoritative list of registered cache directives including `max-age`, `s-maxage`, `no-cache`, `no-store`, `immutable`, `stale-if-error`, and `stale-while-revalidate`. | Include as required registry target for directive completeness. |
| [HTTP Field Name Registry](https://www.iana.org/assignments/http-fields/) | Authoritative registration surface for cache/freshness fields such as `Cache-Control`, `CDN-Cache-Control`, `ETag`, `Expires`, `Age`, `Vary`, `Cache-Status`, and `Cache-Groups`. | Include as required registry target for field completeness. |
| [HTTP Cache-Status Registry](https://www.iana.org/assignments/http-cache-status) | Registry for `Cache-Status` parameters. | Include with cache observability SPEC. |

## Historical and Superseded Context

| Target | Current handling |
| --- | --- |
| RFC 7234 HTTP/1.1 Caching | Obsoleted by RFC 9111; use as historical comparison only. |
| RFC 7232 Conditional Requests | Obsoleted into RFC 9110; use RFC 9110 for new validator/conditional SPECs. |
| RFC 7231 HTTP/1.1 Semantics and Content | Obsoleted into RFC 9110; historical only. |
| RFC 2616 HTTP/1.1 | Obsoleted; historical only. |
| RFC 3230 Instance Digests in HTTP | Obsoleted by RFC 9530; historical only. |

## Non-IETF Watchlist

These are likely relevant to practical cache/freshness governance, but they should not be promoted into IETF/RFC SPECs without a later ADR that accepts non-IETF authority.

| Surface | Examples | Initial disposition |
| --- | --- | --- |
| CDN vendor purge APIs | Cloudflare purge, Fastly surrogate keys, Akamai invalidation APIs | Watchlist; vendor-specific, not core RFC surface. |
| Surrogate-Control and Surrogate-Key | Common CDN/proxy conventions | Watchlist; consider separate non-IETF SPEC if adopted. |
| Browser preload and service worker cache behavior | W3C/WHATWG surfaces | Watchlist; outside RFC/IETF scope unless this pack expands to browser runtime caching. |
| HTTP Archive / performance guidance | Operational freshness heuristics | Watchlist; advisory only. |

## Proposed ADR/SPEC Split After Review

- ADR: current RFC authority outranks historical HTTP/1.1 caching documents.
- ADR: cache policy surfaces split into origin/shared/CDN/browser targets.
- SPEC: HTTP caching model and freshness calculation.
- SPEC: validators and conditional request governance.
- SPEC: Cache-Control and Expires directive governance.
- SPEC: stale response controls.
- SPEC: immutable/versioned asset responses.
- SPEC: targeted cache control and CDN-Cache-Control.
- SPEC: cache diagnostics with Cache-Status.
- SPEC: cache groups and invalidation groups.
- SPEC: structured fields for cache extensions.
- SPEC: IANA cache directive and field registry coverage.
