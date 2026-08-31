# ÖLÇÜM-03 · Emin ses, yanlış cevap · Araç A

- **Tarih:** 2026-08-30
- **Araç:** Araç A, web sohbet arayüzü, oturum açık, en güçlü model, "yüksek" ayar
- **Not:** Araç cevaptan önce 11 saniye "düşündü" (arayüz "Thought for 11s" yazdı)
- **Sonuç:** **Aynı cevabın içinde doğru ve yanlış yan yana**, tamamen aynı üslupla.
  Üstelik yanlış olan kısım, doğru kısımla **çelişiyor.**

Bu, 1. bölümün en önemli sayfasının kanıtıdır. Aranan şey "bir araç yanıldı"
değil, **okurun üsluptan ayırt edemeyeceği bir yanlış**tı. Bulundu.

## İstem (birebir)

```
muvaffakiyetsizleştiricileştiriveremeyebileceklerimizden kelimesinde kaç tane e
harfi var?
```

## Ham çıktı (birebir)

```
Bu kelimede 11 tane "e" harfi var.

Hecelere/eklere göre saymak kolaylaştırıyor:

muvaffakiyet -> 1
leş -> 2
leş -> 3
iver -> 4
eme -> 6
yebil -> 7
ecek -> 9
ler -> 10
den -> 11

Toplam 56 harflik kelimenin 11'i "e". (En sık geçen harf ise 14 kez tekrarlanan "i".)
```

## Doğrulama (yerelde Python, `collections.Counter`, 2026-08-30)

```
harf sayisi: 56
en sik 6 harf: [('e', 11), ('i', 10), ('l', 4), ('r', 4), ('m', 3), ('t', 3)]
```

| İddia | Gerçek | Sonuç |
|---|---|---|
| "11 tane e harfi var" | 11 | **DOĞRU** |
| "Toplam 56 harflik kelime" | 56 | **DOĞRU** |
| "En sık geçen harf 'i'" | En sık harf **'e'** (11 kez) | **YANLIŞ** |
| "'i' 14 kez tekrarlanıyor" | 'i' **10 kez** geçiyor | **YANLIŞ** |

## Neden bu sayfa kitabın en önemli sayfası

Üç şey aynı anda doğru:

1. **Cevabın asıl kısmı doğru.** Okur "demek ki sayabiliyor" diye düşünür.
2. **Yanlış kısım aynı cümlenin içinde, aynı üslupla, parantez içinde**, yani
   en az dikkat çeken yerde. Ses titremiyor, "sanırım" yok, tereddüt yok.
3. **Yanlış kısım kendi doğru kısmıyla çelişiyor.** Araç bir cümle önce "11 tane
   e" demiş; hemen ardından "en sık harf 14 kez geçen i" diyor. İkisi aynı anda
   doğru olamaz. Araç bu çelişkiyi fark etmiyor, çünkü tutarlılığı denetleyen bir
   yeri yok; **oraya yakışan cümleyi** kuruyor.

Bir insan bu iki cümleyi arka arkaya kurmaz. Kurarsa da sesinden anlarsınız.
Burada anlaşılmıyor.

## Bir de mekanizmayı gösteriyor (2. bölüme köprü)

Araç harfleri saymakta niye zorlanıyor? Çünkü kelimeyi harf harf görmüyor.
Aynı kelime gerçek bir belirteçleyiciyle (tiktoken o200k_base, yerelde
çalıştırıldı, bkz. `kanit/bolum-02/`) **20 parçaya** bölünüyor:

```
m | uv | aff | ak | iy | ets | iz | le | ştir | ic | ile | ştir | iver | em |
ey | eb | ilecek | ler | imiz | den
```

56 harf, 20 parça. Araç bu 20 parçayı görüyor, 56 harfi değil. Harf saymak
onun için, kapalı bir kutunun içindekini kutunun dışından saymak gibi.
Doğru saydığında da bunu harfleri görerek yapmıyor; **saymayı taklit ediyor.**
Çoğu zaman tutuyor, tutmadığında da aynı sesle söylüyor.
