"""Etiketli korpusta kural bazlı kesinlik/duyarlılık kapıları.

Kesinlik duyarlılıktan önce gelir: yanlış pozitif, doğru yazılmış bir insan
metnini bozmak demektir. Bu yüzden `error` seviyesindeki kuralların kesinlik
eşiği en yüksektir.
"""

import json
from pathlib import Path

import pytest

CORPUS = Path(__file__).parent / "fixtures" / "rules.jsonl"

# kural -> (asgari kesinlik, asgari duyarlılık)
ESIKLER = {
    "olarak-kalibi": (0.90, 0.80),
    "copula-chain": (0.80, 0.80),
    "spelling-error": (0.95, 0.90),
    "translationese": (0.85, 0.80),
    "baglac-virgul": (0.95, 0.90),
    "em-dash": (0.95, 0.90),
}


def _matchers(az):
    return {
        "olarak-kalibi": lambda s: bool(az.OLARAK_BIZ_RE.search(s) or az.OLARAK_ROL_RE.search(s)),
        "copula-chain": lambda s: bool(az.COPULA_END_RE.search(s)),
        "spelling-error": lambda s: any(p.search(s) for p, _ in az.SPELLING_RULES),
        "translationese": lambda s: any(p.search(s) for p in az.TRANSLATIONESE_PATTERNS.values()),
        "baglac-virgul": lambda s: bool(az.BAGLAC_VIRGUL_RE.search(s)),
        "em-dash": lambda s: bool(az.EM_DASH_RE.search(az.DIALOGUE_DASH_RE.sub("", s))),
    }


def _load(rule):
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            record = json.loads(line)
            if record["rule"] == rule:
                yield record


@pytest.mark.parametrize("rule", sorted(ESIKLER))
def test_kesinlik_duyarlilik(az, rule):
    predict = _matchers(az)[rule]
    tp = fp = fn = 0
    yanlis_pozitif, yanlis_negatif = [], []
    for record in _load(rule):
        hit = predict(record["text"])
        if hit and record["gold"]:
            tp += 1
        elif hit:
            fp += 1
            yanlis_pozitif.append(record["text"])
        elif record["gold"]:
            fn += 1
            yanlis_negatif.append(record["text"])

    assert tp + fn >= 3, f"{rule} için altın örnek sayısı yetersiz"
    kesinlik = tp / (tp + fp) if tp + fp else 1.0
    duyarlilik = tp / (tp + fn) if tp + fn else 1.0
    min_k, min_d = ESIKLER[rule]
    assert kesinlik >= min_k, f"{rule} kesinlik {kesinlik:.2f} < {min_k}\nyanlış pozitif: {yanlis_pozitif}"
    assert duyarlilik >= min_d, (
        f"{rule} duyarlılık {duyarlilik:.2f} < {min_d}\nyanlış negatif: {yanlis_negatif}"
    )


def test_muaf_olarak_ornekleri_yakalanmaz(az):
    """turkce-dilbilgisi.md § 1.1 son paragrafındaki muafiyetler betikte de geçerli olmalı."""
    for cumle in ("Müdür olarak atandı.", "Yedek olarak sakla.", "Örnek olarak şunu verelim."):
        assert not az.OLARAK_BIZ_RE.search(cumle), cumle
        assert not az.OLARAK_ROL_RE.search(cumle), cumle
