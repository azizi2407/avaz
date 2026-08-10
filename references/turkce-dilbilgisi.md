# Türkçeye özgü onarım kılavuzu

Bu dosya SKILL.md'nin "Dil" ve "Ses" geçişlerinde açılır. Genel editoryal belirtiler için `signals.md`'ye bak.

## 1. Çeviri kokusu

İngilizce sözdiziminin Türkçe sözcüklerle kurulması. LLM Türkçesindeki en yaygın bozulma budur ve tek tek sözcükler doğru olduğu için gözden kaçar.

| Kalıp | Neden bozuk | Onarım |
|---|---|---|
| `X'e sahip` (have) | Türkçe sahiplik `var` veya sıfat ekiyle kurulur | "geniş hafızaya sahip" → "geniş hafızalı" / "hafızası geniş" |
| `gerçekleştirmek` | asıl fiili örten yardımcı | "ödeme gerçekleştirdi" → "ödedi"; "toplantı gerçekleştirildi" → "toplandı / toplantı yapıldı" |
| `sağlamak` | aynı şekilde | "erişim sağlamak" → "erişmek"; "katkı sağlamak" → "katkıda bulunmak" |
| `yer almak`, `bulunmak` | İngilizce `located/included` kopyası | "raporda yer alan bulgular" → "rapordaki bulgular" |
| `olan`, `olmuş olan` | gereksiz sıfat-fiil katmanı | "tamamlanmış olan proje" → "tamamlanan proje" |
| `bir` fazlalığı | İngilizce `a/an` kopyası | "bu bir sorundur" → "bu bir sorun" ya da "sorun şu:"; "önemli bir rol oynar" → doğrudan işi yaz |
| `-dır/-dir` yığını | her cümleyi kopula ile kapatma | çoğunda kaldır: "Bu yöntem hızlıdır ve güvenlidir." → "Bu yöntem hızlı ve güvenli." |
| `-mektedir/-maktadır` yoğunluğu | tür gereği değilse mesafe ve tekdüzelik yaratır | kip anlamı korunuyorsa geniş zaman veya belirli geçmiş |
| iyelik/adlaştırma zinciri | eyleyen kaybolur | "sürecin iyileştirilmesine yönelik çalışmaların yürütülmesi" → "X ekibi süreci iyileştiriyor" |
| gereksiz özne zamiri | Türkçe özneyi çekimde taşır | "O, projeyi tamamladı. O, sonra rapor yazdı." → "Projeyi tamamladı, sonra rapor yazdı." |
| `ile ilgili olarak`, `açısından`, `konusunda`, `bazında` yığını | boş ilgeç katmanı | çoğu silinir veya tek ekle karşılanır: "maliyet açısından" → "maliyette" |
| İngilizce virgüllü liste | `A, B, ve C` | Türkçede son öğeden önce virgül yok: `A, B ve C` |
| Başlıkta İngilizce Büyük Harf | "Yeni Ürün Lansmanı Hakkında Bilgilendirme" | başlık cümleyse yalnızca ilk harf ve özel adlar büyük |

Bir metinde bu kalıpların üç dördü bir arada varsa sorun sözcük seçimi değil, cümle mimarisidir: eyleyeni bul, asıl fiili çıkar, cümleyi yeniden kur.

## 1.1. "X olarak biz…" kalıbı (yasak)

Kurumsal Türkçenin en yaygın klişesi. Marka, kurum, ekip veya rol adı `olarak` ile yan öğeye düşürülür, cümlenin öznesi kaybolur ve geriye yüzü olmayan bir "biz" kalır.

**Kural: kurum/marka/ekip/rol adı + `olarak` + biz-anlatımı kurma.** Özneyi doğrudan yaz.

| Yasak | Onarım |
|---|---|
| "Aktaş Elektrik **olarak** ortaya koy**duğumuz** kalite ölçülebilir." | "Aktaş Elektrik'**in** ortaya koy**duğu** kalite ölçülebilir." |
| "Firma **olarak** müşteri memnuniyetine önem veriyoruz." | "Müşteri memnuniyetine önem veriyoruz." / "Şirket müşteri memnuniyetine önem veriyor." |
| "Ekip **olarak** bu projeye inanıyoruz." | "Ekip bu projeye inanıyor." / "Bu projeye inanıyoruz." |
| "Bir tasarımcı **olarak** şunu düşünüyorum:" | "Tasarımcı gözüyle şunu düşünüyorum:" / doğrudan düşünceyi yaz |

Üç onarım yolu:

