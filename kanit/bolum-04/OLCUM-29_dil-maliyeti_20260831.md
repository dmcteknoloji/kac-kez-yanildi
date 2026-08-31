# ÖLÇÜM-29 · Dil başına belirteç maliyeti

- **Tarih:** 31 Ağustos 2026
- **Ortam:** tamamen yerelde, **hiçbir model çalıştırılmadan.** Yalnızca iki
  belirteçleyici karşılaştırıldı: İngilizce merkezli yaygın bir belirteçleyici
  ve Türkçe için sıfırdan eğitilmiş açık lisanslı bir belirteçleyici.
- **Betik:** `tools/olc-istatistik.py` · **Ham:** `OLCUM-29_dil-maliyeti.json`
- **Metin:** İnsan Hakları Evrensel Beyannamesi'nin 1. maddesi, altı dilde.
  Kamuya açık, resmi çevirileri var, ve **altı dilde aynı anlamı taşıyor.**

## Birinci ölçüm: aynı cümle, altı dil

İngilizce merkezli belirteçleyiciyle:

| Dil | Belirteç | İngilizceye oran | Karakter |
|---|---|---|---|
| İngilizce | 33 | 1,00 | 170 |
| İspanyolca | 38 | 1,15 | 171 |
| Almanca | 39 | 1,18 | 165 |
| Fransızca | 41 | 1,24 | 186 |
| **Türkçe** | **46** | **1,39** | 160 |
| **İtalyanca** | **51** | **1,55** | 178 |

**Beklenmedik sonuç: Türkçe listenin en pahalısı değil.** İtalyanca daha
pahalı çıktı, üstelik İtalyanca eklemeli bir dil de değil.

Bu, kitabın 4. bölümündeki maliyet anlatımını genişletiyor: Türkçenin pahalı
olması **Türkçeye özgü bir cezа değil.** İngilizce dışındaki dillerin hepsi
bir bedel ödüyor; Türkçe o kümenin ortasında.

⚠️ Tek cümle. Farklı metinlerde sıra değişebilir. İddia "Türkçe İtalyancadan
ucuzdur" değil; iddia şu: **Türkçe, İngilizce dışı diller arasında istisna
değil.**

## İkinci ölçüm: eklerin bedeli

Aynı kökten büyüyen bir kelime zinciri, iki belirteçleyicide:

| Kelime | İng. merkezli | Türkçe |
|---|---|---|
| ev | 1 | 2 |
| evler | 2 | 2 |
| evlerim | 3 | 3 |
| evlerimiz | 3 | 3 |
| evlerimizde | 4 | 4 |
| evlerimizdeki | 5 | 4 |
| evlerimizdekiler | 5 | 5 |
| evlerimizdekilerden | 6 | 6 |

İki belirteçleyici neredeyse **aynı.** Yani Türkçenin maliyeti, sanılanın
aksine **eklerden gelmiyor.** Uzun ekli kelimeler her iki tarafta da benzer
sayıda parçaya bölünüyor.

## Üçüncü ölçüm: Türkçe harfleri doğru yazmanın bedeli

Aynı cümle, iki biçimde:

| Yazım | İng. merkezli | **Türkçe belirteçleyici** |
|---|---|---|
| "Görüşürüz, çok teşekkür ederim. Işığı söndürmeyi unutma." | 21 | **13** |
| "Gorusuruz, cok tesekkur ederim. Isigi sondurmeyi unutma." | 20 | **20** |

**Bu tablo yaygın bir alışkanlığı tersine çeviriyor.**

Türkçe karakterleri atmak (ş yerine s, ğ yerine g yazmak) İngilizce merkezli
belirteçleyicide neredeyse hiçbir şey kazandırmıyor: 21'den 20'ye, yani
**%5.**

Ama Türkçe belirteçleyicide **tam tersi oluyor:** doğru yazılmış cümle 13
parça, harfleri atılmış cümle **20 parça.** Yani Türkçe karakterleri atmak
maliyeti **%54 artırıyor.**

Sebebi anlaşılır: Türkçe için eğitilmiş bir belirteçleyici "görüşürüz"ü tanır,
"gorusuruz"u tanımaz. Tanımadığı şeyi harf harf bölmek zorunda kalır.

> **Türkçeyi doğru yazmak pahalı değil. Türkçe için yapılmış bir araçta
> yanlış yazmak pahalı.**

Bu, kitabın 7. yanılgısının (ön sayfadaki "ş, ğ, ı kullanmadan yazmak daha
ucuza gelir" tahmini) tam karşılığıdır. O tahmin sadece tutmamakla kalmadı;
Türkçe bir araçta **tersi** çıktı.

## Sınırlar

- Belirteçleyici karşılaştırması **kalite** ölçümü değildir. Hangi modelin
  daha iyi cevap verdiği burada ölçülmedi ve ölçülemez.
- Altı dilin her biri için tek cümle kullanıldı.
- İki belirteçleyici seçildi; piyasada onlarca var ve her biri farklı sonuç
  verebilir.
