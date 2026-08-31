# ÖLÇÜM-11 · Tablo toplamı · Araç B

- **Tarih:** 2026-08-30 · Araç B, oturum açılmadan, varsayılan model
- **Cetvel çıktı alınmadan önce yazıldı:** `DOGRU-CEVAP.md`
- **Sonuç:** **DOĞRU.** Sapma sıfır.

## Yöntem

18 kalemlik, ondalıklı, rastgele üretilmiş bir gider tablosu. Toplam yerel
bilgisayarda Python ile hesaplandı ve **soru sorulmadan önce** kaydedildi.

**Doğru toplam: 776.827,80 TL**

## İstem

```
Aşağıdaki gider tablosunun toplamını hesapla. Sadece toplamı yaz.
[18 satırlık tablo]
```

## Ham çıktı

```
776.827,80 TL
```

## Değerlendirme

| Ölçüt | Sonuç |
|---|---|
| Toplam doğru mu | **Evet, birebir** |
| Sapma | **0,00 TL** |

9\. bölümün "hesap yaptırma: düşük güvenilirlik" satırı bu ölçümde
**doğrulanmadı.**

Muhtemel sebep, arayüzün cevabın altında gösterdiği ipucunda: veri analizi için
oturum açma önerisi çıktı, yani araç bu tür işleri bir hesap aracına
devrediyor olabilir (9. bölümde anlatılan davranış). Ama **bunu kullanıcı
göremiyor** ve ölçüm bunu doğrulayamaz.

## Kitaba giren düzeltme

Eski satır: "Hesap yaptırma - düşük güvenilirlik - işlemi değil görüntüsünü
üretir."

Yeni satır: bu ölçümde 18 ondalıklı sayının toplamı **hatasız** çıktı. Kural
"hesaplatma" değil, **"hesabı görmeden kullanma"** olmalı: ara adımları
isteyip kontrol etmek hala doğru davranış, çünkü aracın hesap makinesi
kullanıp kullanmadığını arayüzden göremiyorsunuz.

## Sınır

Tek tablo, tek koşu, tek araç. Tablo düz metin olarak verildi, **fotoğraf
olarak değil.** Görselden sayı okuma ayrı bir ölçümdür ve yapılmadı.
