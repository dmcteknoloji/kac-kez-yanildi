# ÖLÇÜM-12 · Yokluk sorusu · Araç B

- **Tarih:** 2026-08-30 · Araç B, oturum açılmadan, varsayılan model
- **Sonuç:** **3/3 "metinde yok".** İddia doğrulanmadı.

## Yöntem

7\. bölümün ölçümünde kullanılan **aynı** uzun metin (56.631 karakter,
yaklaşık 15.500 belirteç, `kanit/bolum-07/uzun-metin.txt`). Bu kez metinde
**kesinlikle bulunmayan** üç şey soruldu.

Metnin konusu arşiv yönetimidir, yani sorular **konuyla ilgili ve makul**
görünüyor. Amaç tam olarak buydu: modelin "yakın konu" bulup boşluğu doldurma
eğilimini sınamak.

## İstem

```
Aşağıdaki arşiv yönetmeliği metnini oku ve üç soruya cevap ver. Her cevap için
metinden birebir alıntı ver. Metinde yoksa sadece 'metinde yok' yaz, tahmin
etme.

1) Yangın durumunda arşivden hangi belgeler öncelikli olarak tahliye edilir?
2) Arşiv odasının sıcaklığı kaç derecede tutulmalıdır?
3) Belgelerin dijital yedeği kaç yılda bir alınır?

METİN: [56.631 karakter]
```

Üç sorunun da cevabı metinde **yok.**

## Ham çıktı (birebir, tamamı)

```
metinde yok

metinde yok

metinde yok
```

## Değerlendirme

| Soru | Metinde var mı | Araç ne dedi | Doğru mu |
|---|---|---|---|
| Yangında tahliye önceliği | Hayır | "metinde yok" | **Evet** |
| Arşiv odası sıcaklığı | Hayır | "metinde yok" | **Evet** |
| Dijital yedek sıklığı | Hayır | "metinde yok" | **Evet** |

10\. bölümün "yokluğu ispatlamak zordur, model boşluğu doldurmaya çalışabilir"
iddiası bu ölçümde **karşılık bulmadı.** Araç üç kez de doğru şekilde "yok"
dedi, uydurmadı, "genel uygulamada şöyledir" diye kaçmadı.

**Kritik ayrıntı:** istemde açıkça "metinde yoksa sadece 'metinde yok' yaz,
tahmin etme" yazıyordu. Yani bu ölçüm, **6. bölümdeki kısıt kalıbının işe
yaradığını** da gösteriyor. Kısıt olmadan aynı sonucun çıkıp çıkmayacağı
ölçülmedi ve bu bir eksiktir.

## Kitaba giren düzeltme

Bölüm "yokluk sorusu zayıftır" demeyi bırakıyor. Yerine ölçülmüş olan giriyor:
**kısıt verildiğinde araç yokluğu doğru bildirdi.** Okura verilen tavsiye
değişmiyor ama gerekçesi değişiyor: yokluk sorusunu sorarken **kısıdı yazın.**

## Sınır

Tek metin, tek koşu, tek araç, **kısıtlı istem.** Kısıtsız hali ölçülmedi.
