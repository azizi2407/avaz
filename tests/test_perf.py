"""ReDoS regresyon kapısı.

OLARAK_BIZ_RE'yi patlamadan koruyan tek şey `[^.!?]{0,120}?` içindeki üst
sınırdır. Biri onu `*` veya `{0,}` yaparsa desen `(a+)+` sınıfına yaklaşır.
Bu testler o değişikliği yakalar.
"""

import time

import pytest


@pytest.mark.parametrize("kelime", [2000, 8000])
def test_redos_yok(az, kelime):
    kotu = "şirket olarak " + ("kelime " * kelime)
    basla = time.perf_counter()
    az.OLARAK_BIZ_RE.search(kotu)
    az.OLARAK_ROL_RE.search(kotu)
    assert time.perf_counter() - basla < 1.0, "sınırsız nicelik belirteci eklenmiş olabilir"


def test_lineer_olcekleme(az):
    birim = (
        "Bu bağlamda şirketimiz memnuniyeti sağlamaktadır. "
        "Firma olarak sunduğumuz çözümler raporda yer almaktadır.\n\n"
    )
    basla = time.perf_counter()
    az.analyze(birim * 200)
    kucuk = time.perf_counter() - basla

    basla = time.perf_counter()
    az.analyze(birim * 800)
    buyuk = time.perf_counter() - basla

    assert buyuk < max(kucuk, 0.01) * 12, f"süper-lineer büyüme: {kucuk:.3f}s -> {buyuk:.3f}s"
