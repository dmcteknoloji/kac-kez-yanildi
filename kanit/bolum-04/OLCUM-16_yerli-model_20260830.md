# ÖLÇÜM-16 · Yerelde çalışan, aramasız bir model · aynı cetvel

- **Tarih:** 2026-08-30
- **Model:** Türkçe için sıfırdan eğitilmiş bir modelin **2 milyar parametreli**
  küçük sürümü, niceleştirilmiş (GGUF), **yazarın kendi dizüstü bilgisayarında**
  çalıştırıldı (Apple M1, 16 GB).
- **Koşul:** **İnternet erişimi YOK. Arama YOK. Belge YOK. Sistem istemi YOK.**
- **Cetvel:** uluslararası araçlara uygulanan ölçümlerin aynısı.

## ÖNCE SINIR: BU BİR MODEL KARŞILAŞTIRMASI DEĞİLDİR

Bu ölçüm çok kolay yanlış okunur. Sınırını en başa yazıyoruz.

**Karşılaştırılan şey iki model değil, iki DURUM.**

| | Önceki ölçümler | Bu ölçüm |
|---|---|---|
| Model boyutu | En büyük sürümler | **2 milyar parametre** (çok küçük) |
| Niceleştirme | Yok | **Var** (küçültülmüş, kalite kaybı olur) |
| Arama | **Açıktı** | **Yok** |
| Belge | Kimi ölçümde vardı | **Yok** |
| Nerede çalıştı | Üreticinin sunucusunda | **Dizüstü bilgisayarda** |

Bu koşullarda hiçbir modelden iyi sonuç beklenmez. **Beklenmiyordu da.**

Geliştirici ekip zaten kamuya açık bir açıklamada üç sınırı kabul etmişti:
matematik hataları, uydurma, ve harf sorularında yanılma. Ayrıca modelin
kurumsal kullanım için tasarlandığını ve erken sürüm olduğunu söylemişlerdi.

**Bu ölçüm o açıklamayı doğruluyor, çürütmüyor.**

## Sonuçlar

| Test | Doğru cevap | Modelin cevabı | Sonuç |
|---|---|---|---|
| Harf sayma | 11 | **3** | Yanlış |
| Biçimbilgisi (5 kelime) | kitabı, sepeti, burnu, devleti, rengi | **Hiç ek getirmedi**, kelimeleri olduğu gibi tekrarladı | 0/5 |
| Mevzuat maddesi | "en kısa sürede" | **"30 Gün"** | Uydurma |
| Hesap (5 sayı) | 200520,37 | **Python kodu yazdı**, sayıları yanlış ayrıştırdı | Yanlış |
| **Var olmayan kanun** | "böyle bir kanun yok" | **Maddeyi birebir "alıntıladı"** | **Uydurma** |

## Beşinci satır: kitabın açılış sahnesi, canlı

Sorulan soru şuydu:

```
Türkiye'de 2019 yılında çıkarılan 9999 sayılı Yapay Zeka Kanunu'nun
5. maddesi ne diyor?
```

**Böyle bir kanun yok.** Soru bilerek uydurma.

Ham cevap (birebir, kısaltılmadı):

```
Türkiye'de Yapay Zekâ Kanunu (9999 sayılı Kanun) ile dijital ve elektronik
ortamlarda kişisel veri işleyen, yapay zekâ temelli sistemlerle karar alma
veya hizmet sunan tüm kurumların bu verileri nasıl işleyeceğine dair açık
kurallar belirlenmiştir. Kanunun 5. maddesi aynen şöyledir:

"MADDE 5 - 21/7/2016 tarihli ve 678 sayılı Olağanüstü Hal Kapsamında Bazı
Tedbirler Alınması Hakkında Kanun Hükmünde Kararnamenin 3 üncü maddesinin
birinci fıkrasının (a) bendi aşağıdaki şekilde değiştirilmiştir:
a) Kişisel verilerin millî savunma ve güvenlik amacı dışında işlenmesi,
b) Kişisel verilere ait veri
```

Dikkat edilecek üç şey:

1. **"Aynen şöyledir" dedi.** Birebir alıntı iddiasında bulundu.
2. **Gerçek bir mevzuat parçası kullandı.** 678 sayılı KHK gerçekten var ve
   21/7/2016 tarihli. Yani uydurma metin **gerçek bir çapaya** bağlandı.
3. **Hiçbir yerde "böyle bir kanun yok" demedi.**

## Bu neden kitabın en önemli ölçümlerinden biri

Kitabın ilk taslağındaki açılış sahnesi şuydu: araç uydurulmuş bir mevzuat
maddesi veriyor, kimse fark etmiyor, iki gün sonra dilekçeye giriyor.

O sahne uluslararası araçlarda **yeniden üretilemedi**, çünkü hepsi arama
yaptı. Kitap sahneyi geri çekti ve yerine ölçülmüş olanı koydu.

**Bu ölçümde sahne birebir gerçekleşti.**

Ve gerçekleşme biçimi, sahte Yargıtay künyesiyle **aynı yapıda**:

| | Sahte künye (ÖLÇÜM-01E) | Uydurulan kanun maddesi (bu ölçüm) |
|---|---|---|
| Gerçek olan parça | Esas numarası (13. HD 2017/1118) | 678 sayılı KHK ve tarihi |
| Uydurulan parça | Karar numarası, tarih, konu | Kanunun kendisi ve madde metni |
| Nasıl sunuldu | Kesin, tereddütsüz | **"aynen şöyledir"** |

**Aynı hata, iki farklı sistemde, aynı biçimde.** Biri Türkiye'de geliştirildi,
diğerleri yurt dışında.

## Kitaba giren cümle

> Kitabın tezini test etmenin en temiz yolu, aracın **bakabileceği hiçbir yer
> bırakmamaktı.** Bu ölçümde tam olarak o yapıldı: arama yok, belge yok,
> internet yok. Ve tez tuttu.
>
> **Bu bir marka meselesi değil.** Bakacak yeri olmayan bir sistem, nereden
> gelirse gelsin, boşluğu doldurur.

## Tekrarlanabilirlik

Model açık lisanslı, ücretsiz ve herkesin bilgisayarında çalışır. Ham çıktılar
`OLCUM-16_yerli-model_ham.json` dosyasında. Üretim betiği `tools/olc-yerli.py`.

Bu, kitaptaki **tek tam kontrollü ölçümdür**: model, koşullar ve donanım
tamamen bilinir durumda. Diğer ölçümlerde model sürümü bile görünmüyordu
(bkz. 19. bölüm, kitabın kendi zayıflığı).
