---
name: avaz
description: Kullanıcı bu skill'i adıyla çağırdığında ("avaz", "/avaz") ya da bir Türkçe metni açıkça yeniden yazmasını, düzenlemesini, doğallaştırmasını veya "AI kokusunu" gidermesini istediğinde kullan. Kendiliğinden tetikleme: kullanıcı bir metni yalnızca özetliyor, çeviriyor, inceliyor veya alıntılıyorsa; normal sohbet yanıtları, commit mesajları ve kod yorumları söz konusuysa bu skill'i açma.
---

# Avaz

Türkçeyi yapay kusur ekleyerek değil; amacı, olguyu, kaydı ve yazarın sesini koruyarak iyileştir.

**Beş demir kural:**
1. **Olgu eklemez.** Metinde olmayan sayı, örnek, iddia, duygu veya neden uydurma. Boşluk varsa doldurma; işaretle ve kullanıcıdan iste.
2. **"AI yazmış" demez.** Yazarlık hükmü verme. Yalnızca metinde gözlenen editoryal belirtiyi, konumunu ve okuma etkisini raporla.
3. **Doğallık ≠ kusur.** Kasıtlı yazım yanlışı, tutarsızlık, rastgele argo, emoji, ünlem veya dolgu ekleyerek "insanlaştırma" yapma.
4. **Uzun çizgi (—) kullanmaz.** Bu skill'in dokunduğu hiçbir metinde em dash bulunmaz: ne üret, ne bırak. Girdide varsa temizle. Yerine virgül, parantez, kısa çizgi (-), iki nokta veya ayrı cümle. Ayrıntı: [references/turkce-dilbilgisi.md](references/turkce-dilbilgisi.md) § 3 Noktalama.
5. **"X olarak biz…" kalıbını kurmaz.** Marka, kurum, ekip veya rol adı + `olarak` + biz-anlatımı yasak. Özneyi doğrudan yaz. Ayrıntı: [references/turkce-dilbilgisi.md](references/turkce-dilbilgisi.md) § 1.1.

> "Aktaş Elektrik **olarak** ortaya koy**duğumuz** kalite ölçülebilir."
> → "Aktaş Elektrik'**in** ortaya koy**duğu** kalite ölçülebilir."

## İş akışı

1. **İşlem türünü belirle:** teşhis / hafif düzeltme / kapsamlı yeniden yazım / sıfırdan üretim.
2. **Koruma sözleşmesini çıkar:** özel adlar, sayılar, tarihler, alıntılar, ürün özellikleri, iddialar, kipler, olumsuzluklar, hukuki ifadeler. Bunlar dokunulmaz.
3. **Profili seç:** mecra, tür, hedef kitle, resmiyet, marka sesi. Güvenle çıkarılabiliyorsa sorma, uygula. Birleşik profil serbest (`kurumsal + sosyal`). Ayrıntı: [references/profiles.md](references/profiles.md).
4. **Belirtileri tara:** çeviri kokusu, boş çerçeve, kanıtsız değerlendirme, soyut ad zinciri, tekrar, mekanik bağlaç. 150+ sözcükte veya teşhis isteğinde `scripts/analyze_turkish.py` çalıştır. Belirti kataloğu: [references/signals.md](references/signals.md).
5. **Dört geçişte düzenle** (sırayı bozma):
   - **İçerik:** anlam, gönderim, olgu, mantık.
   - **Yapı:** bilgi sırası, paragraf odağı, söylem bağı.
   - **Dil:** yazım, ekler, noktalama, sözdizimi, gereksiz sözler. → [references/turkce-dilbilgisi.md](references/turkce-dilbilgisi.md)
   - **Ses:** profile uygun sözcük, ritim, vurgu, özgüllük.
6. **Kalite kapılarından geçir:** [references/quality-gates.md](references/quality-gates.md). 1. kapıda (korunan içerik) hata varsa teslim etme.
7. **İstenen biçimde teslim et:** kullanıcı yalnızca metin istediyse yalnızca metin. Aksi hâlde metin + 2–5 kısa değişiklik notu. Ayrıntılı sinyal raporunu yalnızca istenince ver.

## Kırmızı bayraklar

Aşağıdakiler yasağı bilmemekten değil, **iyi bir gerekçe bulmaktan** doğar. Kendini bu gerekçelerden birini kurarken yakalarsan dur.

| Gerekçe | Gerçek |
|---|---|
| "Bu paragraf çok soyut, somut bir ayrıntı gerekiyor" | Gerekiyor ama sende yok. Uydurulan rakam veya örnek olgu hatasıdır: boşluğu işaretle, kullanıcıdan iste. |
| "Kullanıcı 'doğallaştır' dedi, cümleleri kısaltayım" | Ritim uzunluktan değil bilgi vurgusundan gelir. Öğe sırasını değiştir, cümleyi bölme. |
| "'Ayrıca', 'bununla birlikte' klasik AI kalıbı, temizleyeyim" | İlişki gerçekse bağlaç kalır. Tek bir sözcük kanıt değildir; sildiğinde mantık bağı kopar. |
| "Aynı terim üç kez geçmiş, birini eş anlamlısıyla değiştireyim" | Hukuki, teknik ve marka terimlerinde tekrar zorunludur. Eş anlamlı = anlam kayması. |
| "Brief'te 'biz' dili var, o zaman 'X olarak' serbest" | Biz-anlatımı serbest, `olarak` kalıbı değil. "Biz ölçüyoruz" kurulur; "X olarak ölçüyoruz" kurulmaz. |
| "Girdideki uzun çizgiler yazarın üslup tercihi, dokunmayayım" | Kural girdiyi de kapsar. Temizle. |

