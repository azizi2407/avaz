# Türkçeye özgü onarım kılavuzu

Bu dosya SKILL.md'nin "Dil" ve "Ses" geçişlerinde açılır. Genel editoryal belirtiler için `signals.md`'ye bak.

## İçindekiler

- **§ 1 Çeviri kokusu** — İngilizce sözdiziminin Türkçe sözcüklerle kurulması; 16 kalıplık onarım tablosu
- **§ 1.1 "X olarak biz…" kalıbı** — yasak, üç onarım yolu, üç zorunlu istisna
- **§ 2 Vurgu ve öğe sırası** — yüklem öncesi kuralı, bilgi akışı, devrik cümle
- **§ 3 Ek ve yazım tuzakları** — de/da, ki, soru eki, kesme işareti, kısaltmaya ek, yabancı özel ad, birleşik fiil, ses olayları, büyük harf, sayı/tarih/saat/para, tırnak ve alıntı, `ile`, sık hatalar, ünlü daralması, şapkalı harf, noktalama ve uzun çizgi
- **§ 3.1 Kip, zaman ve tanıklık** — `-dı`/`-mış` ayrımı, kesinlik derecesi
- **§ 3.2 Terim tutarlılığı** — terim sözlüğü, İngilizce terim, melez fiil
- **§ 3.3 Kurumsal klişeler** — `olarak` dışındaki aile, neden yığını
- **§ 3.4 Türkçe karakter ve kapsayıcı dil**
- **§ 4 Ses ve ritim** — ek yığılması, ünlü uyumu, nefes

## 1. Çeviri kokusu

İngilizce sözdiziminin Türkçe sözcüklerle kurulması. LLM Türkçesindeki en yaygın bozulma budur ve tek tek sözcükler doğru olduğu için gözden kaçar.

| Kalıp | Neden bozuk | Onarım |
|---|---|---|
| `X'e sahip` (have) | Türkçe sahiplik `var` veya sıfat ekiyle kurulur | "geniş hafızaya sahip" → "geniş hafızalı" / "hafızası geniş" |
| `gerçekleştirmek` | asıl fiili örten yardımcı | "ödeme gerçekleştirdi" → "ödedi"; "toplantı gerçekleştirildi" → "toplandı / toplantı yapıldı" |
| `sağlamak` | aynı şekilde | "erişim sağlamak" → "erişmek"; "katkı sağlamak" → "katkıda bulunmak" |
| `yer almak`, `bulunmak` | İngilizce `located/included` kopyası | "raporda yer alan bulgular" → "rapordaki bulgular" |
| `olan`, `olmuş olan` | gereksiz sıfat-fiil katmanı | "tamamlanmış olan proje" → "tamamlanan proje" |
| `bir` fazlalığı | İngilizce `a/an` kopyası | "önemli **bir** rol oynar" → doğrudan işi yaz; "**bir** çözüm sunmaktadır" → "çözüm sunar". *"Bu bir sorundur" cümlesindeki `bir` fazlalık değildir, belirsizlik taşır: "sorunlardan biri".* |
| `-dır/-dir` yığını | her cümleyi kopula ile kapatma | kopulayı tümden atma, **tekrarı** kes: "Bu yöntem hızlıdır ve güvenlidir." → "Bu yöntem hızlı ve güvenlidir." Kopulayı büsbütün düşürmek ("hızlı ve güvenli") akademik ve teknik yazıda kayıt düşürür. |
| `-mektedir/-maktadır` yoğunluğu | tür gereği değilse mesafe ve tekdüzelik yaratır | kip anlamı korunuyorsa geniş zaman veya belirli geçmiş |
| iyelik/adlaştırma zinciri | eyleyen kaybolur | "sürecin iyileştirilmesine yönelik çalışmaların yürütülmesi" → "X ekibi süreci iyileştiriyor" |
| gereksiz özne zamiri | Türkçe özneyi çekimde taşır | "O, projeyi tamamladı. O, sonra rapor yazdı." → "Projeyi tamamladı, sonra rapor yazdı." |
| `ile ilgili olarak`, `açısından`, `konusunda`, `bazında` yığını | boş ilgeç katmanı | çoğu silinir veya tek ekle karşılanır: "maliyet açısından" → "maliyette" |
| İngilizce virgüllü liste | `A, B, ve C` | Türkçede son öğeden önce virgül yok: `A, B ve C`. Kural `veya`, `yahut`, `ya da` için de geçerli. |
| Cümle başı bağlacından sonra virgül | `However,` `Moreover,` kopyası | Türkçede konmaz: ~~"Ancak,"~~ → "Ancak"; ~~"Ayrıca,"~~ → "Ayrıca"; ~~"Bununla birlikte,"~~ → "Bununla birlikte". LLM Türkçesinin en yaygın noktalama parmak izi. |
| Tamlanan eki düşmesi | `project management process` doğrudan kopyalanınca ek kaybolur | "proje yönetim süreci" → "proje yönetim**i** süreci"; "müşteri memnuniyet anketi" → "müşteri memnuniyet**i** anketi" |
| İngilizce başlık sözdizimi | "Nasıl X Yapılır: 5 Adımda Eksiksiz Rehber" | Türkçe başlık ad öbeği veya doğrudan bildirimdir: "X nasıl yapılır" / "X yapmanın beş adımı". Büyük harf kuralı için § 3 Büyük harf. |

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
- **-ki ilgi/sıfat eki:** bitişik. "benimki", "yarınki toplantı", "masadaki dosya". Bu ek **ünlü uyumuna girmez**: yarın**ki**, akşam**ki**, sabah**ki**, onun**ki**. ~~yarınkı, dünki~~ İstisna (uyuma girenler): **bugünkü, dünkü, öbürkü**.
- Bitişik yazılan kalıplaşmışlar: belki, çünkü, hâlbuki, mademki, meğerki, oysaki, sanki.
- **Soru eki mi/mı:** ayrı yazılır, kendinden sonraki ekler bitişik. "gelecek mi", "yapar mısın", "doğru muydu".

