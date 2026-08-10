"""CLI sözleşmesi: çıkış kodları, stdin, JSON şeması, kodlama."""

import json
import subprocess
import sys


def run(script_path, args, stdin=None):
    return subprocess.run(
        [sys.executable, str(script_path), *args],
        input=stdin,
        capture_output=True,
        text=True,
        timeout=60,
    )


def test_stdin(script_path):
    done = run(script_path, [], "Bu bağlamda bir deneme metni yazıldı.")
    assert done.returncode == 0
    assert "İstatistik" in done.stdout


def test_tire_stdin_demektir(script_path):
    assert run(script_path, ["-"], "Bu bağlamda deneme.").returncode == 0


def test_bos_girdi(script_path):
    done = run(script_path, ["-"], "   \n\n")
    assert done.returncode == 3
    assert done.stdout == ""


def test_eksik_dosya(script_path):
    assert run(script_path, ["yok-boyle-bir-dosya.txt"]).returncode == 3


def test_gecersiz_format_kullanim_hatasi(script_path):
    """Kullanım hatası (2) ile girdi hatası (3) ayrı olmalı."""
    assert run(script_path, ["-", "--format", "xml"], "x").returncode == 2


def test_ikili_dosya_reddedilir(script_path):
    assert run(script_path, ["-"], "abc\x00def").returncode == 3


def test_json_semasi(script_path):
    metin = "Herşey yolunda. Bir kaç kişi geldi."
    data = json.loads(run(script_path, ["-", "--format", "json"], metin).stdout)
    assert set(data) >= {"schema_version", "tool", "disclaimer", "summary", "statistics", "findings"}
    for item in data["findings"]:
        assert set(item) >= {"code", "level", "count", "message", "examples", "spans"}


def test_bom_stdin_ve_dosya_ayni(script_path, tmp_path):
    path = tmp_path / "bom.txt"
    path.write_bytes(b"\xef\xbb\xbf" + "Bu bağlamda herşey güzel.".encode())
    dosya = json.loads(run(script_path, [str(path), "--format", "json"]).stdout)
    boru = json.loads(run(script_path, ["-", "--format", "json"], path.read_bytes().decode()).stdout)
    assert dosya["statistics"] == boru["statistics"]


def test_crlf(script_path):
    done = run(script_path, ["-"], "Bir cümle.\r\n\r\nİkinci paragraf burada.\r\n")
    assert done.returncode == 0


def test_fail_on_error(script_path):
    assert run(script_path, ["-", "--fail-on", "error"], "Herşey yolunda.").returncode == 1
    assert run(script_path, ["-", "--fail-on", "error"], "Temiz bir cümle kuruldu.").returncode == 0


def test_max_examples(script_path):
    metin = "Herşey yolunda. Hiç bir sorun yok. Bir kaç kişi geldi. Herkez biliyor."
    data = json.loads(run(script_path, ["-", "--format", "json", "--max-examples", "1"], metin).stdout)
    for item in data["findings"]:
        assert len(item["examples"]) <= 1


def test_compact_json(script_path):
    out = run(script_path, ["-", "--format", "json", "--compact"], "Herşey yolunda.").stdout
    assert "\n" not in out.strip()
    json.loads(out)


def test_version(script_path):
    assert run(script_path, ["--version"]).returncode == 0
