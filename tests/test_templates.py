from __future__ import annotations

import json
import unittest

from cache_freshness_governance_pack import (
    __pypi_package_name__,
    __ssot_package_name__,
    __version__,
    get_packaged_document_entry,
    list_packaged_document_ids,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class TemplateManifestTests(unittest.TestCase):

    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("cache-freshness-governance-pack", __ssot_package_name__)
        self.assertEqual("cache-freshness-governance-pack", __pypi_package_name__)
        self.assertEqual("0.1.2", __version__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("cache-freshness-governance-pack", metadata["ssot_package_name"])
        self.assertEqual("cache-freshness-governance-pack", metadata["pypi_package_name"])
        self.assertEqual("cache-freshness-governance-pack", metadata["origin"]["package_name"])
        self.assertEqual("cache_freshness_governance_pack", metadata["origin"]["import_name"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:cache-freshness-governance-pack", metadata["trust"]["reservation_owner"])
        self.assertEqual("1.0.0", load_pack_schema_version())
        self.assertEqual("0.1.2", metadata["version"])

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("cache-freshness-governance-pack", manifest["metadata"]["origin"]["package_name"])
        self.assertIn("adr", manifest["documents"])
        self.assertIn("spec", manifest["documents"])
        self.assertEqual("adr:0900", get_packaged_document_entry("adr:0900")["id"])
        self.assertEqual(2, len(list_packaged_document_ids()))
    def test_adr_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("adr")
        self.assertEqual(1, len(manifest))
        self.assertEqual(
            [
                "adr:0900",
            ],
            [row["id"] for row in manifest],
        )

    def test_spec_manifest_has_expected_rows(self) -> None:
        manifest = load_document_manifest("spec")
        self.assertEqual(1, len(manifest))
        self.assertEqual(
            [
                "spc:0900",
            ],
            [row["id"] for row in manifest],
        )

    def test_packaged_document_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0900-cache-freshness-governance-target-review.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0900", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])

    def test_packaged_adr_can_be_loaded(self) -> None:
        text = read_packaged_document_text("adr", "ADR-0900-cache-freshness-standards-targets-reviewed-before-inclusion.yaml")
        payload = json.loads(text)
        self.assertEqual("adr:0900", payload["id"])
        self.assertEqual(
            "Cache/freshness standards targets are reviewed before governance inclusion",
            payload["title"],
        )

    def test_packaged_spec_can_be_loaded(self) -> None:
        text = read_packaged_document_text("spec", "SPEC-0900-cache-freshness-governance-target-review.yaml")
        payload = json.loads(text)
        self.assertEqual("spc:0900", payload["id"])
        self.assertEqual("normative", payload["spec_kind"])


if __name__ == "__main__":
    unittest.main()