### Kesme işareti

- Özel adlara gelen **çekim** ekleri kesme ile ayrılır: Ankara'da, Ahmet'in, Türkiye'nin, Nutuk'ta.
- Özel adlara gelen **yapım** ekleri ve sonrasındakiler ayrılmaz: Türkçenin, Konyalı, Avrupalılaşmak.
- **Kurum ve kuruluş adlarında** ekler ayrılmaz: Türk Dil Kurumundan, Türkiye Büyük Millet Meclisine, Sağlık Bakanlığına.
- **Kısaltmalarda** ayrılır: TBMM'nin, ABD'de, KDV'ye.
- **Sayılarda** ayrılır: 2026'da, %20'si, 15'inci, 3'ü.
- Özel adlarda **ünsüz yumuşaması yazıya yansımaz**: Sinop'un (Sinob'un değil), Zonguldak'a.
- Kesmeden **sonra boşluk bırakılmaz**: Ankara'da (~~Ankara' da~~). Belgede tek tip kesme karakteri kullan; `'` ile `’` karışmasın.

### Kısaltmaya ve yabancı özel ada ek

Ekin ünlüsünü **okunuş** belirler, yazılış değil.

- Harf harf okunan kısaltmalarda son harfin okunuşu esastır: **TDK'ye** (ke), **TRT'den** (te), **THY'de**, **TL'nin**, **ABD'de**, **AB'ye**. *TDK'ya yanlıştır.*
- Sözcük gibi okunan kısaltmalarda okunuşu esastır: **NATO'dan**, **UNESCO'ya**, **ASELSAN'da**, **BOTAŞ'ın**.
- Yabancı özel adlarda da okunuş esastır: **Bordeaux'ya**, **Rousseau'nun**, **Google'ın**, **iPhone'u**, **Renault'yu**, **Bosch'un**.

### Yabancı özel adların yazımı

Latin alfabeli dillerden alınanlar **özgün** yazılır: Shakespeare, Bordeaux, Chopin, München. Latin dışı alfabelerden alınanlar **okunuşuna göre**: Çaykovski, Şolohov, Puşkin, Pekin, Tahran, Kahire. Yerleşik Türkçe biçim varsa o kullanılır: Londra (~~London~~), Viyana (~~Wien~~). Aynı metinde bir adın iki biçimi bulunmaz.

### Birleşik fiil: bitişik mi, ayrı mı

Ad + `etmek/olmak/eylemek/kılmak` kalıbında ölçüt tek: **ad ses değişimine uğruyor mu?**

