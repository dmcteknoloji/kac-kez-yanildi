# ÖLÇÜM-14 · Taşma noktası: kural kaçıncı mesajda düşüyor · Araç B

- **Tarih:** 2026-08-30 · Araç B, oturum açılmadan, varsayılan model
- **Sonuç:** Kural **3. turda hâlâ vardı (67.433 karakter), 4. turda düştü
  (94.349 karakter)** ve bir daha geri gelmedi.

Bu, 7. bölümün en uzun süredir açık olan ölçüm borcuydu ve kitabın okura
verebileceği en pratik sayılardan biri.

## Yöntem

Sohbetin **en başında** akılda kalır ve alakasız bir kural konuldu:

```
KURAL: Bundan sonraki her cevabının en sonuna ayrı bir satır olarak sadece
şunu yaz: MAVİ

Bu kuralı anladıysan 'anladım' de.
```

Araç "anladım" ve altına "MAVİ" yazdı. Kural aktif.

Sonra sohbet, tekrarlayan bir dolgu metniyle uzatıldı. Her turda dolgu
yapıştırıldı ve tek cümlelik özet istendi. Her turdan sonra cevabın sonunda
**MAVİ olup olmadığı** kontrol edildi.

## Sonuçlar

| Tur | Sohbetteki toplam karakter | Yaklaşık belirteç | Kural duruyor mu |
|---|---|---|---|
| 1 | 13.601 | ~3.500 | **Evet** |
| 2 | 40.517 | ~10.500 | **Evet** |
| 3 | 67.433 | ~17.500 | **Evet** |
| 4 | **94.349** | **~24.500** | **HAYIR** |

Dördüncü turdan sonra kısa ve basit bir soru soruldu
("Türkiye'nin başkenti neresi? Tek kelime yaz."). Cevap: "Ankara". **MAVİ yok.**

Yani kural tek seferlik atlanmadı; **kalıcı olarak düştü.**

## Ham çıktı (son iki tur)

```
[4. tur, 94.349 karakter]
Kurumsal arşiv yönetimi; belgelerin sınıflandırılması, uygun sürelerle
saklanması ve imhasının kayda alınması, yıllık planların güncellenmesi,
değişmeyen kodlarla dosyalanması ve devir teslimlerin tutanakla
belgelenmesini kapsar.

[MAVİ YOK]

[teyit sorusu]
Ankara

[MAVİ YOK]
```

## Kitaba giren sayı

> Bu ölçümde, sohbetin başına konan bir kural yaklaşık **67 bin karakterlik**
> (kabaca 17-18 bin belirteç, yani orta uzunlukta bir kitap bölümü kadar)
> bir konuşmadan sonra hâlâ ayaktaydı. **94 bin karakterde düştü ve geri
> gelmedi.**

Okur için pratik karşılığı:

- Uzun bir çalışma oturumunda, başta koyduğunuz kural **bir noktadan sonra
  yok oluyor** ve araç bunu size söylemiyor.
- Düşme anı bir uyarıyla gelmiyor. Cevaplar aynı düzgünlükte devam ediyor.
  Sadece kuralınız yok.
- Bu yüzden 7. bölümdeki birinci kural geçerli: **kritik kısıtları her önemli
  istekte yeniden yazın.**

## Sınır (ölçümün ne olmadığı)

- **Tek araç, tek koşu, tek dolgu tipi.** Sayı araca ve kullanılan metne göre
  değişir. Bu bir "sabit" değil, bir **büyüklük mertebesi**dir.
- **Oturum açılmadan** ölçüldü. Oturum açık hesaplarda sistem istemi ve hafıza
  defteri de masada yer kaplar; sınır **daha erken** gelebilir.
- Belirteç sayıları dolgu metninin karakter/belirteç oranından **tahmin
  edildi**, doğrudan sayılmadı. Karakter sayıları kesindir.
- Düşmenin sebebi bağlam taşması **olabilir**, ama arayüzün kendi kısaltma
  davranışı da olabilir. Dışarıdan ayırt edilemez ve kitap bunu iddia etmiyor.
  Ölçülen şey **davranıştır**, sebebi değil.

## Okur bunu kendisi yapabilir

Bu ölçüm bilinçli olarak **herkesin tekrarlayabileceği** kadar basit tutuldu:
bir kural koy, sohbeti uzat, kuralın ne zaman düştüğünü say. 7. bölümdeki
20 dakikalık uygulamanın birinci adımı tam olarak budur.
