"""Inspect the installed pack identity."""

from cache_freshness_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:cache-freshness-governance"
print(metadata["origin"]["id"])