- **Uğruyorsa bitişik** (ünlü düşmesi veya ünsüz türemesi): kayıp→**kaybetmek**, af→**affetmek**, ret→**reddetmek**, his→**hissetmek**, zan→**zannetmek**, seyir→**seyretmek**, emir→**emretmek**, sabır→**sabretmek**, kayıp→**kaybolmak**.
- **Uğramıyorsa ayrı**: **fark etmek, hak etmek, terk etmek, arz etmek, not etmek, dans etmek, kontrol etmek, yardım etmek, teşekkür etmek, pişman olmak, memnun olmak, hasta olmak**.

Sınama: adı tek başına söyle. *Kayıp* → *kaybet-* (değişti, bitişik). *Fark* → *fark et-* (değişmedi, ayrı).

### Ses olayları ve ek biçimi

Dört ayrı olay; karıştırılmaları en sık görülen ek hatasıdır.

1. **Ünsüz benzeşmesi.** *f, s, t, k, ç, ş, h, p* ile biten sözcükte ek sert başlar: kitap**ta**, seç**ti**, aş**çı**, iş**çi**, Türk**çe**. ~~kitapda, seçdi~~
2. **Ünlü düşmesi (+ yumuşama).** ağız→**ağzı**, burun→**burnu**, alın→**alnı**, oğul→**oğlu**, gönül→**gönlü**, şehir→**şehre**, kalp→**kalbe**.
3. **Kalınlık-incelik uyumunun istisnaları.** Son ünlü kalın olduğu hâlde ek ince gelir: saat→**saate**, gol→**golü**, rol→**rolü**, kabul→**kabulü**, kontrol→**kontrolü**, alkol→**alkolü**, hakikat→**hakikati**, santral→**santrale**.
4. **Yumuşamayan sözcükler.** Tek heceliler ve bazı yabancı kökenliler son ünsüzünü korur: ok→**oku**, saç→**saçı**, at→**atı**, hukuk→**hukuku**, merak→**merakı**, ahlak→**ahlakı**, devlet→**devleti**. Bunlar ünlü uyumu açısından tamamen düzenlidir.

**Kaynaştırma:** iki ünlü arasına *y, ş, s, n* girer: soru**y**u, iki**ş**er, kapı**s**ı, o**n**a.

### Büyük harf

- **Başlık:** ana başlıkta her sözcüğün ilk harfi büyüktür (*Yeni Ürün Lansmanı Hakkında Bilgilendirme* doğrudur). İstisna: başlıkta geçen *ve, ile, ya, veya, yahut, ki, da/de* bağlaçları ve *mı/mi/mu/mü* soru eki küçük yazılır — *Suç ve Ceza*, *Leyla ile Mecnun*. **Alt başlıkta** yalnızca ilk sözcüğün ilk harfi büyüktür.
- **Unvan:** özel adla birlikteyse büyük (*Cumhurbaşkanı Recep Tayyip Erdoğan*, *Doktor Ayşe Yılmaz*), tek başına tür adıysa küçük (*cumhurbaşkanı seçildi*).
- **Yön adı:** özel ad parçasıysa büyük (*Doğu Anadolu*, *Batı Trakya*), coğrafi yön bildiriyorsa küçük (*evin doğusu*).
- Millet, dil, din ve mezhep adları büyük: *Türk, Türkçe, Müslüman, Sünni*.
- Kurum ve kuruluş adlarında her sözcük büyük: *Sağlık Bakanlığı*, *Türk Dil Kurumu*.
- **Ay ve gün adı** belirli bir tarihle geçiyorsa büyük (*29 Mayıs 1453*, *5 Aralık Cuma*), genel anlamdaysa küçük (*Okullar eylülde açılır*).

### Sayı, tarih, saat ve para

LLM'ler İngilizce ayraçları taşır; bunların hepsi kesin hatadır.

