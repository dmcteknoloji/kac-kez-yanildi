# ÖLÇÜM-27 · Görselden tablo okuma

- **Tarih:** 30 Ağustos 2026 · **Araç C**, oturum açık, varsayılan model
- **Cetvel:** `kanit/tur-06/CETVEL-21-28.md` · **Görsel:** `tablo27.png`

## Borç neydi

9. bölüm "metnin ötesi" görsel okumayı anlatıyordu ama **hiç ölçülmemişti.**
ÖLÇÜM-11 aynı tabloyu **metin olarak** vermiş ve sapma sıfır çıkmıştı.

**Öngörü:** görselde okuma hatası girebilir.

## Yöntem

ÖLÇÜM-11'in **birebir aynı** 18 satırlık gider tablosu, bu kez ekran
görüntüsü olarak yüklendi. Tabloda Türkçe biçimli sayılar var (binlik ayracı
nokta, kuruş ayracı virgül), Türkçe karakterli kalem adları var.

**Doğru toplam (önceden hesaplanmış):** 776.827,80

İstem: *"Görseldeki tablodaki Tutar sütununun toplamını hesapla. Sadece toplam
sayıyı yaz."*

## Ham çıktı (birebir, cevabın tamamı)

::: cikti
Ham çıktı · Araç C · 30 Ağustos 2026

```
776.827,80 TL
```
:::

## Sonuç

**Sapma sıfır.** On sekiz satır, kuruş hassasiyetinde, Türkçe sayı biçimiyle,
görselden okundu ve doğru toplandı.

Öngörü **tutmadı.** Metin halinde doğru olan, görsel halinde de doğru çıktı.

## Bu ne anlama geliyor, ne anlama gelmiyor

**Geliyor:** temiz, dijital olarak üretilmiş bir tabloyu okumak bu araç için
çözülmüş bir iş. 9. bölümün temkinli dili buna göre düzeltildi.

**Gelmiyor:** bu tablo **kusursuz** bir tabloydu. Ekrandan üretildi, düz
duruyor, gölge yok, el yazısı yok, tarayıcı bozulması yok, sütunlar birbirine
girmiyor. Gerçek hayatta okurun eline gelen fatura fotoğrafı böyle değildir.

**Açık kalan:** eğik çekilmiş, gölgeli, buruşuk ya da elle doldurulmuş bir
belge ölçülmedi. Bir sonraki turun işi.
