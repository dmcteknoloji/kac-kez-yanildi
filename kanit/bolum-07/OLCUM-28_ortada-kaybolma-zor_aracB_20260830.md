# ÖLÇÜM-28 · Ortada kaybolma, benzer iğnelerle

- **Tarih:** 30 Ağustos 2026 · Araç B, oturum açılmadan
- **Cetvel:** `kanit/tur-06/CETVEL-21-28.md`

## Borç neydi

ÖLÇÜM-10'da uzun metnin başına, ortasına ve sonuna üç bilgi gizlenmiş, üçü de
bulunmuştu ve "ortada kaybolma" iddiası çürümüştü. Ama kitap kendi zayıflığını
yazmıştı: **o üç bilgi birbirinden çok farklıydı**, yani aramak kolaydı.

**Öngörü:** birbirine **benzeyen** iğnelerle karışma olmalı.

## Yöntem

700 maddelik, 51.189 karakterlik bir yönetmelik metni üretildi. İçine
**birbirinin neredeyse aynısı** üç madde kondu:

| Konum | Madde |
|---|---|
| %10 | Madde 70 - Devir teslim tutanağı **3** nüsha halinde düzenlenir. |
| **%50** | **Madde 350 - Devir teslim tutanağı 5 nüsha halinde düzenlenir.** |
| %90 | Madde 630 - Devir teslim tutanağı **7** nüsha halinde düzenlenir. |

Aynı cümle, aynı kalıp, yakın sayılar. Ayırt edici tek şey madde numarası.

## Birinci soru: ortadaki

> "Madde 350'ye göre kaç nüsha düzenlenir? Sadece sayıyı yaz."

::: cikti
Ham çıktı · Araç B · 30 Ağustos 2026 · cevabın tamamı

```
5
```
:::

**Doğru.**

## İkinci soru: üçünü ayırabiliyor mu

> "Devir teslim tutanağının nüsha sayısını belirten TÜM maddeleri madde
> numarası ve nüsha sayısıyla listele."

::: cikti
Ham çıktı · Araç B · 30 Ağustos 2026 · cevabın tamamı

```
Madde 70 — 3 nüsha
Madde 350 — 5 nüsha
Madde 630 — 7 nüsha
```
:::

**Üçü de doğru, sırasıyla, karıştırmadan.**

## Sonuç

**Öngörü tutmadı.** Kitabın kendi zayıflık notu kapandı ve iddia bu kitap için
**kesin olarak** çürüdü:

- ÖLÇÜM-10: farklı iğneler, 56.631 karakter, 3/3 bulundu
- ÖLÇÜM-28: **benzer** iğneler, 51.189 karakter, 3/3 bulundu **ve ayırt edildi**

"Uzun metnin ortasındaki bilgi kaybolur" iddiası, iki ayrı tasarımda da
doğrulanmadı.

## Ama 7. bölümün asıl bulgusu yerinde duruyor

Bu, "uzun konuşma sorunsuz" demek **değil.** Aynı bölümdeki ÖLÇÜM-14'te,
konuşmanın başına konan bir **kural** 94.349 karakterde sessizce düşmüştü.

Aradaki fark önemli:

> **Metnin içinde duran bir bilgiyi bulmak** ile **kendisine verilen bir
> kuralı akılda tutmak** aynı şey değil. Birincisi çalışıyor, ikincisi
> çalışmıyor.
>
> Birincisinde bakabileceği bir yer var: metin. İkincisinde yok.

Kitabın ana örüntüsü, aynı bölümün içinde iki kez doğrulanıyor.

## Sınırlar

- Metin, ölçüm için üretildi ve tekrarlı cümlelerden oluşuyor. Gerçek bir
  yönetmelik daha çeşitlidir; bu, aramayı kolaylaştırmış olabilir.
- Tek araç, tek koşu.