- Ondalık ayracı **virgül**, binlik ayracı **nokta**: `1.250,75 TL`. ~~1,250.75~~
- Saat **nokta** ile: `09.30`. ~~09:30~~ (ISO/İngilizce biçimi)
- Tarih: `12 Mart 2026`, `12.03.2026`. ~~03/12/2026~~ (belirsiz), `2026-03-12` yalnız teknik bağlamda.
- Yüzde işareti sayının **önünde**: `%25`, ekli biçimde `%25'i`. ~~25%~~
- Sıra sayısı: `15.` veya `15'inci`. ~~15.inci~~, ~~15'nci~~
- Üleştirme sayısı yalnız yazıyla: **ikişer, beşer**. ~~2'şer~~
- Birden çok sözcüklü sayılar ayrı yazılır: **üç yüz altmış beş**. Bitişik yazım yalnız çek/senette ve kalıplaşmışlarda (*onbaşı, birbiri*).

### Tırnak ve alıntı

Çift tırnak `" "`, iç tırnak tek tırnak `' '`; belgede tek tip. Alıntının kendi noktalaması tırnak **içinde**, anlatıcının noktalaması **dışında** kalır:

> Ali, "Yarın gelirim." dedi. / Ali "yarın geleceğini" söyledi.

Tırnak içindeki söz **değiştirilmez**; yazım hatası bile düzeltilmez. Düzeltme gerekiyorsa köşeli ayraçla belirtilir. Vurgu için tırnak kullanma (İngilizce *scare quotes* alışkanlığı); vurgu italikle verilir.

### `ile`, `ve/veya`

`ile` ayrı da bitişik de yazılır; bitişikte ünlü uyumuna girer ve ünlüden sonra `y` alır: *Ali ile / Ali'yle*, *araba ile / arabayla*, *kalem ile / kalemle*. Aynı metinde biçim tutarlı olmalı.

`ve/veya` yan yana yazımı hukuki metinde kabul görür, genel metinde kaçınılır: Türkçede *veya* zaten kapsayıcıdır. *ya… ya da* kalıbında ilk *ya* düşürülmez.

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

### Ünlü daralması

Üç kural, üç ayrı yer:

1. **`-yor` önünde daralma yazılır.** a/e ile biten fiillerde son ünlü ı/i/u/ü'ye döner ve bu yazıya geçer: başla→**başlıyor**, izle→**izliyor**, anla→**anlıyor**, atla→**atlıyor**, gelme→**gelmiyor**.
2. **`de-` ve `ye-` tek heceli oldukları hâlde daralır** ve `-y` ile başlayan *bütün* eklerden önce bu yazıya geçer: **diyor, diyen, diyerek, diyecek, diye; yiyor, yiyen, yiyerek, yiyecek, yiyip**. Asıl istisna budur — *diyor* ve *yiyor* 1. kuralın istisnası değil, kapsamıdır.
   - Bunun da istisnası: **deyince, deyip** (e korunur).
   - `-y` ile başlamayan eklerde daralma yok: **dedi, demiş, yedi, yemiş**.
3. **`-acak/-ecek` önünde daralma yazılmaz:** başla→**başlayacak**, gelme→**gelmeyecek**, izle→**izlemeyecek**, atla→**atlayarak**.

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

## 3.1. Kip, zaman ve tanıklık

Türkçenin en ayırt edici özelliği **tanıklık** ayrımıdır ve bu bir üslup meselesi değil, olgu meselesidir.

- `-dı` tanıklığa ve kesinliğe, `-mış` duyuma ve çıkarıma dayanır. Aynı anlatı içinde gerekçesiz değişmez.
- Haberde kaynağa dayanan bilgi `-dı` ile verilmez: *"Şirket zarar etti"* ≠ *"Şirketin zarar ettiği belirtildi"*. Bir kaynağın iddiasını `-dır` ile kesinleştirme; `-dığı öne sürüldü / bildirildi` mesafesini koru.
- Aynı paragrafta `-yor / -dı / -mış / -maktadır` gerekçesiz dönüşümlü kullanılmaz. Zaman ekseni bir kez kurulur, sonra korunur.
- Kesinlik derecesini yükseltme veya düşürme: *olabilir → olur*, *çoğu → tüm*, *yürütmektedir → çalışmaktadır* dönüşümlerinin hepsi olgu değişikliğidir.

## 3.2. Terim tutarlılığı ve İngilizce terim

Metne başlarken **terim sözlüğü** çıkar: bir kavram için tek karşılık seç, metin boyunca değiştirme.

