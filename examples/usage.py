"""Resolve and read a packaged specification without synchronizing it."""

from cache_freshness_governance_pack import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:cache-freshness-governance-target-review")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
