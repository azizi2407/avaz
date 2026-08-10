#!/usr/bin/env python3
"""Türkçe metindeki açıklanabilir editoryal belirtileri raporla.

Bu araç AI yazarlığı tahmin etmez ve kalite puanı üretmez. Bulgular,
profil ve bağlamla birlikte insan tarafından değerlendirilmelidir.

Seviyeler:
  error  — TDK yazımına göre kesin hata; doğrudan düzeltilir.
  review — okuma etkisi olası; paragrafı elle incele.
  notice — yalnızca başka belirtilerle birlikte anlamlı.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

TURKISH = "A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû"
WORD_RE = re.compile(rf"[{TURKISH}]+(?:['’][{TURKISH}]+)?")
ABBREVIATIONS = ("Dr.", "Prof.", "Doç.", "Yrd.", "Sn.", "vb.", "vs.", "No.", "T.C.", "Av.", "Bkz.", "Md.")

# --- Eşikler: kümelenme sayıları deneysel, hüküm değil uyarı üretir. ---
T_TRANSITION = 3          # bürokratik geçiş kalıbı sayısı
T_EVALUATION = 2          # kanıtsız değerlendirme sıfatı
T_FRAMING = 2             # içeriksiz üst çerçeve
T_MAKTADIR = (3, 1.5)     # (adet, yüzde yoğunluk)
T_PASSIVE = (4, 2.0)
T_TRANSLATIONESE = 4      # çeviri kokusu kalıplarının toplamı
T_COPULA = (4, 1.5)       # cümle sonu -dır/-dir
T_STARTERS = 3            # hazır ifadeyle başlayan paragraf
T_CV = 0.25               # cümle uzunluğu değişim katsayısı

PHRASE_GROUPS = {
    "bureaucratic_transitions": (
        "bu bağlamda", "bu doğrultuda", "bu çerçevede", "bunun yanı sıra",
        "bununla birlikte", "öte yandan", "söz konusu", "bu kapsamda",
    ),
    "empty_evaluations": (
        "benzersiz", "eşsiz", "paha biçilmez", "devrim niteliğinde",
        "hayati önem", "kritik bir rol", "vazgeçilmez", "zengin bir mozaik",
        "çok boyutlu", "kusursuz", "son derece", "büyük bir titizlikle",
    ),
    "meta_framing": (
        "günümüzün hızla değişen", "günümüz dünyasında", "her geçen gün",
        "önem kazanmaktadır", "bu noktada belirtmek gerekir",
        "altını çizmek gerekir", "göz ardı edilmemelidir", "dikkat çekmektedir",
    ),
}

PARAGRAPH_STARTERS = (
    "ayrıca", "bununla birlikte", "öte yandan", "bu bağlamda", "bu doğrultuda",
    "bu çerçevede", "sonuç olarak", "dolayısıyla", "bu kapsamda",
)

# --- Çeviri kokusu: İngilizce sözdiziminin Türkçe sözcüklerle kurulması. ---
TRANSLATIONESE_PATTERNS = {
    # "sahip ol-" kadar "-e sahip" sıfat öbeği de aranır: SKILL.md'nin amiral
    # örneği ("yüksek performansa sahip motor") yardımcı fiil içermez.
    "sahip-olmak": re.compile(
        r"\b[a-zçğıöşüâîû]+[ae]\s+sahip\b|\bsahip\s+ol[a-zçğıöşüâîû]*",
        re.IGNORECASE,
    ),
    "gerçekleştirmek": re.compile(r"\bgerçekleştir[a-zçğıöşüâîû]*", re.IGNORECASE),
    "sağlamak": re.compile(
        r"\bsağla(?:mak|mayı|maya|maktadır|makta|nmak|nması|nmasına|nmakta|nmaktadır"
        r"|yan|yarak|nan|r|nır|dı|ndı|mıştır|nmıştır)\b",
        re.IGNORECASE,
    ),
    # (?!t) "yer altı / yer altında" adını dışarıda bırakır; fiil çekimlerinin
    # hiçbiri "al"dan sonra t ile devam etmez.
    "yer-almak": re.compile(r"\byer\s+al(?!t)[a-zçğıöşüâîû]*", re.IGNORECASE),
    "olan-fazlalığı": re.compile(
        r"\b(?:olmuş\s+olan|olmakta\s+olan|bulunmakta\s+olan|[a-zçğıöşüâîû]+m[ıiuü]ş\s+olan)\b",
        re.IGNORECASE,
    ),
    "ilgec-yigini": re.compile(r"\b(?:ile\s+ilgili\s+olarak|açısından|konusunda|bazında|nezdinde)\b", re.IGNORECASE),
}

PASSIVE_STEMS_RE = re.compile(
    r"\b(?:yapıl|edil|gerçekleştiril|sağlan|sunul|kullanıl|belirlen|değerlendiril|oluşturul|yürütül)"
    r"[a-zçğıöşüâîû]*\b",
    re.IGNORECASE,
)
MAKTADIR_RE = re.compile(r"\b[a-zçğıöşüâîû]+m[ae]kt[ae]d[ıiuü]r(?:lar|ler)?\b", re.IGNORECASE)

# -DIr yalnızca kopula değildir: ettirgen/emir eki ("indir", "getir") ve t/d ile
# biten gövdelerin geniş zamanı ("unutur", "öğretir") aynı sesle biter. Bunlar
# elenmezse emir kipiyle yazılmış her kurulum talimatı kopula zinciri sanılır.
NON_COPULA_WORDS = (
    # ettirgen / emir
    "artır", "bildir", "bitir", "buldur", "coştur", "değiştir", "doldur", "dondur",
    "geçir", "getir", "giydir", "götür", "indir", "kaldır", "karıştır", "oluştur",
    "otur", "öldür", "sıkıştır", "ulaştır", "uyandır", "yaptır", "yatır", "yetiştir",
    # t/d ile biten gövdelerin geniş zamanı
    "unutur", "artırır", "azaltır", "bitirir", "getirir", "öğretir", "yatırır",
    # ad
    "satır", "çadır", "hatır", "katır", "kadir",
)
# -maktadır ayrı bir bulgu olduğu için kopula zincirinden çıkarılır.
COPULA_END_RE = re.compile(
    r"\b(?!(?:" + "|".join(NON_COPULA_WORDS) + r")(?:lar|ler)?\s*[.!?])"
    r"[a-zçğıöşüâîû]{2,}(?:(?<!m[ae]kt[ae])d|t)[ıiuü]r(?:lar|ler)?\s*[.!?]",
    re.IGNORECASE,
)
CONTRAST_RE = re.compile(r"\b(?:sadece|yalnızca)\b[^.!?]{0,80}\bdeğil\b", re.IGNORECASE)

# --- Yasak kalıplar (demir kural 4 ve 5). ---
# Yasak, boşluklu ara söz çizgisidir; varyantları da kapsar çünkü en dash (–)
# LLM metinlerinde em dash kadar sık geçer ve aynı işlevi üstlenir.
EM_DASH_RE = re.compile(r"[‒–—―]")
# Satır başındaki çizgi TDK'de konuşma çizgisidir ve korunur (bkz. demir kural 4
# istisnası); sayımdan düşülür.
DIALOGUE_DASH_RE = re.compile(r"(?m)^[ \t>]*[‒–—―][ \t]")

# Yalnızca yüksek özgüllüklü birinci şahıs ekleri; "artık", "balık" gibi
# sözcüklere takılmamak için genel -dık/-dik dışarıda bırakıldı.
FIRST_PERSON = (
    r"(?:[ıiuü]yoruz|[ıiuü]yorum|[ae]cağız|[ae]ceğiz|[ae]cağım|[ae]ceğim"
    r"|[dt][ıiuü]ğ[ıiuü]m[ıiuü]z|[dt][ıiuü]ğ[ıiuü]m|[ae]r[ıi]z|m[ıiuü]ş[ıiuü]z)"
)
# Birinci çoğul iyelik ("sorumluluğumuz"), biz-anlatımının çekimsiz biçimidir.
FIRST_PERSON_POSSESSIVE = r"[ıiuü]m[ıiuü]z"

# Yasak, özneyi gizleyen kalıptır. "olarak" belirteç kurduğunda ya da nesneye
# sıfat verdiğinde özne yerinde durur; bu kullanımlar turkce-dilbilgisi.md § 1.1
# son paragrafında açıkça serbest bırakılmıştır.
OLARAK_BELIRTEC = (
    "sonuç", "örnek", "misal", "genel", "ek", "özet", "kısa", "uzun", "ayrıntılı",
    "detaylı", "tam", "doğrudan", "dolaylı", "yedek", "alternatif", "geçici",
    "kalıcı", "öncelikli", "ilk", "son", "karşılık", "temel", "açık", "net",
    "aynı", "farklı", "ayrı", "toplu", "bireysel", "hediye", "ödül", "cevap",
    "yanıt", "tepki", "başlangıç", "varsayılan", "standart", "gönüllü", "zorunlu",
)
_OLARAK_MUAF = r"(?!(?:" + "|".join(OLARAK_BELIRTEC) + r")\s+olarak\b)"

OLARAK_BIZ_RE = re.compile(
    rf"\b{_OLARAK_MUAF}[\wçğıöşüâîû'’]+\s+olarak\b"
    rf"[^.!?]{{0,120}}?[a-zçğıöşüâîû]+{FIRST_PERSON}\b",
    re.IGNORECASE,
)
# Rol adı tek başına yeterli değildir: kural "rol adı + olarak + biz-anlatımı"
# der. Koşulsuz desen "Şirket olarak tescil edildi" gibi üçüncü şahıs
# sınıflandırma cümlelerini de yakalıyordu.
OLARAK_ROL_RE = re.compile(
    r"\b(?:firma|marka|şirket|ekip|kurum|kuruluş|aile|takım|yönetim|holding"
    r"|grup|banka|ajans|kadro|çalışanlar|hepimiz)\s+olarak\b"
    rf"[^.!?]{{0,120}}?(?:\bbiz\b|[a-zçğıöşüâîû]+(?:{FIRST_PERSON}\b|{FIRST_PERSON_POSSESSIVE}))",
    re.IGNORECASE,
)

# --- Kesin yazım hataları (TDK). ---
# "bir çok/kaç" ancak arkasından bileşik sıfat gelmiyorsa birleşik yazılır.
_BILESIK_SIFAT = (
    r"(?!\s+(?:yönlü|boyutlu|taraflı|anlamlı|amaçlı|katmanlı|aşamalı|basamaklı"
    r"|yıllık|aylık|haftalık|günlük|kişilik|parçalı)\b)"
)

SPELLING_RULES = (
    (re.compile(r"\bherşey[a-zçğıöşü]*\b", re.IGNORECASE), "her şey"),
    (re.compile(r"\bbirşey[a-zçğıöşü]*\b", re.IGNORECASE), "bir şey"),
    (re.compile(r"\bhiçbirşey[a-zçğıöşü]*\b", re.IGNORECASE), "hiçbir şey"),
    (re.compile(r"\bhiç\s+bir\b", re.IGNORECASE), "hiçbir"),
    # "bir çok yönlü sorun" = sayı sıfatı + bileşik sıfat; birleşik yazım hatası değil.
    (re.compile(rf"\bbir\s+kaç\b{_BILESIK_SIFAT}", re.IGNORECASE), "birkaç"),
    (re.compile(rf"\bbir\s+çok\b{_BILESIK_SIFAT}", re.IGNORECASE), "birçok"),
    # Büyük harfli "Yada" bir özel addır (Yada dağı); IGNORECASE bilerek yok.
    (re.compile(r"\byada\b"), "ya da"),
    (re.compile(r"\bherkez\b", re.IGNORECASE), "herkes"),
    (re.compile(r"\byalnış[a-zçğıöşü]*\b", re.IGNORECASE), "yanlış"),
    (re.compile(r"\byanlız[a-zçğıöşü]*\b", re.IGNORECASE), "yalnız"),
    (re.compile(r"\bsüpriz[a-zçğıöşü]*\b", re.IGNORECASE), "sürpriz"),
    (re.compile(r"\borjinal[a-zçğıöşü]*\b", re.IGNORECASE), "orijinal"),
    (re.compile(r"\bfarket[a-zçğıöşü]*\b", re.IGNORECASE), "fark et-"),
    (re.compile(r"\bheryer[a-zçğıöşü]*\b", re.IGNORECASE), "her yer"),
    (re.compile(r"\bhiçkimse\b", re.IGNORECASE), "hiç kimse"),
    (re.compile(r"\b(?:gel|yap|al|ol|bil|gör|ver)[iı]c[ae]k\b", re.IGNORECASE), "-acak/-ecek (daralma yazılmaz)"),
)


def tr_lower(text: str) -> str:
    """Türkçe kurallarına göre küçült: İ→i, I→ı."""
    return text.replace("İ", "i").replace("I", "ı").lower()


def split_sentences(text: str) -> list[str]:
    masked = text
    marker = "<DOT>"
    for abbreviation in ABBREVIATIONS:
        masked = masked.replace(abbreviation, abbreviation.replace(".", marker))
    pieces = re.split(r"(?<=[.!?…])(?:[\"”’')\]]*)\s+|\n+", masked)
    return [piece.replace(marker, ".").strip() for piece in pieces if piece.strip()]


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def population_std(values: list[int]) -> float:
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((value - mean) ** 2 for value in values) / len(values))


def sentence_examples(sentences: list[str], needles: tuple[str, ...], limit: int = 3) -> list[str]:
    output: list[str] = []
    for sentence in sentences:
        lowered = tr_lower(sentence)
        if any(needle in lowered for needle in needles):
            output.append(sentence[:220])
            if len(output) == limit:
                break
    return output


def regex_examples(sentences: list[str], patterns: list[re.Pattern[str]], limit: int = 3) -> list[str]:
    output: list[str] = []
    for sentence in sentences:
        if any(pattern.search(sentence) for pattern in patterns):
            output.append(sentence[:220])
            if len(output) == limit:
                break
    return output


def finding(code: str, level: str, count: int, message: str, examples: list[str]) -> dict[str, object]:
    return {"code": code, "level": level, "count": count, "message": message, "examples": examples}


def analyze(text: str) -> dict[str, object]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    sentences = split_sentences(text)
    token_list = words(text)
    token_count = len(token_list)
    lengths = [len(words(sentence)) for sentence in sentences]
    mean_length = (sum(lengths) / len(lengths)) if lengths else 0.0
    std_length = population_std(lengths)
    cv = (std_length / mean_length) if mean_length else 0.0
    lowered = tr_lower(text)
    findings: list[dict[str, object]] = []

    group_counts: dict[str, dict[str, int]] = {}
    for group, phrases in PHRASE_GROUPS.items():
        counts = {phrase: lowered.count(phrase) for phrase in phrases}
        group_counts[group] = {k: v for k, v in counts.items() if v > 0}

    def density(count: int) -> float:
        return (count * 100 / token_count) if token_count else 0.0

    # 1. Kesin yazım hataları
    spelling_hits: list[str] = []
    for pattern, correction in SPELLING_RULES:
        for match in pattern.finditer(text):
            spelling_hits.append(f"{match.group(0)} → {correction}")
    if spelling_hits:
        findings.append(
            finding(
                "spelling-error", "error", len(spelling_hits),
                "TDK yazımına göre kesin hata; doğrudan düzelt.",
                spelling_hits[:6],
            )
        )

    # 2. Bürokratik geçiş kümelenmesi
    transition_total = sum(group_counts["bureaucratic_transitions"].values())
    if transition_total >= T_TRANSITION:
        findings.append(
            finding(
                "transition-cluster", "review", transition_total,
                "Kurumsal geçiş kalıpları kümeleniyor; her bağlacın gerçek bir ilişkiyi taşıyıp taşımadığını kontrol et.",
                sentence_examples(sentences, PHRASE_GROUPS["bureaucratic_transitions"]),
            )
        )

    # 3. Kanıtsız değerlendirme
    evaluation_total = sum(group_counts["empty_evaluations"].values())
    if evaluation_total >= T_EVALUATION:
        findings.append(
            finding(
                "unsupported-evaluation", "review", evaluation_total,
                "Değerlendirici ifadeler kümeleniyor; metinde zaten var olan kanıtla eşleştir, yoksa kaldır. Yeni ayrıntı uydurma.",
                sentence_examples(sentences, PHRASE_GROUPS["empty_evaluations"]),
            )
        )

    # 4. İçeriksiz çerçeve
    framing_total = sum(group_counts["meta_framing"].values())
    if framing_total >= T_FRAMING:
        findings.append(
            finding(
                "meta-framing", "review", framing_total,
                "Metin, içerik yerine konunun önemini anlatan üst çerçeve kalıplarını tekrarlıyor; silmeyi dene, bilgi kaybı olmuyorsa dolgudur.",
                sentence_examples(sentences, PHRASE_GROUPS["meta_framing"]),
            )
        )

    # 5. Çeviri kokusu
    translationese: dict[str, int] = {}
    for label, pattern in TRANSLATIONESE_PATTERNS.items():
        hits = len(pattern.findall(text))
        if hits:
            translationese[label] = hits
    translationese_total = sum(translationese.values())
    if translationese_total >= T_TRANSLATIONESE:
        findings.append(
            finding(
                "translationese", "review", translationese_total,
                "İngilizce cümle iskeleti belirtileri kümeleniyor (sahip olmak / gerçekleştirmek / sağlamak / yer almak). "
                "Eyleyeni bul, asıl fiili çıkar, cümleyi yeniden kur.",
                regex_examples(sentences, list(TRANSLATIONESE_PATTERNS.values())),
            )
        )

    # 6. -mektedir/-maktadır yoğunluğu
    maktadir_matches = MAKTADIR_RE.findall(text)
    if len(maktadir_matches) >= T_MAKTADIR[0] and density(len(maktadir_matches)) >= T_MAKTADIR[1]:
        findings.append(
            finding(
                "maktadir-density", "notice", len(maktadir_matches),
                "-mektedir/-maktadır yoğunlaşıyor; kip ve resmiyet anlamı korunuyorsa çeşitlendir.",
                regex_examples(sentences, [MAKTADIR_RE]),
            )
        )

    # 7. Cümle sonu kopula yığını
    copula_matches = COPULA_END_RE.findall(text)
    if len(copula_matches) >= T_COPULA[0] and density(len(copula_matches)) >= T_COPULA[1]:
        findings.append(
            finding(
                "copula-chain", "notice", len(copula_matches),
                "Cümleler ardı ardına -dır/-dir ile kapanıyor; çoğunda kopula düşürülebilir.",
                regex_examples(sentences, [COPULA_END_RE]),
            )
        )

    # 8. Edilgenlik
    passive_matches = PASSIVE_STEMS_RE.findall(text)
    if len(passive_matches) >= T_PASSIVE[0] and density(len(passive_matches)) >= T_PASSIVE[1]:
        findings.append(
            finding(
                "passive-cluster", "notice", len(passive_matches),
                "Edilgen gövdeler kümeleniyor; sorumluluk veya eyleyen belirsizleşiyorsa etkin yapıyı değerlendir.",
                regex_examples(sentences, [PASSIVE_STEMS_RE]),
            )
        )

    # 9. Karşıtlık şablonu
    contrast_matches = CONTRAST_RE.findall(text)
    if len(contrast_matches) >= 2:
        findings.append(
            finding(
                "contrast-template", "notice", len(contrast_matches),
                "'Sadece X değil, aynı zamanda Y' kalıbı tekrar ediyor; iki düşünce arasındaki gerçek ilişkiyi kontrol et.",
                regex_examples(sentences, [CONTRAST_RE]),
            )
        )

    # 10. Paragraf başı kalıbı
    starter_hits: list[str] = []
    for paragraph in paragraphs:
        paragraph_lower = tr_lower(paragraph).lstrip("\"“'‘-— ")
        for starter in PARAGRAPH_STARTERS:
            if paragraph_lower.startswith(starter):
                starter_hits.append(starter)
                break
    if len(starter_hits) >= T_STARTERS:
        findings.append(
            finding(
                "paragraph-starter-pattern", "review", len(starter_hits),
                "Birden çok paragraf hazır geçiş ifadesiyle başlıyor; akışın bağlaç olmadan da açık olup olmadığını sına.",
                starter_hits[:3],
            )
        )

    # 11. Tekdüze cümle uzunluğu
    if len(sentences) >= 4 and mean_length >= 12 and cv < T_CV:
        findings.append(
            finding(
                "uniform-sentence-length", "notice", len(sentences),
                "Cümle uzunlukları birbirine yakın. Tek başına sorun değildir; sesli okumada ritim gerçekten tekdüzeyse "
                "cümleyi bölmek yerine bilgi sırasını ve vurgu yerini değiştir.",
                [],
            )
        )

    # 12. Yasak: ara söz uzun çizgisi (demir kural 4)
    # Satır başındaki konuşma çizgisi TDK kuralıdır; sayımdan düşülür.
    dialogue_count = len(DIALOGUE_DASH_RE.findall(text))
    em_dash_count = len(EM_DASH_RE.findall(text)) - dialogue_count
    if em_dash_count > 0:
        # Örneklerde yalnızca ara söz kullanımı gösterilir; satır başındaki
        # konuşma çizgisi korunacağı için onu örnek olarak sunmak yanıltır.
        arasoz = [s for s in sentences if EM_DASH_RE.search(DIALOGUE_DASH_RE.sub("", s))]
        findings.append(
            finding(
                "em-dash", "error", em_dash_count,
                "Ara söz uzun çizgisi yasak. Virgül, parantez, kısa çizgi (-), iki nokta veya ayrı cümle "
                "ile değiştir. Satır başındaki konuşma çizgisi bu sayıma dahil değildir; "
                "alıntı ve kod içindeki çizgiye dokunma.",
                [s[:220] for s in arasoz[:3]],
            )
        )

    # 13. "X olarak biz…" kalıbı (demir kural 5)
    # Seviye 'review': betik alıntıyı, karşıtlık odağını ve hukuki taraf sıfatını
    # göremez; bunlar kuralın tanımlı istisnalarıdır (SKILL.md § Demir kural 5).
    olarak_sentences = [s for s in sentences if OLARAK_BIZ_RE.search(s) or OLARAK_ROL_RE.search(s)]
    if olarak_sentences:
        findings.append(
            finding(
                "olarak-kalibi", "review", len(olarak_sentences),
                "Marka/kurum/ekip adı + 'olarak' + biz-anlatımı. Özneyi doğrudan yaz: "
                "'X olarak yaptığımız' → 'X'in yaptığı'. Alıntı içindeyse, karşıtlık odağı taşıyorsa "
                "veya hukuki taraf sıfatı bildiriyorsa dokunma.",
                [s[:220] for s in olarak_sentences[:3]],
            )
        )

    # 14. Noktalı virgül yoğunluğu
    semicolon_count = text.count(";")
    if semicolon_count >= 3:
        findings.append(
            finding(
                "semicolon-density", "notice", semicolon_count,
                "Noktalı virgül yoğunluğu dikkat çekiyor; tür normu açısından doğrula, otomatik hata sayma.",
                [],
            )
        )

    return {
        "disclaimer": "Bu rapor AI yazarlığı veya metin kalitesi puanı değildir; bağlama bağlı editoryal uyarılar içerir.",
        "statistics": {
            "characters": len(text),
            "words": token_count,
            "paragraphs": len(paragraphs),
            "sentences": len(sentences),
            "mean_sentence_words": round(mean_length, 2),
            "sentence_length_std": round(std_length, 2),
            "sentence_length_cv": round(cv, 3),
        },
        "phrase_counts": {group: counts for group, counts in group_counts.items() if counts},
        "translationese_counts": translationese,
        "findings": findings,
    }


def render_text(report: dict[str, object]) -> str:
    stats = report["statistics"]
    lines = [
        str(report["disclaimer"]),
        "",
        (
            f"İstatistik: {stats['words']} sözcük, {stats['sentences']} cümle, "
            f"{stats['paragraphs']} paragraf; ortalama cümle {stats['mean_sentence_words']} sözcük."
        ),
    ]
    findings = report["findings"]
    if not findings:
        lines.extend([
            "",
            "Tanımlı eşikleri aşan bir belirti bulunmadı. Bu, metnin kusursuz veya insan yazımı olduğu anlamına gelmez.",
        ])
        return "\n".join(lines)
    lines.extend(["", "Uyarılar:"])
    for item in findings:
        lines.append(f"- [{item['level']}] {item['code']} ({item['count']}): {item['message']}")
        for example in item["examples"]:
            lines.append(f"    · {example}")
    return "\n".join(lines)


def read_input(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8-sig")
    return sys.stdin.read()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Türkçe metindeki editoryal belirtileri raporla; AI puanı üretme."
    )
    parser.add_argument("path", nargs="?", help="UTF-8 metin dosyası; verilmezse stdin okunur")
    parser.add_argument("--format", choices=("text", "json"), default="text", dest="output_format")
    args = parser.parse_args()

    try:
        text = read_input(args.path)
    except (OSError, UnicodeError) as exc:
        print(f"Girdi okunamadı: {exc}", file=sys.stderr)
        return 2
    if not text.strip():
        print("Boş metin analiz edilemez.", file=sys.stderr)
        return 2

    report = analyze(text)
    if args.output_format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
