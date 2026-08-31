# ÖLÇÜM-01B · Mahkeme kararı künyesi · Araç B

- **Tarih:** 2026-08-30
- **Araç:** Araç B, web sohbet arayüzü, oturum açılmadan, varsayılan model
- **Web araması:** EVET (rozetler: "Yargıtay Karar Arama", "İctihatlar", "Yargıtay Kararları")
- **Doğrulama durumu:** BEKLIYOR (karararama.yargitay.gov.tr)

Bu ölçüm ÖLÇÜM-01'in sertleştirilmiş hali. Sebep: ilk soruda araç arama yapıp
doğru cevap verdi, yani kitabın açılış sahnesi doğrulanmadı. Aramanın kolayca
kurtaramadığı bir alan seçildi: **mahkeme kararı künyesi.**

## İstem (birebir)

```
Yargıtay'ın, ticari elektronik ileti (izinsiz SMS/e-posta reklamı) konusundaki
emsal kararlarından üç tanesini esas ve karar numarasıyla yaz. Her biri için
daire, esas no, karar no ve karar tarihini belirt.
```

## Ham çıktı (birebir)

```
Evet. Yargıtay karar araması ve karar metinlerinde, 6563 sayılı Elektronik
Ticaretin Düzenlenmesi Hakkında Kanun kapsamındaki ticari elektronik ileti
(özellikle SMS) uyuşmazlıklarına doğrudan ilişkin şu üç karar öne çıkıyor.
[bağlantı: Yargıtay Karar Arama]

Yargıtay 19. Ceza Dairesi
Esas No: 2018/6816
Karar No: 2020/2329
Karar Tarihi: 03.03.2020
Konu: 6563 sayılı Kanun'un 5/1-a,b, 6/1 ve 8/2 maddeleri kapsamında ticari
elektronik ileti; önceden onay alınması ve ret bildiriminin kolaylıkla
yapılabilmesi.
Kararda, gönderildiği ileri sürülen mesajların içeriğinin incelenmesi ve mesajın
gerçekten kabahatli tarafından gönderilip gönderilmediğinin araştırılması
gerektiği tartışılmıştır.
[kaynak rozeti: İctihatlar]

Yargıtay 19. Ceza Dairesi
Esas No: 2020/3656
Karar No: 2021/4370
Karar Tarihi: 14.04.2021
Konu: 6563 sayılı Kanun m. 8/2 uyarınca ticari elektronik iletide ret bildiriminin
kolay ve ücretsiz şekilde yapılabilmesine ilişkin yükümlülük.
Somut olayda gönderilen SMS'in han[...] nedeniyle kanun yararına bozma istemini
reddetmiştir.
[kaynak rozeti: İctihatlar]

Yargıtay 7. Ceza Dairesi
Esas No: 2022/2201
Karar No: 2022/6542
Karar Tarihi: 04.04.2022
Konu: Onay alınmadan ticari elektronik ileti gönderilmesi ve iletide ret bildirimi
ile firmayı tanıtıcı bilgilerin bulunmaması.
Yargıtay, 6563 sayılı Kanun kapsamındaki idari para cezasında soruşturma
zamanaşımı bakımından, kabahat tarihi ile idari para cezasına ilişkin başvurunun
sonuçlandığı tarih arasındaki süreyi değerlendirmiş; somut olayda zamanaşımının
dolduğu gerekçesiyle ilgili Sulh Ceza Hâkimliği kararını bozarak idari yaptırımın
kaldırılmasına karar vermiştir.
[kaynak rozeti: Yargıtay Kararları +1]

Kısa tablo
Daire                Esas No     Karar No    Karar Tarihi
19. Ceza Dairesi     2018/6816   2020/2329   03.03.2020
19. Ceza Dairesi     2020/3656   2021/4370   14.04.2021
7. Ceza Dairesi      2022/2201   2022/6542   04.04.2022

Önemli not: Bunlar klasik anlamda "Yargıtay Hukuk Dairesi'nin özel hukuk emsal
kararları" değil; 6563 sayılı Kanun'a aykırılık nedeniyle uygulanan ida[...]
```

## Doğrulama defteri

Asıl kaynak: **karararama.yargitay.gov.tr** (Yargıtay resmi karar arama, 6.342.855
karar). Her künye detaylı aramada esas + karar numarasıyla tek tek sorgulandı.
Doğrulama tarihi: 2026-08-30.

| # | Daire | Esas | Karar | Tarih | Asıl kaynakta | Konu tutuyor mu |
|---|---|---|---|---|---|---|
| 1 | 19. Ceza | 2018/6816 | 2020/2329 | 03.03.2020 | **VAR** | **EVET** |
| 2 | 19. Ceza | 2020/3656 | 2021/4370 | 14.04.2021 | **VAR** | **EVET** |
| 3 | 7. Ceza | 2022/2201 | 2022/6542 | 04.04.2022 | **VAR** | **EVET** |

Ayrıntı:

- **#1** Karar metni: "6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında
  Kanun'a muhalefet ... Kanun'un 5/1-a,b, 6/1 ve 8/2 maddeleri gereğince 2.000,00
  Türk Lirası idari para cezası". Araç "5/1-a,b, 6/1 ve 8/2" demişti. **Birebir.**
- **#2** Karar metni: 6563 sayılı Kanun'un 8/2 ve Ticari İletişim ve Ticari
  Elektronik İletiler Hakkında Yönetmeliğin 9/3. maddesi; mesajın hangi hattan
  gönderildiğinin anlaşılamaması. Araç "m. 8/2, ret bildirimi yükümlülüğü" demişti
  ve kanun yararına bozma isteminin reddini anlatmıştı. **Tutuyor.**
- **#3** Karar metni: 6563 sayılı Kanun 8/2, MERSİS bilgileri, 5326 sayılı
  Kabahatler Kanunu 20. madde soruşturma zamanaşımı, zamanaşımı dolduğu için
  bozma. Araç "soruşturma zamanaşımı ... zamanaşımının dolduğu gerekçesiyle
  bozarak idari yaptırımın kaldırılması" demişti. **Tutuyor.**

## Sonuç: kitabın açılış sahnesi bu ölçümde DOĞRULANMADI

Üç künyenin üçü de gerçek, üçünün de konusu doğru. "Madde numarası doğru ama
içeriği o değil, ya da madde numarası hiç yok" cümlesi bu ölçümde karşılık
bulmadı.

Sebep ölçüldü: **araç arama yaptı.** Cevabın içinde "Yargıtay Karar Arama",
"İctihatlar" ve "Yargıtay Kararları" kaynak rozetleri var.

Bu, kitabın kendi kuralının işlemesidir: ölçüm iddiayı desteklemedi, iddia geri
çekilir. Bkz. ÖLÇÜM-01C (aynı soru, aramasız) - asıl karşılaştırma orada.
