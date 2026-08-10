"""Altın çıktı testleri: kural değişikliklerinin etkisini görünür kılar.

Yeni bir kural eklendiğinde veya bir eşik değiştiğinde bu testler kırılır;
farkı gözle inceleyip kasıtlıysa `UPDATE_GOLDEN=1 pytest` ile yenile.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


def ozet(cikti: str) -> dict:
    data = json.loads(cikti)
    return {
        "statistics": data["statistics"],
        "summary": data["summary"],
        "findings": sorted([f["code"], f["count"]] for f in data["findings"]),
    }


@pytest.mark.parametrize("girdi", sorted(FIXTURES.glob("*.txt")), ids=lambda p: p.stem)
def test_altin_cikti(script_path, girdi):
    done = subprocess.run(
        [sys.executable, str(script_path), str(girdi), "--format", "json"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert done.returncode == 0, done.stderr
    gercek = ozet(done.stdout)

    beklenen_dosya = girdi.with_suffix(".expected.json")
    if os.environ.get("UPDATE_GOLDEN"):
        beklenen_dosya.write_text(
            json.dumps(gercek, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        pytest.skip("altın dosya yenilendi")

    assert beklenen_dosya.exists(), f"{beklenen_dosya.name} yok; UPDATE_GOLDEN=1 ile üret"
    assert gercek == json.loads(beklenen_dosya.read_text(encoding="utf-8"))


def test_temiz_metin_error_uretmez(script_path):
    """01: iyi yazılmış kurumsal metin hiçbir 'error' üretmemeli."""
    done = subprocess.run(
        [sys.executable, str(script_path), str(FIXTURES / "01_temiz_kurumsal.txt"), "--format", "json"],
        capture_output=True, text=True, timeout=60,
    )
    assert json.loads(done.stdout)["summary"]["error"] == 0


def test_diyalogda_konusma_cizgisi_bulgusu_yok(script_path):
    done = subprocess.run(
        [sys.executable, str(script_path), str(FIXTURES / "04_diyalog.txt"), "--format", "json"],
        capture_output=True, text=True, timeout=60,
    )
    kodlar = {f["code"] for f in json.loads(done.stdout)["findings"]}
    assert "em-dash" not in kodlar


def test_hukuki_metinde_tekrar_bulgu_uretmez(script_path):
    """03: terim tekrarı hukuki profilde zorunludur; 'error' çıkmamalı."""
    done = subprocess.run(
        [sys.executable, str(script_path), str(FIXTURES / "03_hukuki.txt"), "--format", "json"],
        capture_output=True, text=True, timeout=60,
    )
    assert json.loads(done.stdout)["summary"]["error"] == 0
