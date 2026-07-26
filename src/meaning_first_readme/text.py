from __future__ import annotations

import hashlib
import math
import re
import unicodedata
from collections import Counter
from typing import Iterable

WORD_RE = re.compile(r"[A-Za-z0-9_./:-]+|[\u3040-\u30ff\u3400-\u9fff]+")
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")

STOP_TERMS = {
    "する", "した", "して", "いる", "ある", "なる", "でき", "れる", "られ",
    "こと", "もの", "ため", "から", "まで", "どう", "どの", "この", "その",
    "するか", "るか", "たい", "また", "よう", "なく", "ない", "として",
    "について", "を知", "知り", "知りた", "知りたい", "the", "a", "an", "of", "to",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return " ".join(text.split())


def terms(text: str) -> list[str]:
    """Extract English words and overlapping Japanese character bigrams.

    This intentionally avoids a heavyweight tokenizer so the runtime remains
    dependency-free.  Bigram features provide useful retrieval behavior for
    Japanese task prompts while preserving exact alphanumeric identifiers.
    """

    output: list[str] = []
    for chunk in WORD_RE.findall(normalize(text)):
        if any(CJK_RE.fullmatch(char) for char in chunk):
            chars = [char for char in chunk if CJK_RE.fullmatch(char)]
            if len(chars) == 1:
                output.append(chars[0])
            else:
                output.extend("".join(chars[index : index + 2]) for index in range(len(chars) - 1))
                if len(chars) >= 3:
                    output.extend("".join(chars[index : index + 3]) for index in range(len(chars) - 2))
                if len(chars) <= 10:
                    output.append("".join(chars))
        else:
            output.append(chunk)
    return [term for term in output if term not in STOP_TERMS]


def term_counts(text: str) -> Counter[str]:
    return Counter(terms(text))


def estimate_tokens(text: str) -> int:
    """Conservative local estimate for mixed Japanese and English text."""

    if not text:
        return 0
    cjk = len(CJK_RE.findall(text))
    ascii_words = len(re.findall(r"[A-Za-z0-9_]+", text))
    punctuation = len(re.findall(r"[^\w\s\u3040-\u30ff\u3400-\u9fff]", text))
    whitespace_chunks = len(re.findall(r"\s+", text))
    return max(1, math.ceil(cjk * 0.95 + ascii_words * 1.30 + punctuation * 0.35 + whitespace_chunks * 0.05))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def shingles(text: str, width: int = 5) -> set[str]:
    sequence = terms(text)
    if not sequence:
        return set()
    if len(sequence) < width:
        return {" ".join(sequence)}
    return {" ".join(sequence[index : index + width]) for index in range(len(sequence) - width + 1)}


def jaccard(left: Iterable[str], right: Iterable[str]) -> float:
    a = set(left)
    b = set(right)
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)



def simhash64(features: Iterable[str]) -> int:
    """Compute a deterministic 64-bit SimHash for approximate LSH bucketing."""

    vector = [0] * 64
    seen = list(features)
    if not seen:
        return 0
    for feature in seen:
        digest = hashlib.sha256(feature.encode("utf-8")).digest()
        value = int.from_bytes(digest[:8], "big")
        for bit in range(64):
            vector[bit] += 1 if value & (1 << bit) else -1
    result = 0
    for bit, weight in enumerate(vector):
        if weight >= 0:
            result |= 1 << bit
    return result


def simhash_bands(value: int, bands: int = 4) -> tuple[tuple[int, int], ...]:
    """Split a 64-bit SimHash into stable band keys for candidate generation."""

    if bands <= 0 or 64 % bands:
        raise ValueError("bands must be a positive divisor of 64")
    width = 64 // bands
    mask = (1 << width) - 1
    return tuple((index, (value >> (index * width)) & mask) for index in range(bands))

def canonical_claim(value: str) -> str:
    value = normalize(value)
    value = re.sub(r"[\s\-_:：。,.!?！？]+", "", value)
    return value
