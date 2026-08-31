# ÖLÇÜM-09 · İstem kalıpları: A ve B karşılaştırması · Araç B

- **Tarih:** 2026-08-30
- **Araç:** Araç B, web sohbet arayüzü, oturum açılmadan, varsayılan model
- **Yöntem:** Aynı toplantı notu, iki ayrı boş sohbette, iki farklı istemle
- **Cetvel çıktılar alınmadan önce yazıldı:** `DOGRU-CEVAP.md`

Bu ölçüm 6. bölümün ana iddiasını sınıyor: altı kalıpla yazılan istem daha iyi
sonuç verir mi?

## Malzeme

`toplanti-notu.txt` (10 satır, dört gerçek görev, dört tuzak). Tuzaklar:

- Sorumlusu belirsiz iki görev ("Birinin hazırlaması lazım")
- Tarihi belirsiz görevler ("bu hafta içinde")
- Bir **tahmin** ("2 milyon liraydı, bu sene daha yüksek olur herhalde")
- Açıkça **ertelenmiş** bir konu ("yeni ofis... sonraki toplantıya kalsın")
- Birbirinden ayrı iki görev (bütçe onayı ve sunum hazırlama) - **notta bunların
  aynı iş olduğu YAZMIYOR**

## Ham çıktı · İSTEM A (kalıpsız)

```
İSTEM: Bu toplantı notundan görevleri çıkar.  [+ not]

ÇIKTI:
Toplantı notundan çıkan görevler:

Mehmet: Web sitesi yenileme tedarikçisini arayıp gecikmeyi çözmek - bu hafta içinde.
Ayşe / atanması gereken kişi: Bütçe onayı için Genel Müdür'e sunulacak sunumu
hazırlamak - sorumlu ve tarih belirtilmemiş.
Zeynep: Artan müşteri şikayetlerinin nedenlerini analiz etmek - 20 Mart'a kadar.

Not: Yeni ofis konusu sonraki toplantıya bırakılmış; bu nedenle mevcut görev
listesine dahil edilmedi.
```

## Ham çıktı · İSTEM B (altı kalıpla)

```
Görev tablosu

Sorumlu   | Görev                              | Tarih          | Kaynak satır
Mehmet    | Tedarikçiyi aramak                 | bu hafta içinde| "Ben tedarikçiyi arayacağım, bu hafta içinde hallederim."
belirsiz  | Bütçe onayını Genel Müdür'e sunmak | notta yok      | "Bir de bütçe onayı lazım, Genel Müdür'e sunulacak."
belirsiz  | Sunumu hazırlamak                  | notta yok      | "Değil. Birinin hazırlaması lazım."
Zeynep    | Müşteri şikayetlerinin nedenine    | 20 Mart        | "Zeynep, sen bir analiz yapabilir misin? 20 Mart'a kadar yetişir mi?"
          | ilişkin analiz yapmak              |                |

Tabloya alınmayan cümleler

"Web sitesi yenileme işi gecikti. Tedarikçi cevap vermiyor."
Neden: Durum bilgisi veriyor; açıkça bir görev tanımlamıyor.

"Sunum hazır mı?"
Neden: Soru niteliğinde; herhangi bir görev atamıyor.

"Geçen sene 2 milyon liraydı, bu sene daha yüksek olur herhalde."
Neden: [tahmin niteliğinde]

"Bir de yeni ofis meselesi var ama o sonraki toplantıya kalsın."
Neden: Konunun sonraki toplantıya bırakıldığı açıkça belirtiliyor; mevcut
toplantı için yapılacak bir görev tanımlanmıyor.
```

## Puanlama (cetvele göre)

| Ölçüt | İstem A | İstem B |
|---|---|---|
| Dört gerçek görevden kaçı çıktı | **3** (ikisi birleştirildi) | **4** |
| Notta olmayan bağ kuruldu mu | **EVET.** Sunumun bütçe onayı için olduğunu söyledi; **notta bu yazmıyor** | Hayır, ikisi ayrı satır |
| Sahte kesinlik | **EVET.** "Ayşe / atanması gereken kişi" - Ayşe'ye yarı atama yaptı, not öyle demiyor | Hayır, "belirsiz" yazdı |
| "2 milyon" tahmini taşındı mı | Hayır | Hayır, ayrıca gerekçesiyle dışarıda bırakıldı |
| Ertelenen ofis konusu | Doğru dışarıda, gerekçeli | Doğru dışarıda, gerekçeli |
| Kaynak satırı verdi mi | **Hayır** | **Evet, her satır için** |
| Dışarıda bırakılanların dökümü | Sadece bir tanesi | **Hepsi, gerekçeli** |

## Sonuç: iddia DESTEKLENDİ, ama abartısız

**İstem B daha iyi sonuç verdi ve farkı ölçülebilir:** 4/4'e karşı 3/4 görev,
sıfıra karşı bir uydurulmuş bağ, sıfıra karşı bir sahte atama.

Ama dürüst olmak gerekiyor: **İstem A da kötü değildi.** İki tuzağın ikisini de
atladı ("2 milyon" tahmini ve ertelenmiş ofis konusu), belirsizliği de kısmen
işaretledi ("sorumlu ve tarih belirtilmemiş").

Aradaki asıl fark **görevlerin sayısı değil, çıktının denetlenebilirliği:**

- İstem A'nın çıktısını doğrulamak için notun tamamını yeniden okumanız gerekir.
- İstem B'nin çıktısında **her satırın kaynağı yazılı** ve dışarıda bırakılan
  her cümlenin gerekçesi var. Doğrulama otuz saniye sürüyor.

İstem A'nın uydurduğu bağ (sunum = bütçe sunumu) bu farkın tam örneğidir. B'de
o bağ kurulamazdı, çünkü kaynak satırı yazmak zorundaydı ve o cümle notta yoktu.

## Kitaba giren cümle

> İyi bir istem sadece daha iyi bir cevap vermez. **Cevabın nereden geldiğini
> gösterir**, ve asıl kazanç oradadır.

## Sınır

Tek araç, tek not, tek koşu. Süre ölçülmedi. "Altı kalıp her zaman daha iyidir"
genellemesi bu ölçümden çıkmaz.
