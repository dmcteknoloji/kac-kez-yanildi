# Kanıt Deposu

**"Bu Kitap Kaç Kez Yanıldı?"** adlı kitabın bütün ölçümlerinin ham verisi.

Kitap, yapay zeka hakkında yaygın olarak bilinen iddiaları tek tek ölçüyor ve
şunu söylüyor: *bir cevabın doğruluğunu üslubundan anlayamazsınız, dışarıdan
bakmanız gerekir.* Aynı standardı kendisine de uygulaması gerekiyordu.

Bu depo o yüzden var. Kitaptaki her rakamın, her ham çıktının ve her
"ölçüldü" cümlesinin arkasındaki dosya burada duruyor.

---

## Ne bulacaksınız

| Klasör | İçerik |
|---|---|
| `kanit/bolum-NN/` | O bölüme ait ölçümler: sorulan istemin tam metni, aracın **kırpılmamış** cevabı, doğru cevabın ne olduğu ve nereden doğrulandığı |
| `kanit/tur-06/` | Ölçümlerden **önce** yazılmış cetveller (beklenen sonuçlar) ve toplu skor |
| `araclar/` | Ölçümleri üreten betikler. Çalıştırılabilir |
| `ARAC-ESLESMESI.md` | Kitapta "Araç A / B / C" diye geçen araçların gerçek adları |

Ölçüm klasörlerinde `.md` uzantılı dosyanın yanında bazen düz metin dosyaları
da var (`istem.txt`, `uzun-metin.txt`, `tablo.txt`, `belgeler.txt`). Bunlar
araca **birebir gönderilen girdilerdir**; ölçümü tekrarlamak isteyen kopyalayıp
yapıştırsın diye ayrı duruyorlar. `.json` dosyaları ise betiklerin ürettiği
işlenmemiş sonuçlardır.

## Ölçüm dosyaları neyi içerir

Her ölçüm dosyasında şunlar var, ve **hepsi zorunlu**:

- **Tarih ve koşullar:** hangi araç, oturum açık mıydı, arama açık mıydı,
  varsayılan model miydi
- **İstem:** sorulan sorunun birebir metni
- **Ham çıktı:** aracın cevabı, **kırpılmadan ve düzeltilmeden**
- **Doğrusu:** cevabın doğru olup olmadığı ve bunun **hangi resmi kayıttan**
  kontrol edildiği
- **Sınırlar:** ölçümün neyi kanıtlamadığı

Son madde en önemlisi. Kitabın kuralı şu: bir ölçümün neyi kanıtlamadığını
söylemeyen kişi, ölçümü değil kanaatini yayımlamış olur.

## Cetveller neden önemli

`kanit/tur-06/CETVEL-21-28.md` ve `kanit/bolum-19/CETVEL-ongoruler.md`
dosyaları, ilgili ölçümler **yapılmadan önce** yazıldı ve beklenen sonucu
ilan ediyor.

Sebebi: elinizde yeterince sonuç varsa, birbirini tutan bir açıklama her
zaman bulunabilir. Beklentiyi önceden yazmak, sonradan hikaye kurmayı
engelliyor. Bu cetvellerde ilan edilmiş beklentilerin **bir kısmı tutmadı** ve
tutmayanlar da kitapta basıldı.

---

## Kitabın kendi karnesi

Ölçümlerde araçların ürettiği, doğruluğu bağımsız olarak kontrol
edilebilen 133 birim (bir künye, bir toplam, bir tarih, bir dize) tek tek
sayıldı:

| Aracın durumu | Birim | Doğru | İsabet |
|---|---|---|---|
| Bakabileceği doğru bir yer **vardı** | 114 | 111 | **%97,4** |
| Bakabileceği yer **yoktu** | 19 | 7 | **%36,8** |
| Toplam | 133 | 118 | %88,7 |

Sayımı `araclar/olc-skor.py` üretiyor; satırların hangi kanıt dosyasından
geldiği betiğin içinde yazılı. **Kendiniz yeniden sayabilirsiniz** ve farklı
bir sonuç bulursanız duymak isteriz.

