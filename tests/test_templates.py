from __future__ import annotations

import json
import unittest

from cache_freshness_governance_pack import load_document_manifest, read_packaged_document_text


class TemplateManifestTests(unittest.TestCase):
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
