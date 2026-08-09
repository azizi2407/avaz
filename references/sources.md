# Kaynak yönlendirmesi ve sınırlar

Kaynakları yalnızca gereken karar için kullan. Bir kaynağın varlığı, her metinde bağlama yüklenmesi gerektiği anlamına gelmez. Skill'in çalışması hiçbir dış kaynağa veya haricî klasöre bağımlı değildir; internet erişimi yoksa `turkce-dilbilgisi.md` yeter.

## Yazım ve söz varlığı

- TDK Yazım Kılavuzu: https://tdk.gov.tr/tdk/kurumsal/yazim-kilavuzu/
- TDK noktalama açıklamaları: https://tdk.gov.tr/icerik/yazim-kurallari/noktalama-isaretleri-aciklamalar/
- Güncel Türkçe Sözlük: https://sozluk.gov.tr/

Yazım, ayrı/bitişik biçim, anlam ve çekim tartışmasında tek madde sorgula. Siteleri topluca kazıma veya sözlük içeriğini skill'e kopyalama.

## Editoryal ve kurumsal rehberler

- Anadolu Ajansı "Türkçeyi Doğru Kullan" kartları: sık medya dili hataları.
- RTÜK Yayın İlkeleri Rehberi: kamusal/yayın iletişiminde sorumluluk.
- AB Mevzuatı Çeviri Rehberi: terim tutarlılığı, çeviri kokusunu azaltma.
- MEB yazma rubrikleri: amaç, düzen, bağdaşıklık boyutları.

Bunlardan birini bütün türlerin üslup normu yapma. Kurumsal/teknik kuralı edebî metne taşımadan önce profil uyumunu kontrol et.

## Derlemler

- TS Corpus: https://tscorpus.com/corpora
- LexiTR: https://lexitr.tscorpus.com/
- Türkçe Ulusal Derlemi: https://www.tnc.org.tr/
- Sözlü Türkçe Derlemi: https://std.metu.edu.tr/en/

İfade, eşdizim, dönem ve kayıt karşılaştırmasında kullan. **Sıklığı doğrulukla eşitleme.** Alt derlemin türünü ve erişim koşulunu kaydet; telifli tam metni skill'e gömme.

## Dilbilim ve NLP

- Zemberek NLP (https://github.com/ahmetaa/zemberek-nlp): tokenizasyon, cümle sınırı, biçimbilim, normalizasyon; Apache-2.0.
- UD Turkish BOUN (https://github.com/UniversalDependencies/UD_Turkish-BOUN): sözdizim örüntüleri; CC BY-SA 4.0.
- Turkish PropBank (https://github.com/StarlangSoftware/TurkishPropBank): eylem ve katılımcı rolleri; GPL-3.0.
- Turkish Discourse Bank 1.2 (https://arxiv.org/abs/2207.05008): açık/örtük söylem ilişkileri.
- Turkish NLP Resources survey (https://arxiv.org/abs/2204.05042): araç ve veri keşfi.
- Türkçe okunabilirlik (hibrit öznitelikler): https://arxiv.org/abs/2306.03774

Araç çıktısını hüküm değil uyarı say. Okunabilirliği doğallıkla, sözdizimsel yaygınlığı estetik zorunlulukla eşitleme.

## Slop ve üslup araştırması

- Measuring AI Slop in Text: https://arxiv.org/abs/2509.19163
- Exploring Register Variation in Turkish Web Corpus: https://www.utupub.fi/handle/10024/190866
- MIT lisanslı aday sinyal kataloğu: https://github.com/bushrabeg/turkce-humanizer

Bu kaynaklardan **yazarlık dedektörü üretme**. Belirtileri açıklık, özgüllük, tekrar ve profil uyumu gibi editoryal etkiler üzerinden değerlendir.

## Kullanılmayacak veya kısıtlı kaynaklar

- ISO 24495-1 metnini izin olmadan prompta veya skill'e gömme; ISO sayfası yapay zekâ kullanımını ayrıca sınırlar: https://www.iso.org/standard/78907.html
- ASD-STE100 telifli kontrollü İngilizce standardını Türkçe kural kitabına dönüştürme: https://www.asd-ste100.org/
- Lisansı belirsiz veri veya kitap metinlerini indirme, yeniden dağıtma ya da belirli bir yazarı taklit etmek için örnek bankası yapma.
