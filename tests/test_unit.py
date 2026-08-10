"""Betiğin saf fonksiyonları ve tekil desenleri."""

import unicodedata

import pytest


@pytest.mark.parametrize(
    "raw,expected",
    [("İSTANBUL", "istanbul"), ("ILIK", "ılık"), ("IŞIK", "ışık"), ("TÜRKİYE", "türkiye")],
)
def test_tr_lower_nfc(az, raw, expected):
    assert az.tr_lower(raw) == expected


def test_tr_lower_nfd(az):
    """Ayrışık İ (I + U+0307) tabanı bozmamalı."""
    assert az.tr_lower(unicodedata.normalize("NFD", "İSTANBUL")) == "istanbul"


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Dr. Ahmet geldi. Sonra gitti.", 2),
        ("1. Madde geçerlidir. 2. Madde iptal.", 2),
        ("Yıl 2024. yılında bitti.", 1),
        ("Uzun bir cümle\nsatır sonuyla\nbölünmüş halde.", 1),
        ("Bir paragraf.\n\nİkinci paragraf.", 2),
        ("Fiyat 3,5 TL. Ucuz.", 2),
    ],
)
def test_split_sentences(az, text, expected):
    assert len(az.split_sentences(text)) == expected


def test_sentinel_cakismasi(az):
    """Görünür işaretçi girdiyi bozuyordu; artık NUL kullanılıyor."""
    assert az.split_sentences("x <DOT> y.") == ["x <DOT> y."]


@pytest.mark.parametrize("ch", ["—", "―", "–", "‒"])
def test_uzun_cizgi_varyantlari(az, ch):
    assert az.EM_DASH_RE.search(f"a {ch} b")


def test_kisa_cizgi_yasak_degil(az):
    assert not az.EM_DASH_RE.search("çok-yönlü bakış 2020-2024")


@pytest.mark.parametrize("line", ["— Kim o?", "  — Gel.", "> — Evet."])
def test_konusma_cizgisi_taninir(az, line):
    assert az.DIALOGUE_DASH_RE.search(line)


def test_arasoz_cizgisi_konusma_sayilmaz(az):
    assert not az.DIALOGUE_DASH_RE.search("Rapor — ki uzundu — teslim edildi.")


def test_sifir_sozcuk_bolme_hatasi_yok(az):
    assert az.analyze("12345 ...")["statistics"]["words"] == 0


def test_rapor_semasi(az):
    report = az.analyze("Herşey yolunda. Bir deneme cümlesi.")
    assert report["schema_version"] == az.SCHEMA_VERSION
    assert set(report["summary"]) == {"error", "review", "notice"}
    for item in report["findings"]:
        assert set(item) >= {"code", "level", "count", "message", "examples", "spans"}
        assert item["level"] in {"error", "review", "notice"}


def test_dusuk_agirlikli_belirti_tek_basina_raporlanmaz(az):
    """signals.md: cümle uzunluğu varyansı ve noktalı virgül tek başına kullanılmaz."""
    duz = " ".join(["Bu cümle tam olarak on iki sözcükten oluşan düzgün bir cümledir."] * 6)
    kodlar = {f["code"] for f in az.analyze(duz)["findings"]}
    assert "uniform-sentence-length" not in kodlar
