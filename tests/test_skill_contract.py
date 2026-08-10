"""Skill paketinin kendi sözleşmesi: frontmatter, bağlantılar, betik yolları.

Bu dosyadaki ilk test, skill'i tümden yüklenemez hâle getiren sınıftan bir
hatayı yakalar: frontmatter'ın geçerli YAML olmaması.
"""

import re

import pytest

yaml = pytest.importorskip("yaml")

IZINLI_ALANLAR = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def frontmatter(repo):
    icerik = (repo / "SKILL.md").read_text(encoding="utf-8")
    eslesme = re.match(r"^---\n(.*?)\n---", icerik, re.DOTALL)
    assert eslesme, "SKILL.md YAML frontmatter ile başlamalı"
    return yaml.safe_load(eslesme.group(1))


def test_frontmatter_gecerli_yaml(repo):
    assert isinstance(frontmatter(repo), dict)


def test_frontmatter_alanlari(repo):
    veri = frontmatter(repo)
    fazla = set(veri) - IZINLI_ALANLAR
    assert not fazla, f"izinsiz anahtar: {fazla}"
    assert re.fullmatch(r"[a-z0-9-]{1,64}", veri["name"])
    assert 0 < len(veri["description"]) <= 1024
    assert "<" not in veri["description"], "description XML etiketi içeremez"


def test_kirik_referans_yok(repo):
    hedefler = [repo / "SKILL.md", *sorted((repo / "references").glob("*.md"))]
    for dosya in hedefler:
        icerik = dosya.read_text(encoding="utf-8")
        for yol in re.findall(r"\]\(([\w./-]+\.md)\)", icerik):
            assert (dosya.parent / yol).resolve().exists(), f"{dosya.name} -> {yol}"


def test_belgelenen_betikler_var(repo):
    for dosya in (repo / "SKILL.md", repo / "README.md"):
        icerik = dosya.read_text(encoding="utf-8")
        for yol in re.findall(r"(scripts/[\w./-]+\.py)", icerik):
            assert (repo / yol).exists(), f"{dosya.name} var olmayan betiği gösteriyor: {yol}"


def test_skill_md_makul_uzunlukta(repo):
    """Progressive disclosure: gövde 500 satırı aşmamalı."""
    assert len((repo / "SKILL.md").read_text(encoding="utf-8").splitlines()) < 500


def test_uzun_referanslarda_icindekiler(repo):
    for dosya in sorted((repo / "references").glob("*.md")):
        satirlar = dosya.read_text(encoding="utf-8").splitlines()
        if len(satirlar) > 100:
            assert any("İçindekiler" in s for s in satirlar[:20]), f"{dosya.name}: içindekiler yok"