- İlk geçişte biçim: *Türkçe karşılık (İngilizce özgün)*. Sonraki geçişlerde yalnız Türkçe.
- Yerleşmiş karşılık yoksa özgün biçim korunur, çeviri uydurulmaz; ek kesme ile gelir: *commit'i*, *branch'e*.
- **Melez fiil kurma:** ~~deploy etmek, update'lemek, handle etmek~~ → *yayına almak, güncellemek, karşılamak*.
- Arayüz metni, komut, parametre ve hata mesajı **çevrilmez**; korunan bölgedir.

## 3.3. Kurumsal klişeler

Demir kural 5 tek bir kalıbı yasaklar; aynı ailenin geri kalanı yasak değil ama **kümelendiğinde** cümle mimarisi bozuktur. Aynı paragrafta ikiden fazlası varsa yeniden kur.

*noktasında* ("bu konu noktasında" → "bu konuda"), *adına* ("başarı adına" → "başarı için"), *anlamında*, *bazında*, *özelinde*, *nezdinde*, *bünyesinde*, *çerçevesinde*, *kapsamında*, *yönelik*, *hayata geçirmek*, *değer katmak*, *fark yaratmak*, *çözüm ortağı*, *müşteri odaklı*, *bir adım öne çıkmak*, *sizlere/sizlerle*.

**Neden yığını:** *nedeniyle / sebebiyle / -den dolayı / -dığı için / dolayısıyla* aynı cümlede birden fazla kez kullanılmaz. Nedensellik bir kez adlandırılır.

## 3.4. Türkçe karakter ve kapsayıcı dil

**Karakter bütünlüğü.** `ı/i`, `İ/I`, `ş/s`, `ğ/g`, `ç/c`, `ö/o`, `ü/u` ayrımı korunur; ASCII'leştirilmiş girdi (*gorusme, ogrenci*) onarılır. Büyütme Türkçe kurallarına göre yapılır: `i → İ`, `ı → I`. `İSTANBUL`'un küçüğü *istanbul*, `IŞIK`'ın küçüğü *ışık*; İngilizce yerelleştirmeyle üretilmiş `ISTANBUL`, `ISIK` hatalıdır.

**Kapsayıcı dil.** Türkçede dilbilgisel cinsiyet yoktur; İngilizceden gelen cinsiyetlendirmeyi taşıma. *o* zamiri cinsiyetsizdir, "o/onun (erkek/kadın)" açımlaması yapma. Meslek adına gereksiz cinsiyet ekleme (~~kadın doktor, bayan öğretmen~~ → *doktor, öğretmen*); gerekliyse *kadın hekim*. *Bayan* yerine *kadın*, hitapta *Sayın*. Engellilikte kişi önce: *görme engelli kişi* (~~özürlü, sakat~~).

Bu değişiklikler **korunan bölgelere tabidir**: alıntıda, mevzuat metninde ve marka sözlüğünde geçen biçim değiştirilmez, işaretlenir.

## 4. Ses ve ritim

Türkçe eklemeli bir dil olduğu için ritim sorunları çoğunlukla **ek yığılmasından** doğar, cümle uzunluğundan değil.

Kontrol listesi:
- **Aynı sesle biten yüklem zinciri:** art arda "-dır… -dır… -dır", "-yordu… -yordu…", "-lması… -lması…". Ses tekrarı monotonluğu kulakla duyulur; yapıyı değiştir, sözcüğü değil.
- **Ek zinciri:** "değerlendirilebilmesinin" gibi beş ekli sözcükler. Böl, adlaştırmayı fiile çevir.
- **-ma/-me adlaştırması yığını:** "yapılması, sağlanması, geliştirilmesi" aynı cümlede üç kez → eyleyeni bul.
- **Ek biçimi:** üç ayrı ses olayı karıştırılmamalı, bkz. § 3 Ses olayları ve ek biçimi. Özetle: *saat**e*** kalınlık-incelik uyumunun istisnası, *kalb**e*** ünlü düşmesi + yumuşama, *hukuk**u*** ise yumuşamanın olmamasıdır ve ünlü uyumu açısından tamamen düzenlidir.
- **Ulama ve nefes:** metni zihinde sesli oku. Nefes alınamayan yer varsa bilgi sırası hatalıdır; virgül eklemek çözüm değildir.

Son uyarı: **doğru ve doğal bir cümleyi yalnızca çeşitlilik olsun diye bozma.** Tekdüzelik gerçek bir okuma sorunu yaratmıyorsa dokunma.
