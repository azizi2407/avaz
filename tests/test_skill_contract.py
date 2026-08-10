"""Skill ve plugin paketinin sözleşmesi: frontmatter, bağlantılar, manifestler.

Buradaki ilk test, skill'i tümden yüklenemez hâle getiren sınıftan bir hatayı
yakalar: frontmatter'ın geçerli YAML olmaması.
"""

import json
import re

import pytest

yaml = pytest.importorskip("yaml")

IZINLI_ALANLAR = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def frontmatter(skill_dir):
    icerik = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    eslesme = re.match(r"^---\n(.*?)\n---", icerik, re.DOTALL)
    assert eslesme, "SKILL.md YAML frontmatter ile başlamalı"
    return yaml.safe_load(eslesme.group(1))


def test_frontmatter_gecerli_yaml(skill_dir):
    assert isinstance(frontmatter(skill_dir), dict)


def test_frontmatter_alanlari(skill_dir):
    veri = frontmatter(skill_dir)
    fazla = set(veri) - IZINLI_ALANLAR
    assert not fazla, f"izinsiz anahtar: {fazla}"
    assert re.fullmatch(r"[a-z0-9-]{1,64}", veri["name"])
    assert 0 < len(veri["description"]) <= 1024
    assert "<" not in veri["description"], "description XML etiketi içeremez"


def test_skill_adi_dizin_adiyla_eslesir(skill_dir):
    assert frontmatter(skill_dir)["name"] == skill_dir.name


def test_kirik_referans_yok(skill_dir):
    hedefler = [skill_dir / "SKILL.md", *sorted((skill_dir / "references").glob("*.md"))]
    for dosya in hedefler:
        icerik = dosya.read_text(encoding="utf-8")
        for yol in re.findall(r"\]\(([\w./-]+\.md)\)", icerik):
            assert (dosya.parent / yol).resolve().exists(), f"{dosya.name} -> {yol}"


def test_tum_referanslar_skill_mdden_bagli(skill_dir):
    """Progressive disclosure: referanslar bir seviye derinlikte olmalı."""
    icerik = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    for dosya in sorted((skill_dir / "references").glob("*.md")):
        assert dosya.name in icerik, f"{dosya.name} SKILL.md'den bağlı değil"


def test_belgelenen_betikler_var(repo, skill_dir):
    """Belgelerde adı geçen her .py dosyası skill'in scripts/ dizininde olmalı."""
    for dosya in (skill_dir / "SKILL.md", repo / "README.md"):
        for ad in set(re.findall(r"([\w-]+\.py)", dosya.read_text(encoding="utf-8"))):
            assert (skill_dir / "scripts" / ad).exists(), f"{dosya.name} -> {ad}"


def test_skill_md_makul_uzunlukta(skill_dir):
    """Progressive disclosure: gövde 500 satırı aşmamalı."""
    assert len((skill_dir / "SKILL.md").read_text(encoding="utf-8").splitlines()) < 500


def test_uzun_referanslarda_icindekiler(skill_dir):
    for dosya in sorted((skill_dir / "references").glob("*.md")):
        satirlar = dosya.read_text(encoding="utf-8").splitlines()
        if len(satirlar) > 100:
            assert any("İçindekiler" in s for s in satirlar[:20]), f"{dosya.name}: içindekiler yok"


# --- Plugin ve marketplace manifestleri ---


def test_plugin_manifesti(plugin_dir):
    veri = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    assert veri["name"] == plugin_dir.name
    assert re.fullmatch(r"\d+\.\d+\.\d+", veri["version"])
    assert veri["description"]


def test_marketplace_manifesti(repo, plugin_dir):
    veri = json.loads((repo / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    assert veri["name"] and veri["owner"]["name"]
    kayitlar = veri["plugins"]
    assert kayitlar, "marketplace en az bir plugin listelemeli"
    for kayit in kayitlar:
        hedef = (repo / kayit["source"]).resolve()
        assert hedef.exists(), f"source yolu yok: {kayit['source']}"
        assert (hedef / ".claude-plugin" / "plugin.json").exists()


def test_surumler_senkron(repo, plugin_dir):
    """marketplace.json, plugin.json ve betik sürümü birbirini takip etmeli."""
    market = json.loads((repo / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugin = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    kayit = next(p for p in market["plugins"] if p["name"] == plugin["name"])
    assert kayit["version"] == plugin["version"]
    assert market["metadata"]["version"] == plugin["version"]


def test_gelistirme_dosyalari_plugin_disinda(plugin_dir):
    """tests/ ve evals/ kullanıcının bağlam dizinine inmemeli."""
    for istenmeyen in ("tests", "evals", "pyproject.toml", ".github"):
        assert not (plugin_dir / istenmeyen).exists(), f"plugin içinde olmamalı: {istenmeyen}"