Dosyaların değişip değişmediğini ayrıca kontrol etmeniz gerekmiyor: git,
her dosyanın içerik özetini kendi tutuyor. `git log` ve `git show` ile hangi
dosyanın ne zaman değiştiğini görebilirsiniz.

Bu sayının sınırı da açıkça yazılmalı: "birim" ayrımını kitap yaptı, başka
bir ayrım başka bir yüzde verirdi, ve iki kümenin büyüklüğü eşit değil
(114'e karşı 19). **Farkın yönü güvenilir, ondalığı değil.**

---

## Ölçümleri kendiniz tekrarlamak

### Bilgisayarda çalışanlar

```bash
# Toplu skor (ek bağımlılık yok)
python3 araclar/olc-skor.py

# Belirteç sayımı
pip install tiktoken
python3 araclar/olc-belirtec.py

# Dil başına maliyet + Türkçe harflerin bedeli
pip install tiktoken tokenizers
VERI_DIZINI=/belirtecleyici/dosyasinin/klasoru python3 araclar/olc-istatistik.py
```

Son betik, Türkçe için eğitilmiş bir belirteçleyicinin tanım dosyasını bekler.
O dosya bu depoda **yok**, çünkü kendi lisansıyla ve kendi kaynağından
indirilmesi gerekiyor; nereden indirileceği `kanit/bolum-04/OLCUM-15_*` içinde
yazılı.

Yerelde model çalıştıran ölçümler (`olc-yerli.py`, `olc-onyargi.py`) bir
`ollama` kurulumu bekler ve `localhost:11434` adresine bağlanır.

### Sohbet arayüzünde yapılanlar

Ölçümlerin çoğu, okurun kullandığı yerde yapıldı: web sohbet arayüzünde.
Tekrarlamak için ölçüm dosyasındaki **istemi birebir kopyalayın** ve
koşulları eşitleyin (oturum açık mı, arama açık mı).

**Farklı bir cevap almanız normaldir.** Bunun neden normal olduğu kitabın
2. bölümünde anlatılıyor; aynı soru aynı araca üç kez soruldu ve üç farklı
cevap geldi (`kanit/bolum-02/OLCUM-06_*`).

---

## Bu deponun sınırları

Dürüst olmak gerekiyor, çünkü kitap başka herkesten bunu istiyor.

- **Ekran görüntüsü yok.** Ham çıktılar metin olarak kaydedildi. Bir metin
  dosyası, bir ekran görüntüsünden daha kolay değiştirilebilir. Bunu
  bilerek okuyun.
- **Model sürümleri çoğu ölçümde kayıtlı değil.** Sebebi
  `kanit/bolum-19/OLCUM-19_hangi-model_20260830.md` dosyasında ölçülerek
  anlatılıyor: arayüzler sürümü kullanıcıya göstermiyor, araca sormak da
  güvenilir çıkmadı.
- **Ölçümler 30-31 Ağustos 2026'da yapıldı.** Bu alanda araçlar haftalar
  içinde değişiyor. Bugün aynı sonucu almanız beklenmez; kitabın 19. bölümü
  zaten bunun üzerine kurulu.
- **Telifli metin yok.** Ezberleme ölçümünde (`kanit/bolum-16/`) telifli bir
  eserin metni bilinçli olarak kaydedilmedi; yalnızca kamuya açık bir metin
  kullanıldı ve aracın verdiği cevap kaydedildi.

## Hata bulursanız

Bu deponun var olma sebebi tam olarak bu. Bir hesap hatası, yanlış bir
doğrulama ya da haksız bir çıkarım bulursanız **issue açın.** Kitabın adı,
yanılmanın saklanacak bir şey olmadığı fikri üzerine kurulu.

## Lisans

Kanıt dosyaları, betikler ve belgeler **CC BY 4.0** ile paylaşılıyor: kaynak
göstererek kullanabilir, çoğaltabilir ve üzerine çalışabilirsiniz.
Türkçe özet `LISANS-OZET.md`, resmi metin `LICENSE` dosyasında.

Araçların ürettiği ham çıktıların hakları kendi üreticilerine aittir; burada
**alıntı ve inceleme amacıyla**, değiştirilmeden yer alıyorlar.