1. **Tamlama:** "X olarak yaptığımız" → "X'in yaptığı"
2. **Doğrudan özne:** "X olarak yapıyoruz" → "X yapıyor"
3. **Öğeyi sil:** kim konuştuğu bağlamdan belliyse "olarak" öbeğini tamamen kaldır, yalın biz-anlatımını bırak.

Biz-anlatımının kendisi yasak değildir; yasak olan `olarak` ile kurulan bu kalıptır. "Kaliteyi ölçüyoruz" serbesttir.

`olarak` sözcüğü, cümlenin öznesini gizlemediği yerlerde kalır: "Müdür olarak atandı", "Yedek olarak sakla", "Örnek olarak şunu verelim". Belirteç kuran kullanımlar (`sonuç olarak`, `genel olarak`, `ayrıntılı olarak`, `ek olarak`) biz-anlatımıyla birlikte gelse bile serbesttir: "Sonuç olarak bu yöntemi öneriyoruz" kurulabilir.

**Üç zorunlu istisna.** Kalıp şu durumlarda **korunur**, onarılmaz:

1. **Alıntı ve doğrudan konuşma içinde.** `Müdür, "Aktaş Elektrik olarak bu yatırımı tamamladık" dedi.` Tırnak içini onarmak, söylenmemiş bir cümleyi tırnak içinde bırakmaktır: olgu hatası, üslup düzeltmesi değil.
2. **Karşıtlık odağı taşıdığında.** "Şirket olarak değil, kişi olarak dava açtık." Buradaki `olarak` odak taşıyıcıdır; kaldırılırsa cümlenin anlamı gider.
3. **Hukuki veya resmî taraf sıfatı bildirdiğinde.** "Yüklenici olarak taahhüt ederiz", "Vekil olarak beyan ederiz." Taraf sıfatı hukuken işlevseldir; silinmesi hukuki etkiyi değiştirir.

**Onarım yolu 1'in yan etkisi.** "X olarak yaptığımız" → "X'in yaptığı" dönüşümü kişiyi birinci çoğuldan üçüncü tekile kaydırır. Metnin geri kalanı birinci çoğulsa paragraf içinde kişi tutarsızlığı doğar; o durumda yol 2 veya 3'ü kullan.

## 2. Vurgu ve öğe sırası

**Kural: vurgulanan öğe yüklemden hemen öncedir.** Türkçede canlılık sözcük değiştirerek değil, sıra değiştirerek gelir.

- "Sözleşmeyi **dün** imzaladık." → ne zaman sorusunu vurgular.
- "**Sözleşmeyi** dün imzaladık." → neyi sorusunu vurgular.
- "Dün sözleşmeyi **biz** imzaladık." → kimi vurgular.

Yanlış vurgu, dilbilgisi hatası vermediği için sessizce yanlış anlama yol açar. Yeniden yazımda yüklem öncesi öğenin değişip değişmediğini kontrol et.

**Bilgi akışı:** bilinen bilgi başta, yeni bilgi yükleme yakın. Paragraf içinde her cümle bir öncekinin sonundaki bilgiyi başında karşılamalı; bağdaşıklık böyle kurulur, bağlaç yığmakla değil.

**Devrik cümle:** yüklemden sonra öğe. Konuşmada, şiirde, reklamda doğaldır; kurumsal ve hukuki metinde ölçülü kullanılır. **Yazarın sesinde yoksa enjekte etme**, varsa düzleştirme.

## 3. Ek ve yazım tuzakları

### Bağlaç mı, ek mi

- **de/da bağlaç:** ayrı yazılır, sertleşmez. "Ben de geldim", "Kitap da güzeldi". *Te/ta biçimi yoktur.*
- **-de/-da bulunma eki:** bitişik, ünsüz uyumuna girer. "evde", "okulda", "kitapta", "raporda".
- Sınama: cümleden çıkarınca anlam bozulup "dahi/bile" işlevi kayboluyorsa bağlaçtır (ayrı).
- **ki bağlaç:** ayrı. "Biliyorum ki gelecek."
- **-ki ilgi/sıfat eki:** bitişik. "benimki", "yarınki toplantı", "masadaki dosya".
- Bitişik yazılan kalıplaşmışlar: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki.
- **Soru eki mi/mı:** ayrı yazılır, kendinden sonraki ekler bitişik. "gelecek mi", "yapar mısın", "doğru muydu".

### Kesme işareti

