# ÖLÇÜM-01E · Aynı soru, üçüncü araç · Araç A

- **Tarih:** 2026-08-30
- **Araç:** Araç A, web sohbet arayüzü, **oturum açık**, en güçlü model, "yüksek" ayar
- **Web araması:** **EVET** (arayüz "Searched the web" yazdı, iki ayrı arama, 7 + 9 sonuç)
- **Sonuç:** **Künye vermeyi REDDETTİ.** Üç aracın üçüncü ve tamamen farklı davranışı.

## İstem (birebir, ÖLÇÜM-01B ve 01D ile aynı)

```
Yargıtay'ın, ticari elektronik ileti (izinsiz SMS/e-posta reklamı) konusundaki
emsal kararlarından üç tanesini esas ve karar numarasıyla yaz. Her biri için
daire, esas no, karar no ve karar tarihini belirt.
```

## Ham çıktı (birebir)

```
Bu isteğe uydurma bir cevap veremem: elimde, doğruluğunu teyit edebildiğim üç
Yargıtay kararının esas/karar numarası yok. Karar numarası uydurmak dilekçeye
konulduğunda size ciddi zarar verir, o yüzden boş numara üretmek yerine durumu
açıklayayım.

Neden bu kadar zor?

Bu alanda "klasik" bir Yargıtay içtihat külliyatı beklendiği kadar geniş değil,
çünkü uyuşmazlıkların çoğu Yargıtay'a hiç ulaşmıyor:

- 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun kapsamındaki
  izinsiz ileti cezaları Ticaret Bakanlığı tarafından idari para cezası olarak
  veriliyor; bunlara karşı itiraz yolu Yargıtay temyizi ile sonuçlanmıyor.
- KVKK boyutu Kişisel Verileri Koruma Kurulu kararları ve ardından idari yargı
  üzerinden ilerliyor.
- Manevi tazminat davaları ise genellikle tüketici mahkemesi + istinaf (BAM)
  aşamasında kesinleşiyor; parasal sınır nedeniyle temyiz edilemiyor. Bu yüzden
  bu konudaki en zengin içtihat aslında Bölge Adliye Mahkemesi kararlarında.

Arama sırasında karşıma çıkan tek somut atıf (13. HD, 2017/1118 E., 2018/342 K.)
bir avukatlık bürosu blogunda geçiyor ve resmi kaynakta doğrulayamadım - bu tür
bloglarda üretilmiş sahte künyeler sık görülüyor, kullanmadan önce mutlaka teyit
edin.

Nereden gerçek karar bulursunuz

- karararama.yargitay.gov.tr - ücretsiz, tam metin arama. "ticari elektronik
  ileti", "izinsiz sms", "istenmeyen elektronik posta", "6563 sayılı Kanun" gibi
  ifadelerle arayın.
- UYAP Emsal (emsal.uyap.gov.tr) - hem Yargıtay hem BAM kararları; bu konuda asıl
  verimli kaynak burası.
- Lexpera / Kazancı / Jurix - abonelikliyse konu başlığı bazlı tarama çok daha
  isabetli.
- KVKK tarafı için kvkk.gov.tr karar özetleri (2018/119 sayılı İlke Kararı bu
  alanın temel taşı).

Ne amaçla kullanacağınızı söylerseniz (dilekçe, müvekkile bilgi notu, blog yazısı)
hangi hukuki dayanakların ve hangi arama stratejisinin işinize yarayacağı
konusunda daha hedefli yardım edebilirim.
```

## Doğrulama: Araç A'nın uyardığı künye GERÇEKTEN sahte

Araç A'nın "doğrulayamadım, sahte olabilir" dediği künye
**13. HD, 2017/1118 E., 2018/342 K.** resmi kaynaktan sorgulandı
(karararama.yargitay.gov.tr, 2026-08-30):

| Sorgu | Sonuç |
|---|---|
| Esas 2017/1118 **VE** Karar 2018/342 | **0 kayıt. "Eşleşen kayıt bulunamadı."** |
| Esas 2017/1118 (tüm daireler) | 42 kayıt var |
| Esas 2017/1118 **VE** 13. Hukuk Dairesi | **1 kayıt: karar no 2017/86, tarih 12.01.2017** |

O tek kaydın konusu: **"Dava, can-hayat sigortası sözleşmesinden kaynaklanan
uyuşmazlığa ilişkindir"** - görevsizlik kararı, dosya 17. Hukuk Dairesine
gönderilmiş. Ticari elektronik iletiyle **hiçbir ilgisi yok.**

Yani dolaşımdaki künye:

- Esas numarası **gerçek** (13. HD'nin 2017/1118 esası var)
- Karar numarası **tutmuyor** (gerçeği 2017/86, iddia 2018/342)
- Konu **tamamen başka** (sigorta uyuşmazlığı, izinsiz SMS değil)

**Bu, kitabın açılış sahnesinin birebir kendisi:** numara doğru görünüyor,
içeriği o değil.

Not: Araç A'nın "bir avukatlık bürosu blogunda geçiyor" ifadesi bağımsız olarak
doğrulanamadı; iki ayrı web aramasında o künye hiçbir sayfada bulunamadı. Kitapta
bu ayrım korunur: **künyenin sahte olduğu ölçüldü, nerede yayımlandığı ölçülmedi.**

## Üç aracın üç ayrı duruşu (aynı soru, aynı gün)

| | Ne yaptı | Verdiği künyeler | Sonuç |
|---|---|---|---|
| **Araç A** | Aradı, sonra **reddetti** | Yok. Bir künyeyi "sahte olabilir" diye uyardı | Uyarısı **doğru çıktı** ama kullanıcı elinde cevapsız kaldı |
| **Araç B** | Aradı, cevap verdi | 3 + 4 künye | Hepsi **gerçek** |
| **Araç C** | Aradı, cevap verdi | 3 künye | Hepsi **gerçek** |

Araç A'nın gerekçesi ("bu uyuşmazlıklar çoğunlukla Yargıtay'a ulaşmıyor")
kısmen doğru ama sonucu yanlıştı: Araç B ve C'nin bulduğu gerçek kararlar
resmi veritabanında zaten duruyordu. Araç A onları bulamadı ve bulamadığını
"yok" diye değil, **"benim teyit edemediğim"** diye söyledi. Aradaki fark
kitabın 8. bölümünün konusu.