## Türkçeye özgü çekirdek

En sık bozulma **çeviri kokusu**: İngilizce sözdiziminin Türkçe sözcüklerle kurulması. İlk taramada bunları ara:

| Kalıp | Onarım |
|---|---|
| `-e sahip` | sıfata çevir: "yüksek performansa sahip motor" → "yüksek performanslı motor" |
| `gerçekleştirmek` | asıl fiili kullan: "satın alma gerçekleştirdi" → "satın aldı" |
| `sağlamak` yardımcısı | "erişim sağlamak" → "erişmek" |
| `yer almak / bulunmak` | "listede yer alan ürünler" → "listedeki ürünler" |
| `olan / olmuş olan` | "yapılmış olan çalışma" → "yapılan çalışma" |
| gereksiz `bir` | "önemli bir rol oynamaktadır" → "belirleyicidir" / doğrudan işi yaz |
| her cümlede `-dır/-maktadır` | kip anlamı korunuyorsa geniş zaman veya belirli geçmiş |
| iyelik zinciri | "sürecin iyileştirilmesi çalışmasının yürütülmesi" → eyleyeni bul, fiille kur |
| gereksiz özne zamiri | Türkçe özneyi düşürür: "O, dedi ki..." → "Dedi ki..." / "…dedi." |

**Vurgu kuralı (Türkçenin motoru):** vurgulanan öğe **yüklemden hemen öncedir**. Bilinen bilgi başa, yeni bilgi yükleme yakın. "Toplantı yarın Ankara'da yapılacak" ile "Toplantı Ankara'da yarın yapılacak" farklı şeyler vurgular. Cümleyi canlandırmak istiyorsan sözcük değiştirme; **öğe sırasını değiştir**.

Ek, yazım, noktalama, ses ve ritim ayrıntısı: [references/turkce-dilbilgisi.md](references/turkce-dilbilgisi.md).

## Örnek: ne yapmalı, ne yapmamalı

**Girdi (kurumsal):**
> Günümüzün hızla değişen iş dünyasında, dijital dönüşüm her geçen gün daha da önem kazanmaktadır. Bu bağlamda, şirketimiz müşteri memnuniyetinin en üst düzeyde sağlanmasına yönelik çalışmaları titizlikle yürütmektedir. Bununla birlikte, sunmuş olduğumuz benzersiz çözümler sektörde vazgeçilmez bir rol oynamaktadır.

**Yanlış "doğallaştırma"** (akıcı ama uydurma):
> Çağrı merkezimizde bekleme süresini 4 dakikadan 45 saniyeye indirdik. 🎯 Bunu 20 talebi self-servis ekrana taşıyarak yaptık.

Rakam, kanal, yöntem, emoji: hiçbiri girdide yok. Bu düzenleme değil, kurgudur.

**Doğru çıktı:**
> Şirketimiz müşteri memnuniyetini artırmaya çalışıyor. Sunduğumuz çözümler sektörde kullanılıyor.
>
> Notlar:
> - Giriş paragrafı silindi: "hızla değişen iş dünyası / önem kazanmaktadır" hiçbir bilgi taşımıyordu.
> - "Benzersiz, vazgeçilmez" kaldırıldı; dayanağı yok.
> - Metinde tek bir doğrulanabilir ayrıntı yok. İskeleti doldurmak için şu üçü lazım: hangi çalışma, hangi ölçüt, hangi sonuç.

Kısaltmak marifet değil; **kalanın doğru olması** marifet. Boşluğu kullanıcı doldurur.

## Anlamı koruma kapısı

Yeniden yazımdan sonra karşılaştır:

- Kim ne yaptı: eyleyen ve etkilenen aynı mı?
- Olumsuzluk, olasılık, zorunluluk, koşul, istisna korundu mu? ("olabilir" → "olur", "bazı" → "tüm" oldu mu?)
- Sayı, tarih, kapsam aynı mı?
- Kaynağın görüşü kurumun kesin iddiası gibi sunuldu mu?
- Zamirler ve eksiltiler doğru gönderene bağlanıyor mu?

Sağlık, hukuk, finans ve itibar riski taşıyan metinlerde doğal söyleyiş uğruna **kesinlik derecesini ve yükümlülüğü değiştirme**. Şüpheliysen değiştirme; işaretle ve neden insan onayı gerektiğini söyle.

## Betik

```bash
python3 scripts/analyze_turkish.py metin.txt
```

```bash
python3 scripts/analyze_turkish.py metin.txt --format json
```

Betik AI puanı üretmez, eşik aşan editoryal belirtileri listeler. Uyarıyı nihai hüküm sayma: az cümleli metinde ritim ölçüleri, özel adlarda sözcük örüntüleri, alıntılarda noktalama sayıları yanıltır. Bulgu yoksa bu "metin iyi" demek değildir.

## Kaynaklar

Kaynakları topluca yükleme; yalnızca karar için gerekeni aç. Yazımda TDK, kurumsal dilde resmî rehberler, gerçek kullanım karşılaştırmasında derlemler. Rol, sınır ve lisans: [references/sources.md](references/sources.md).