- Özel adlara gelen **çekim** ekleri kesme ile ayrılır: Ankara'da, Ahmet'in, Türkiye'nin, Nutuk'ta.
- Özel adlara gelen **yapım** ekleri ve sonrasındakiler ayrılmaz: Türkçenin, Konyalı, Avrupalılaşmak.
- **Kurum ve kuruluş adlarında** ekler ayrılmaz: Türk Dil Kurumundan, Türkiye Büyük Millet Meclisine, Sağlık Bakanlığına.
- **Kısaltmalarda** ayrılır: TBMM'nin, ABD'de, KDV'ye.
- **Sayılarda** ayrılır: 2026'da, %20'si, 15'inci, 3'ü.
- Özel adlarda **ünsüz yumuşaması yazıya yansımaz**: Sinop'un (Sinob'un değil), Zonguldak'a.

### Sık görülen yazım hataları

| Yanlış | Doğru |
|---|---|
| herşey | her şey |
| hiç bir | hiçbir |
| bir kaç | birkaç |
| bir çok | birçok |
| yada | ya da |
| herkez | herkes |
| yalnış | yanlış |
| süpriz | sürpriz |
| orjinal | orijinal |
| fark etmek → farketmek | fark etmek (ayrı) |
| gelicek, yapıcak | gelecek, yapacak (`-acak/-ecek` daralması yazıya geçmez) |

`-yor` öncesi daralma **yazılır**: bekliyor, anlıyor, atlıyor. İstisnalar: diyor, yiyor.

### Şapkalı harf (düzeltme işareti)

Anlam ayırt ediyorsa yaz: kâr (fayda) / kar (yağış), hâlâ / hala (teyze), âdet (gelenek) / adet (sayı), şûra / şura. Uzun ünlü ve incelik: kâğıt, dükkân, mahkûm, hükûmet, sükût. Nispet eki: askerî, millî, resmî, tarihî.

### Noktalama

- Türkçede seri virgülü yok: "A, B ve C".
- **Ara söz uzun çizgisi (em dash) yasaktır.** Ne üret, ne bırak. Girdide varsa temizle.
  - Ara söz: virgül, parantez veya kısa çizgi (-).
  - Açıklama, sonuç, liste girişi: iki nokta.
  - Zıtlık veya kopuş: nokta ile ayrı cümle, ya da noktalı virgül.
  - Aralık: kısa çizgi (2020-2024, s. 15-32).
  - Boşluklu uzun çizgi İngilizce tipografisidir ve LLM metinlerinin en görünür parmak izidir. Türkçe yazım kılavuzunda **ara söz** işareti değildir.
  - En dash (–), yatay çizgi (―) veya çift kısa çizgi (--) ile ikame etmek kaçıştır; işlevi Türkçe noktalamayla karşıla.
- **Konuşma çizgisi yasak değildir, korunur.** TDK'de işaretin adı zaten "Çizgi (—)" ve birincil işlevi budur: satır başında konuşmaları göstermek, oyunlarda konuşanın adından sonra gelmek. Diyalog metninde bu çizgiyi silmek karakter ayrımını yok eder.
  - Yasak olan **satır içi, boşluklu ara söz** kullanımıdır: "Rapor — ki uzundu — teslim edildi."
  - Korunan **satır başı** kullanımıdır: "— Nereye gidiyorsun?"
- Alıntı içindeki noktalama alıntının kendisine aittir; anlatıcının cümlesine karışmamalı.
- İki nokta, açıklama ya da liste gerçekten geliyorsa konur; süs olarak değil.

## 4. Ses ve ritim

Türkçe eklemeli bir dil olduğu için ritim sorunları çoğunlukla **ek yığılmasından** doğar, cümle uzunluğundan değil.

Kontrol listesi:
- **Aynı sesle biten yüklem zinciri:** art arda "-dır… -dır… -dır", "-yordu… -yordu…", "-lması… -lması…". Ses tekrarı monotonluğu kulakla duyulur; yapıyı değiştir, sözcüğü değil.
- **Ek zinciri:** "değerlendirilebilmesinin" gibi beş ekli sözcükler. Böl, adlaştırmayı fiile çevir.
- **-ma/-me adlaştırması yığını:** "yapılması, sağlanması, geliştirilmesi" aynı cümlede üç kez → eyleyeni bul.
- **Ünlü uyumu:** yabancı kökenli sözcüklerde ekin doğru biçimi (saat**e**, kalp**e** değil kalb**e**, gol**ü**, hukuk**u**).
- **Ulama ve nefes:** metni zihinde sesli oku. Nefes alınamayan yer varsa bilgi sırası hatalıdır; virgül eklemek çözüm değildir.

Son uyarı: **doğru ve doğal bir cümleyi yalnızca çeşitlilik olsun diye bozma.** Tekdüzelik gerçek bir okuma sorunu yaratmıyorsa dokunma.
