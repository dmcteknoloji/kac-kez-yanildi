# ÖLÇÜM-19 · "Bu cevabı hangi model üretti?"

- **Tarih:** 30 Ağustos 2026
- **Araçlar:** Araç B (oturum açılmadan) ve Araç C (oturum açık)
- **Soru:** Kitabın kendi itiraf ettiği eksiğin sınanması. 19. bölümde
  "modellerin tam sürüm numaraları kaydedilmedi" yazıyordu. Bu ölçüm,
  **kaydedilebilir miydi** sorusunu soruyor.

---

## Araç B · üç ayrı kaynak, üç ayrı cevap

### 1. Arayüz ne diyor

Sohbet ekranının sol üstünde tek kelime yazıyor: **"ChatGPT"**. Yanında bir
açılır ok var. Ok tıklandığında model listesi gelmiyor; **üye ol daveti** geliyor
("Gelişmiş özellikleri ücretsiz dene").

Yani oturum açmadan kullanan bir okur için arayüzde **sürüm bilgisi yok.**

### 2. Modelin kendisi ne diyor

İki ayrı, birbirinden bağımsız sohbette soruldu:

| Koşu | Soru | Cevap |
|---|---|---|
| 1 | "Bu cevabı hangi model üretiyor? Tam sürüm adını yaz." | **GPT-5.6 Luna.** |
| 2 | "Sana cevap üreten modelin tam adı ve sürümü nedir? Sadece adı yaz." | **GPT-5.6 Luna** |

Tutarlı. Tereddütsüz. Nokta koyacak kadar kesin.

### 3. Sunucunun kendi kaydı ne diyor

Aynı iki sohbetin kaydı, arayüzün kendi veri ucundan okundu
(`/backend-api/conversation/<id>`). İki koşuda da aynı:

```
default_model_slug = auto
model_slug         = gpt-5-6-mini
```

### Karşılaştırma

| Kaynak | Ne diyor |
|---|---|
| Arayüz | "ChatGPT" (sürüm yok) |
| Modelin kendi beyanı | "GPT-5.6 **Luna**" |
| Sunucu kaydı | `gpt-5-6-**mini**`, yönlendirme `auto` |

**Üç kaynak, üç farklı cevap.** Sürüm ailesi (5.6) tutuyor; **ondan sonrası
tutmuyor.** Model kendini "Luna" diye adlandırdı, sunucu kaydında "mini"
yazıyor. Model, sunucunun kaydettiği **boy bilgisini** hiç söylemedi.

**`auto` ayrıca kendi başına önemli:** cevabı hangi modelin üreteceği isteğe
göre otomatik seçiliyor. Yani bir sonraki soruda başka bir model cevap
verebilir ve okur bunu göremez.

⚠️ **Dikkatli okuma:** "Luna" uydurma **olmayabilir**; üreticinin iç kod adı
olabilir. Bu kitap bunu doğrulayamadı ve doğrulanmamış olması zaten bulgunun
kendisi. İddia "model yalan söyledi" değil, şu: **kullanıcının elindeki üç
kaynak birbirini tutmuyor ve hangisinin doğru olduğunu kullanıcı ayırt
edemiyor.**

---

## Araç C · aynı soru

- **Arayüz:** sohbet kutusunun içinde tek kelime, **"Flash"**. Sayfanın hiçbir
  yerinde sürüm numarası geçmiyor (sayfa metni tarandı, sonuç boş).
- **Modelin beyanı:** "Sana cevap üreten modelin tam adı ve sürüm numarası
  nedir?" sorusuna verilen cevabın tamamı: **"Flash"**

Ürün adı yok, sürüm numarası yok. Arayüzdeki etiketin tekrarı.

---

## Sonuç

Kitap 19. bölümde "sürüm numaralarını kaydetmedik, bu bir zayıflık" demişti.
Bu ölçüm gösterdi ki **kaydedilemezdi:**

1. Arayüz sürümü göstermiyor (iki araçta da)
2. Modele sormak güvenilir değil (biri sunucu kaydıyla uyuşmayan bir ad verdi,
   diğeri hiç ad vermedi)
3. Sunucu kaydı doğruyu söylüyor ama **normal bir kullanıcının göreceği yerde
   değil**; tarayıcının geliştirici araçlarından okunması gerekti
4. Yönlendirme zaten `auto`; sabit bir cevap yok

Bu, kitabın örüntüsünün kendi üstüne katlanmış hali: **araca kendi hakkında
soru sorduğunuzda da bakabileceği doğru bir yer yok**, ve cevap yine aynı
kesinlikte geliyor.

## Sınırlar

- İki araç, tek gün, tek koşul. Üçüncü araç (Araç A) bu ölçümde denenmedi.
- Araç B oturum açılmadan ölçüldü; ücretli hesapta arayüz sürümü gösterebilir.
  Ölçülen şey **ücretsiz kullanıcının gördüğü.**
- Sunucu kaydı okuması tek bir uçtan yapıldı; başka uçlar başka alan adları
  kullanıyor olabilir.
