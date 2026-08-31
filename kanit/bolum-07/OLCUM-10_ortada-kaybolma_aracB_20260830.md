# ÖLÇÜM-10 · Uzun metinde ortadaki bilgi kayboluyor mu · Araç B

- **Tarih:** 2026-08-30
- **Araç:** Araç B, web sohbet arayüzü, **oturum açılmadan**, varsayılan model
- **Amaç:** 7. bölümün "uzun metinde ortadaki bilgi daha zayıf kullanılıyor"
  iddiasını sınamak
- **Sonuç:** **İddia bu koşullarda DOĞRULANMADI.**

## Yöntem

Tekrarlayan, anlamsız ama gerçekçi bir "arşiv yönetmeliği" metni üretildi. İçine
birbirinden bağımsız **üç iğne** (kısa, benzersiz bilgi cümlesi) yerleştirildi:

| Kod | Konum | Cümle |
|---|---|---|
| BAŞ | **%2,4** | "Kırmızı klasörlerin anahtarı ikinci kattaki dolapta durur." |
| ORTA | **%49,9** | "Arşiv nem ölçer cihazının kalibrasyon numarası 47-B'dir." |
| SON | **%97,5** | "Depo girişinin yedek anahtarı güvenlik masasında Ahmet Bey'dedir." |

Sonra üçü birden soruldu ve **her cevap için birebir alıntı** istendi.

Metin `uzun-metin.txt` dosyasındadır ve tekrarlanabilir: dolgu paragrafı sabit,
tekrar sayısı sabit, iğneler sabit.

## Koşu 1: 56.631 karakter (15.555 belirteç)

**Ham çıktı (birebir):**

```
Kırmızı klasörlerin anahtarı: İkinci kattaki dolapta duruyor.
"Kırmızı klasörlerin anahtarı ikinci kattaki dolapta durur."

Arşiv nem ölçer cihazının kalibrasyon numarası: 47-B
"Arşiv nem ölçer cihazının kalibrasyon numarası 47-B'dir."

Depo girişinin yedek anahtarı: Güvenlik masasında Ahmet Bey'de.
"Depo girişinin yedek anahtarı güvenlik masasında Ahmet Bey'dedir."
```

| İğne | Bulundu mu | Alıntı doğru mu |
|---|---|---|
| BAŞ (%2,4) | **Evet** | Birebir |
| ORTA (%49,9) | **Evet** | Birebir |
| SON (%97,5) | **Evet** | Birebir |

**3/3. Ortadaki iğne de bulundu.**

## Koşu 2: 226.871 karakter (yaklaşık 62.000 belirteç)

Aynı yapı, dolgu dört katına çıkarıldı. Sonuç:

```
Bağlanılamıyor · Yeniden dene
```

Mesaj gönderildi ama **işlenemedi.** İki denemede de aynı sonuç.

Bu bir model hatası değil, **arayüz sınırı**. Ama okur açısından farkı yok:
aracın reklam edilen bağlam penceresi ne olursa olsun, oturum açmadan kullanılan
arayüzde bu boyutta bir metin işlenemedi.

## Değerlendirme: iddia geri çekiliyor

7\. bölümün "uzun metinde ortadaki kısımlar daha zayıf kullanılıyor" iddiası,
bu ölçümde **karşılık bulmadı.** 15.555 belirteçlik bir metinde ortadaki bilgi,
baştaki ve sondaki kadar temiz biçimde bulundu ve birebir alıntılandı.

Dürüst değerlendirme üç maddede:

1. **15.555 belirteç, bugünün araçları için uzun bir metin değil.** Bu olgunun
   gözlendiği çalışmalar çok daha uzun metinlerle ve çok daha fazla dikkat
   dağıtıcıyla yapılıyor. Yani ölçüm iddiayı çürütmüyor, **bu uzunlukta
   gözlenmediğini** gösteriyor.
2. **Üç iğne birbirinden çok farklıydı.** Gerçek belgelerde benzer bilgiler
   birbirine karışır; bu deney o zorluğu içermiyor.
3. **Daha uzun koşu yapılamadı**, çünkü arayüz mesajı işleyemedi.

## Kitaba giren cümle (düzeltilmiş)

Eski cümle: "uzun metinde ortadaki kısımlar daha zayıf kullanılıyor."

Yeni cümle:

> Bu kitap bunu ölçmeye çalıştı ve **15.500 belirteçlik bir metinde fark
> bulamadı**: baştaki, ortadaki ve sondaki bilgi aynı şekilde bulundu.
> Daha uzun bir metinle denendiğinde ise araç mesajı hiç işleyemedi.
> Yani sizin için pratik sınır, reklam edilen bağlam penceresi değil,
> **arayüzün gerçekte kabul ettiği boyut.**

## Sınır

Tek araç, tek metin, tek koşu, tek uzunluk. Üç iğne birbirinden çok farklıydı.
Bu ölçüm "ortada kaybolma diye bir şey yoktur" demiyor; **bu koşullarda
gözlenmedi** diyor.
