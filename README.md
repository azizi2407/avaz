# Avaz

Türkçe metinleri anlamı ve olguları koruyarak doğal, akıcı ve bağlama uygun hâle getiren bir [Claude Code](https://claude.com/claude-code) skill'i.

*A Claude Code skill that rewrites Turkish text into natural, context-appropriate prose without altering its meaning or facts.*

[Türkçe](#türkçe) · [English](#english)

---

## Türkçe

### Ne yapar

Avaz, "AI kokusunu" yapay kusur ekleyerek gizlemez. Metnin gerçekten bozuk olan yerlerini onarır: çeviri kokusu, boş çerçeve, kanıtsız değerlendirme, soyut ad zinciri, yanlış vurgu, mekanik bağlaç.

Adı, sesin kendisinden gelir. Amaç metne yeni bir ses takmak değil, mevcut sesi duyulur kılmaktır.

### Beş demir kural

1. **Olgu eklemez.** Metinde olmayan sayı, örnek, iddia veya neden uydurulmaz. Boşluk varsa doldurulmaz; işaretlenir ve kullanıcıya sorulur.
2. **"AI yazmış" demez.** Yazarlık hükmü vermez. Yalnızca gözlenen editoryal belirtiyi, konumunu ve okuma etkisini raporlar.
3. **Doğallık kusur demek değildir.** Kasıtlı yazım yanlışı, rastgele argo, emoji, ünlem veya dolgu ekleyerek "insanlaştırma" yapmaz.
4. **Ara söz uzun çizgisi (—) kullanmaz.** Ne üretir ne bırakır; girdide varsa temizler. Yerine virgül, parantez, kısa çizgi, iki nokta veya ayrı cümle. Satır başındaki konuşma çizgisi TDK kuralıdır ve korunur.
5. **"X olarak biz…" kalıbını kurmaz.** Marka, kurum, ekip veya rol adı `olarak` ile yan öğeye düşürülmez; özne doğrudan yazılır. Karşıtlık odağı ve hukuki taraf sıfatı korunur.

> "Aktaş Elektrik **olarak** ortaya koy**duğumuz** kalite ölçülebilir."
> → "Aktaş Elektrik'**in** ortaya koy**duğu** kalite ölçülebilir."

Kurallar çatıştığında sıra bellidir:

> korunan bölgeler > kural 1 (olgu) > kural 2, 3 > kullanıcının o anki isteği > kural 4, 5 > profil varsayılanı

Kural 4 ve 5 biçim kurallarıdır. Bir alıntıyı değiştirmenin, bir olguyu kaydırmanın veya korunan bir bölgeye dokunmanın gerekçesi olamazlar: alıntı içindeki yasak kalıbı "düzeltmek", söylenmemiş bir cümleyi tırnak içinde bırakmak demektir.

### Kurulum

```bash
git clone https://github.com/azizi2407/avaz.git ~/.claude/skills/avaz
```

Claude Code'u yeniden başlat. Skill `avaz` adıyla görünür.

### Kullanım

```
/avaz
```

ya da doğrudan:

> Bu metni avaz ile düzenle: …

Skill dar tetiklenir: adıyla çağrıldığında ya da bir Türkçe metni açıkça düzenleme, sadeleştirme veya doğallaştırma isteğinde devreye girer. Özetleme, başka dile çevirme, salt yazım denetimi ve kısaltma isteklerinde açılmaması için `description` alanında negatif tetikleyici tanımlıdır. Bu bir eğilimdir, kesin bir kilit değildir.

### Yöntem

Avaz altı adımlı bir editoryal yordam uygular. Adımların sırası bağlayıcıdır; ses düzenlemesi en sona bırakılır, çünkü ritim müdahalesi anlam hatasını gizler.

**1. Koruma sözleşmesi.** Düzenlemeden önce dokunulmazlar listelenir: özel adlar, sayılar, tarihler, alıntılar, ürün özellikleri, iddialar, kipler, olumsuzluklar, hukuki ifadeler, komutlar ve dosya yolları.

**2. Profil seçimi.** Mecra, tür, hedef kitle ve resmiyet düzeyine göre dokuz profilden biri veya birleşimi seçilir: kurumsal, haber, sosyal medya, reklam, açıklayıcı, teknik dokümantasyon, editoryal, diyalog, hukuki. Birleşik profilde baskın profil içerik ve riski, yardımcı profil ritim ve mecrayı belirler; çakışmada risk taşıyan profil kazanır.

**3. Belirti taraması.** Şablonlu anlatım belirtileri üç ağırlıkta değerlendirilir:

| Ağırlık | Örnek | Kural |
|---|---|---|
| Güçlü | içeriksiz çerçeve, kanıtsız değerlendirme, soyut ad zinciri, referanssız genelleme, paragraf sonu yankısı | tek başına müdahale gerekçesi olabilir |
| Orta | bürokratik bağlaç kümelenmesi, `-maktadır` yoğunluğu, edilgenlik yığını, karşıtlık şablonu, aşırı açıklama | bağlam ve profil ile birlikte değerlendirilir |
| Düşük | noktalı virgül, devriklik, üçlü liste, cümle uzunluğu varyansı, birinci çoğul anlatım | tek başına asla kullanılmaz |

Bu ayrım kasıtlıdır. Tek bir sözcükten veya noktalama işaretinden yazarlık hükmü çıkarmak, insan metnini yanlışlıkla bozmanın en hızlı yoludur.

**4. Dört geçişli düzenleme.**

- *İçerik:* anlam, gönderim, olgu, mantık.
- *Yapı:* bilgi sırası, paragraf odağı, söylem bağı.
- *Dil:* yazım, ekler, noktalama, sözdizimi, gereksiz sözler.
- *Ses:* profile uygun sözcük, ritim, vurgu, özgüllük.

**5. Altı kalite kapısı.** Korunan içerik, dil doğruluğu, bilgi akışı, profil uyumu, doğallık, son sesli okuma. İlk kapı bloklayıcıdır: özne, sayı, kip veya kapsam değiştiyse metin teslim edilmez.

**6. Teslim biçimi.** Yalnızca metin, metin ve değişiklik notları, önce/sonra karşılaştırması, teşhis raporu veya eksik bilgi listesi. Metinde doğrulanabilir ayrıntı yoksa iskelet bırakılır ve eksikler sorulur.

#### Türkçeye özgü onarım

Skill'in çekirdeği dile bağımsız editoryal öğüt değildir. En sık bozulma, İngilizce sözdiziminin Türkçe sözcüklerle kurulmasıdır:

| Kalıp | Onarım |
|---|---|
| `-e sahip` | "yüksek performansa sahip motor" → "yüksek performanslı motor" |
| `gerçekleştirmek` | "satın alma gerçekleştirdi" → "satın aldı" |
| `sağlamak` | "erişim sağlamak" → "erişmek" |
| `yer almak` | "listede yer alan ürünler" → "listedeki ürünler" |
| `olmuş olan` | "yapılmış olan çalışma" → "yapılan çalışma" |
| iyelik zinciri | "sürecin iyileştirilmesi çalışmasının yürütülmesi" → eyleyeni bul, fiille kur |

Buna ek olarak vurgu kuralı uygulanır: Türkçede vurgulanan öğe yüklemden hemen öncedir. Cümleyi canlandırmak için sözcük değiştirilmez, öğe sırası değiştirilir. Ek, kesme işareti, şapkalı harf, soru eki ve birleşik yazım tuzakları ayrı bir başvuru dosyasında toplanmıştır.

### Kaynaklar

Kaynaklar toplu hâlde bağlama yüklenmez. Yalnızca verilecek karar için gereken katman açılır.

**Yazım ve söz varlığı.** Ayrı/bitişik biçim, çekim, anlam ve noktalama tartışmalarında başvurulur.

- [TDK Yazım Kılavuzu](https://tdk.gov.tr/tdk/kurumsal/yazim-kilavuzu/)
- [TDK noktalama açıklamaları](https://tdk.gov.tr/icerik/yazim-kurallari/noktalama-isaretleri-aciklamalar/)
- [Güncel Türkçe Sözlük](https://sozluk.gov.tr/)

**Derlemler.** Bir ifadenin gerçekte nasıl kullanıldığını, hangi kayda ait olduğunu ve eşdizimini karşılaştırmak için. Sıklık doğrulukla eşitlenmez.

- [TS Corpus](https://tscorpus.com/corpora)
- [LexiTR](https://lexitr.tscorpus.com/)
- [Türkçe Ulusal Derlemi](https://www.tnc.org.tr/)
- [Sözlü Türkçe Derlemi](https://std.metu.edu.tr/en/)

**Dilbilim ve NLP.** Biçimbilim, sözdizim, eylem rolleri ve söylem ilişkileri için. Araç çıktısı hüküm değil uyarı sayılır.

- [Zemberek NLP](https://github.com/ahmetaa/zemberek-nlp) (Apache-2.0): tokenizasyon, cümle sınırı, biçimbilim, normalizasyon
- [UD Turkish BOUN](https://github.com/UniversalDependencies/UD_Turkish-BOUN) (CC BY-SA 4.0): sözdizim örüntüleri
- [Turkish PropBank](https://github.com/StarlangSoftware/TurkishPropBank) (GPL-3.0): eylem ve katılımcı rolleri
- [Turkish Discourse Bank 1.2](https://arxiv.org/abs/2207.05008): açık ve örtük söylem ilişkileri
- [Turkish NLP Resources survey](https://arxiv.org/abs/2204.05042): araç ve veri keşfi
- [Türkçe okunabilirlik, hibrit öznitelikler](https://arxiv.org/abs/2306.03774)

**Üslup ve şablonlu anlatım araştırması.** Belirti kataloğunun editoryal temeli için.

- [Measuring AI Slop in Text](https://arxiv.org/abs/2509.19163)
- [Exploring Register Variation in Turkish Web Corpus](https://www.utupub.fi/handle/10024/190866)

**Editoryal ve kurumsal rehberler.** Anadolu Ajansı "Türkçeyi Doğru Kullan" kartları (medya dili), RTÜK Yayın İlkeleri Rehberi (yayın sorumluluğu), AB Mevzuatı Çeviri Rehberi (terim tutarlılığı), MEB yazma rubrikleri (amaç, düzen, bağdaşıklık). Hiçbiri bütün türlerin üslup normu sayılmaz.

**Kullanılmayan kaynaklar.** [ISO 24495-1](https://www.iso.org/standard/78907.html) metni lisans nedeniyle skill'e gömülmez; ISO sayfası yapay zekâ kullanımını ayrıca sınırlar. [ASD-STE100](https://www.asd-ste100.org/) telifli kontrollü İngilizce standardı Türkçe kural kitabına çevrilmez. Lisansı belirsiz veri ve kitap metinleri indirilmez, yeniden dağıtılmaz, belirli bir yazarı taklit etmek için örnek bankasına dönüştürülmez.

### Betik

Bağımlılığı yoktur, Python 3.9 ve üzeri yeterlidir.

```bash
python3 scripts/analyze_turkish.py metin.txt
python3 scripts/analyze_turkish.py metin.txt --format json
cat metin.txt | python3 scripts/analyze_turkish.py -
```

Skill içinden çağrılırken çalışma dizini genellikle kullanıcının projesidir; bu yüzden SKILL.md göreli yol değil `${CLAUDE_SKILL_DIR}` (ya da plugin kurulumunda `${CLAUDE_PLUGIN_ROOT}`) üzerinden mutlak yol kullanır.

| Bayrak | İşlev |
|---|---|
| `--format json` | makine okunur çıktı; `schema_version`, `summary` ve bulgu başına `spans` içerir |
| `--fail-on error` | o seviyede bulgu varsa 1 ile çıkar (CI için) |
| `--max-examples N` | bulgu başına örnek cümle sayısı |
| `--compact` | boşluksuz JSON |

Çıkış kodları: `0` temiz, `1` eşik aşıldı, `2` kullanım hatası, `3` girdi okunamadı.

Bulgu seviyeleri: `error` (TDK'ye göre kesin yazım hatası veya demir kural ihlali), `review` (okuma etkisi olası), `notice` (yalnızca başka belirtilerle birlikte anlamlı).

Betik yazarlık puanı üretmez. Bulgu çıkmaması metnin iyi olduğunu, bulgu çıkması metnin yapay zekâ ürünü olduğunu göstermez. Betik korunan bölgeleri göremez: özel adı, alıntıyı, kod bloğunu ve şablon değişkenini ayırt edemediği için `error` seviyesindeki bulgular bile bağlamla doğrulanmalıdır.

### Test ve değerlendirme

```bash
pip install -e ".[dev]"
pytest -q
```

İki katman var. `tests/` betiği deterministik olarak sınar: her kural için etiketli bir korpusta kesinlik ve duyarlılık kapısı, CLI sözleşmesi, altın çıktılar, ReDoS zaman kapısı ve skill paketinin bütünlüğü (frontmatter geçerli YAML mı, bağlantılar kırık mı). `evals/` ise skill'in davranışını ölçer: olgu tuzağı, alıntı koruma, konuşma çizgisi, kod bloğu, enjeksiyon, hukuki kesinlik, erozyon ve negatif tetikleme vakaları.

Kural eklerken korpusa hem yakalanması hem **yakalanmaması** gereken örnekler eklenir. Kesinlik duyarlılıktan önce gelir: yanlış pozitif, doğru yazılmış bir insan metnini bozmak demektir.

### Dosya yapısı

| Dosya | İçerik |
|---|---|
| `SKILL.md` | Demir kurallar, iş akışı, kırmızı bayraklar, Türkçe çekirdek |
| `references/turkce-dilbilgisi.md` | Çeviri kokusu, `olarak` kalıbı, vurgu ve öğe sırası, ek ve yazım tuzakları, ritim |
| `references/ornekler.md` | Profil profil önce/sonra örnekleri |
| `references/profiles.md` | Dokuz yazı profili ve birleşim kuralı |
| `references/signals.md` | Şablonlu anlatım belirtileri ve ağırlıkları |
| `references/quality-gates.md` | Teslim öncesi altı kapı |
| `references/teslim-ve-sinirlar.md` | Müdahale şiddeti, teslim biçimi, uzun metin, yineleme, işaretleme |
| `references/sources.md` | Kaynak yönlendirmesi ve lisans sınırları |
| `scripts/analyze_turkish.py` | Eşik aşan editoryal belirtileri listeler |
| `tests/`, `evals/` | Deterministik testler ve davranışsal değerlendirme vakaları |

### Sınırlar

Avaz bir yapay zekâ dedektörü değildir ve öyle kullanılamaz. Bildirdiği her belirti insan metninde de bulunabilir.

**Dedektör atlatma aracı da değildir.** Piyasadaki "humanizer" araçlarının çoğu, metne kasıtlı kusur ekleyerek yapay zekâ dedektörlerini şaşırtmayı hedefler. Avaz'ın tasarımı bunun tam tersidir: metne kusur eklemez, olguyu korur ve neyi neden değiştirdiğini söyler. Amacı bir denetimden geçmek değil, metnin gerçekten bozuk yerlerini onarmaktır.

Betiğin çıktısı bir hüküm değil, uyarıdır. Betik korunan bölgeleri (özel ad, alıntı, kod, şablon değişkeni) göremez; bu yüzden `error` seviyesindeki bulguları bile bağlamla doğrulamak gerekir.

Sağlık, hukuk, finans ve itibar riski taşıyan metinlerde kesinlik derecesi ve yükümlülük değiştirilmez; şüpheli ifade düzeltilmez, işaretlenir ve insan onayına bırakılır.

### Lisans

MIT. Bkz. [LICENSE](LICENSE).

---

## English

### What it does

Avaz does not hide the "AI smell" by injecting artificial flaws. It repairs what is genuinely broken in the text: translationese, empty framing, unsupported evaluation, abstract nominalisation chains, misplaced emphasis, mechanical connectives.

The name comes from the Turkish word for a raised voice. The goal is not to fit the text with a new voice but to make the existing one audible.

### Five iron rules

1. **It adds no facts.** No invented figure, example, claim or cause. Gaps are flagged and returned to the user, never filled.
2. **It never claims "an AI wrote this".** No authorship verdict. It reports the observed editorial symptom, its location and its effect on reading.
3. **Natural does not mean flawed.** No deliberate typos, random slang, emoji, exclamation marks or filler added in the name of sounding human.
4. **No parenthetical em dash (—).** Neither produced nor left in place; removed from input as well. Commas, parentheses, hyphens, colons or separate sentences instead. A line-initial dialogue dash is a TDK rule and is preserved.
5. **No "as X, we…" construction.** A brand, company, team or role name is never demoted to an adverbial with `olarak`; the subject is written directly.

> "Aktaş Elektrik **olarak** ortaya koy**duğumuz** kalite ölçülebilir."
> → "Aktaş Elektrik'**in** ortaya koy**duğu** kalite ölçülebilir."
> *(As Aktaş Elektrik, the quality we deliver is measurable. → The quality Aktaş Elektrik delivers is measurable.)*

### Installation

```bash
git clone https://github.com/azizi2407/avaz.git ~/.claude/skills/avaz
```

Restart Claude Code. The skill appears as `avaz`.

### Usage

```
/avaz
```

or directly:

> Edit this text with avaz: …

The skill triggers narrowly: by name, or on an explicit request to rewrite, simplify or naturalise a Turkish text. Negative triggers in the `description` field keep it closed for summarising, translating into another language, plain spell-checking and shortening. This is a tendency, not a hard lock.

### Method

Avaz applies a six-step editorial procedure. The order is binding: voice work comes last, because rhythm edits mask meaning errors.

**1. Preservation contract.** Before any edit, the untouchables are listed: proper nouns, figures, dates, quotations, product attributes, claims, moods, negations, legal wording, commands and file paths.

**2. Profile selection.** One of nine profiles, or a combination, is chosen by medium, genre, audience and formality: corporate, news, social media, advertising, explanatory, technical documentation, editorial, dialogue, legal. In a combined profile the dominant one governs content and risk while the secondary governs rhythm and medium; on conflict, the risk-bearing profile wins.

**3. Symptom scan.** Templated-writing symptoms are weighted in three tiers:

| Weight | Example | Rule |
|---|---|---|
| Strong | empty framing, unsupported evaluation, nominalisation chain, unsourced generalisation, paragraph-end echo | may justify intervention on its own |
| Medium | bureaucratic connective clustering, `-maktadır` density, passive pile-up, contrast template, over-explanation | judged together with context and profile |
| Low | semicolons, inversion, rule of three, sentence-length variance, first person plural | never used on its own |

The distinction is deliberate. Inferring authorship from a single word or punctuation mark is the fastest way to damage human writing by mistake.

**4. Four editing passes.**

- *Content:* meaning, reference, fact, logic.
- *Structure:* information order, paragraph focus, discourse cohesion.
- *Language:* orthography, suffixes, punctuation, syntax, redundancy.
- *Voice:* profile-appropriate diction, rhythm, emphasis, specificity.

**5. Six quality gates.** Preserved content, linguistic accuracy, information flow, profile fit, naturalness, final read-aloud. The first gate blocks delivery: if subject, figure, mood or scope changed, the text is not handed over.

**6. Delivery format.** Text only, text plus change notes, before/after comparison, diagnostic report, or a list of missing information. When the source contains no verifiable detail, the skeleton is left standing and the gaps are asked about.

#### Turkish-specific repair

The core of this skill is not language-agnostic editorial advice. The most frequent failure is English syntax built out of Turkish words: `-e sahip` for *have*, the auxiliaries `gerçekleştirmek` and `sağlamak` masking the real verb, `yer almak` copying *located in*, redundant `bir` copying the English article, and possessive chains that bury the agent.

On top of that, an emphasis rule applies: in Turkish the stressed element sits immediately before the predicate. To enliven a sentence the skill reorders constituents rather than swapping words. Suffix, apostrophe, circumflex, question-particle and compound-spelling traps are collected in a separate reference file.

### Sources

Sources are never loaded into context in bulk. Only the layer needed for the decision at hand is opened.

**Orthography and lexicon.** Consulted for spacing, inflection, meaning and punctuation disputes: [TDK Spelling Guide](https://tdk.gov.tr/tdk/kurumsal/yazim-kilavuzu/), [TDK punctuation notes](https://tdk.gov.tr/icerik/yazim-kurallari/noktalama-isaretleri-aciklamalar/), [Contemporary Turkish Dictionary](https://sozluk.gov.tr/).

**Corpora.** For how an expression is actually used, which register it belongs to, and its collocations. Frequency is not equated with correctness: [TS Corpus](https://tscorpus.com/corpora), [LexiTR](https://lexitr.tscorpus.com/), [Turkish National Corpus](https://www.tnc.org.tr/), [Spoken Turkish Corpus](https://std.metu.edu.tr/en/).

**Linguistics and NLP.** For morphology, syntax, predicate roles and discourse relations. Tool output counts as a warning, never a verdict: [Zemberek NLP](https://github.com/ahmetaa/zemberek-nlp) (Apache-2.0), [UD Turkish BOUN](https://github.com/UniversalDependencies/UD_Turkish-BOUN) (CC BY-SA 4.0), [Turkish PropBank](https://github.com/StarlangSoftware/TurkishPropBank) (GPL-3.0), [Turkish Discourse Bank 1.2](https://arxiv.org/abs/2207.05008), [Turkish NLP Resources survey](https://arxiv.org/abs/2204.05042), [Turkish readability with hybrid features](https://arxiv.org/abs/2306.03774).

**Style and templated-writing research.** The editorial basis of the symptom catalogue: [Measuring AI Slop in Text](https://arxiv.org/abs/2509.19163), [Exploring Register Variation in Turkish Web Corpus](https://www.utupub.fi/handle/10024/190866).

**Editorial and institutional guides.** Anadolu Agency "Use Turkish Correctly" cards (media language), RTÜK Broadcasting Principles Guide (broadcast responsibility), EU Legislation Translation Guide (term consistency), Ministry of Education writing rubrics (purpose, organisation, cohesion). None of these is treated as the style norm for every genre.

**Excluded sources.** The [ISO 24495-1](https://www.iso.org/standard/78907.html) text is not embedded for licensing reasons, and the ISO page separately restricts AI use. [ASD-STE100](https://www.asd-ste100.org/), a copyrighted controlled-English standard, is not converted into a Turkish rulebook. Data and book texts of unclear licence are not downloaded, redistributed, or turned into a sample bank for imitating a named author.

### Script

No dependencies; Python 3.9 or later is enough.

```bash
python3 scripts/analyze_turkish.py text.txt
python3 scripts/analyze_turkish.py text.txt --format json
cat text.txt | python3 scripts/analyze_turkish.py -
```

When invoked from the skill the working directory is usually the user's project, so SKILL.md resolves an absolute path through `${CLAUDE_SKILL_DIR}` (or `${CLAUDE_PLUGIN_ROOT}` for a plugin install) rather than a relative one.

`--fail-on error` exits 1 when a finding at that level exists (for CI); `--max-examples N` and `--compact` control output size. Exit codes: `0` clean, `1` threshold exceeded, `2` usage error, `3` unreadable input.

Finding levels: `error` (definite spelling error per TDK, or an iron-rule violation), `review` (likely reading impact), `notice` (meaningful only alongside other symptoms).

The script produces no authorship score. An empty report does not mean the text is good, and a full one does not mean the text was machine-written. The script cannot see protected regions — proper nouns, quotations, code blocks, template variables — so even `error` findings must be confirmed against context.

### Tests and evaluation

```bash
pip install -e ".[dev]"
pytest -q
```

Two layers. `tests/` checks the script deterministically: per-rule precision and recall gates over a labelled corpus, the CLI contract, golden outputs, a ReDoS timing gate, and the integrity of the skill package itself. `evals/` measures the skill's behaviour: fact-injection traps, quotation and code-block preservation, dialogue dashes, prompt injection, legal certainty, erosion across repeated passes, and negative triggering.

### Limits

Avaz is not an AI detector and cannot be used as one. Every symptom it reports can also occur in human writing.

**Nor is it a detector-bypass tool.** Most "humanizer" products aim to fool AI detectors by injecting deliberate flaws. Avaz is built the other way round: it adds no flaws, preserves the facts, and states what it changed and why. The goal is not to pass an audit but to repair what is genuinely broken.

In medical, legal, financial and reputation-sensitive texts it never alters degree of certainty or obligation; a doubtful phrase is flagged for human review rather than corrected.

### License

MIT. See [LICENSE](LICENSE).
