from __future__ import annotations

import unittest

from meaning_first_readme.text import canonical_claim, estimate_tokens, jaccard, normalize, shingles, simhash64, simhash_bands, terms


class TextTests(unittest.TestCase):
    def test_normalize_nfkc_and_case(self):
        self.assertEqual(normalize("ＡＢＣ  Test"), "abc test")

    def test_terms_keep_english_identifier(self):
        extracted = terms("README purpose.meaning")
        self.assertIn("readme", extracted)
        self.assertIn("purpose.meaning", extracted)

    def test_terms_make_japanese_bigrams(self):
        extracted = terms("意味達成")
        self.assertIn("意味", extracted)
        self.assertIn("味達", extracted)
        self.assertIn("意味達", extracted)

    def test_terms_remove_common_stopword(self):
        self.assertNotIn("する", terms("実行する"))

    def test_estimate_tokens_empty(self):
        self.assertEqual(estimate_tokens(""), 0)

    def test_estimate_tokens_mixed_text(self):
        self.assertGreater(estimate_tokens("日本語 and English 123."), 5)

    def test_shingles_and_jaccard_identical(self):
        data = shingles("one two three four five six")
        self.assertEqual(jaccard(data, data), 1.0)

    def test_jaccard_disjoint(self):
        self.assertEqual(jaccard({"a"}, {"b"}), 0.0)


    def test_simhash_is_deterministic(self):
        features = {"alpha", "beta", "gamma"}
        self.assertEqual(simhash64(features), simhash64(features))

    def test_simhash_bands_cover_64_bits(self):
        bands = simhash_bands((1 << 64) - 1, bands=8)
        self.assertEqual(len(bands), 8)
        self.assertTrue(all(value == 255 for _, value in bands))

    def test_canonical_claim_ignores_spacing_and_punctuation(self):
        self.assertEqual(canonical_claim("Length is not the goal."), canonical_claim("length-is-not-the-goal"))


if __name__ == "__main__":
    unittest.main()
