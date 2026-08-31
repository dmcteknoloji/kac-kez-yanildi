# ÖLÇÜM-15 · Türkçe için eğitilmiş belirteçleyici ne kadar fark ediyor

- **Tarih:** 2026-08-30
- **Yöntem:** İki belirteçleyici de **yerel bilgisayarda** çalıştırıldı.
  Model çalıştırılmadı, sadece metnin kaç parçaya bölündüğü sayıldı.
- **Karşılaştırılanlar:**
  - İngilizce merkezli, yaygın kullanılan açık kaynak belirteçleyici
    (tiktoken o200k_base)
  - Türkçe için sıfırdan eğitilmiş bir modelin belirteçleyicisi
    (Kumru-2B, VNGRS, Apache 2.0, Hugging Face'ten indirildi)

## Sonuç

| Metin | İngilizce merkezli | Türkçe | Fazlası |
|---|---|---|---|
| İnsan Hakları Evrensel Beyannamesi, 1. madde | 46 | 31 | **+%48** |
| Gündelik cümle: toplantı | 25 | 17 | **+%47** |
| Gündelik cümle: fatura | 26 | 19 | **+%37** |
| Mevzuat cümlesi (6698 m.12/5) | 43 | 26 | **+%65** |
| **Toplam** | **140** | **93** | **+%51** |

Tek kelimelerde:

```
görüşebileceğimizi                                       7 parça  ->  4 parça
muvaffakiyetsizleştiricileştiriveremeyebileceklerimizden 20 parça -> 13 parça
```

## Bağımsız doğrulama

Modelin geliştiricisi kendi belge sayfasında şunu yazıyor: diğer açık kaynak
modeller, aynı Türkçe metin için Kumru'dan **%38 ile %98 arasında daha fazla
belirteç harcıyor.**

Bu kitabın ölçtüğü aralık cümle bazında **%37 ile %65**, toplamda **%51**.
Yani geliştiricinin belirttiği aralığın **içinde** ve alt yarısında.

İki taraf birbirini tutuyor: biri ürünün geliştiricisi, diğeri bu kitap.

## ÖLÇÜM-04 ile ilişkisi

ÖLÇÜM-04'te aynı metinlerin Türkçesi ile İngilizcesi karşılaştırılmış ve
Türkçenin **1,37 kat** (yani %37 fazla) belirteç tükettiği bulunmuştu.
O ölçüm dilin maliyetini gösteriyordu.

Bu ölçüm o maliyetin **nereden geldiğini** gösteriyor: dilin kendisinden
değil, **belirteçleyicinin hangi dile göre ayarlandığından.** Türkçeye göre
ayarlanmış bir belirteçleyicide aynı metin yarı yarıya azalıyor.

## Bu ölçüm neyi GÖSTERMEZ

Bu ayrımı yazmak zorundayız, çünkü kolayca yanlış okunur:

- **Bu bir model karşılaştırması değildir.** Hiçbir model çalıştırılmadı.
  Cevap kalitesi, doğruluk, uydurma oranı **ölçülmedi.**
- **"Türkçe model daha iyidir" demiyor.** Sadece "Türkçe için ayarlanmış bir
  belirteçleyici, Türkçe metni daha az parçaya böler" diyor.
- **Bir ürün tavsiyesi değildir.** Belirteçleyici, ölçülebilir ve açık kaynak
  olduğu için seçildi; aynı ölçümü herhangi bir okur tekrarlayabilir.
- **Az belirteç, az maliyet demektir; doğru cevap demek değildir.**

## Üretim

`tools/olc-kumru.py`. Tek komutla tekrarlanır. Belirteçleyici dosyası
Hugging Face'ten açık lisansla indirilir.
