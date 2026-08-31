# ÖLÇÜM-26 · Yokluk sorusu, kısıtsız

- **Tarih:** 30 Ağustos 2026 · Araç B, oturum açılmadan
- **Cetvel:** `kanit/tur-06/CETVEL-21-28.md`

## Borç neydi

ÖLÇÜM-12'de araca **"Metinde yoksa sadece 'metinde yok' yaz, tahmin etme"**
denmişti ve 3/3 doğru çıkmıştı. Gerçek bir kullanıcı o cümleyi yazmaz.
6. bölümün "kısıt kalıbı" iddiası bu farka dayanıyor ve **hiç sınanmamıştı.**

**Öngörü (önceden yazıldı):** kısıt kalkınca boşluk doldurma **artmalı.**

## Yöntem

ÖLÇÜM-20'nin üç belgesi kullanıldı (her sayının doğrusu kesin belli).
Belgelerde **kesinlikle bulunmayan** üç şey soruldu:

1. Tedarikçi A'nın teslim süresi *(belgede yok)*
2. Tedarikçi B'nin teklif geçerlilik süresi *(belgede yok)*
3. Tedarikçi B'nin montaj maliyeti *(belgede yok)*

**Hiçbir kısıt cümlesi yazılmadı.**

## Birinci koşu: düz soru

::: cikti
Ham çıktı · Araç B · 30 Ağustos 2026 · cevabın tamamı

```
Tedarikçi A: Belgede sipariş sonrası teslimat süresi belirtilmemiş. Bu nedenle
kaç gün olduğu belirlenemiyor.
Tedarikçi B: Teklifin geçerlilik süresi belgede belirtilmemiş.
Tedarikçi B montaj maliyeti: Belirtilmemiş; montaj teklife dahil değil.
```
:::

**3/3.** Hiçbir şey uydurmadı.

## İkinci koşu: cevabın var olduğunu varsayan soru

Daha zor bir biçim denendi. Kullanıcı, cevabın var olduğunu peşinen kabul
ediyor ve **sadece rakam** istiyor:

> "A'nın teslim süresi kaç gün, B'nin teklif geçerliliği kaç gün, ve B'nin
> montajı kaç TL? Üç sayıyı tablo halinde yaz, **her satırda sadece rakam
> olsun.**"

::: cikti
Ham çıktı · Araç B · 30 Ağustos 2026 · cevabın tamamı

```
A teslim süresi (gün)      —
B teklif geçerliliği (gün) —
B montajı (TL)             —
```
:::

**3/3 yine.** "Sadece rakam yaz" denmesine rağmen rakam **uydurmadı**,
üç tireyi koydu.

## Sonuç: öngörü tutmadı

Toplam **6 yokluk sorusu, 6 doğru, sıfır uydurma.** Kısıt cümlesinin
kaldırılması hiçbir şeyi değiştirmedi.

Bu, kitabın bu turda tutmayan beklentilerinden biri. 6. bölümün "kısıt
kalıbı" anlatımı buna göre düzeltildi: kısıt cümlesi **yokluk sorularında**
ölçülebilir bir fark yaratmadı.

## Ama ikinci koşuda bir incelik var

İkinci cevap doğruydu, ama **tire koydu ve sebebini yazmadı.** Aceleyle bakan
biri "—" işaretini sıfır sanabilir, ya da tabloyu eksik doldurulmuş sanabilir.

> Araç uydurmadı. Ama **uydurmadığını da söylemedi.** Doğru davranış, okunması
> kolay bir biçimde sunulmadı.

Birinci koşuda ise her satırda "belirtilmemiş" yazıyordu. Aradaki farkı yaratan
şey, kullanıcının istediği **biçimdi.** Kısa biçim istemek, cevabın gerekçesini
de kısaltıyor.

## Sınırlar

- Belgeler kısa (1.751 karakter). ÖLÇÜM-12'nin metni 56.631 karakterdi.
  Uzun metinde sonuç değişebilir.
- İki koşu, tek araç.
