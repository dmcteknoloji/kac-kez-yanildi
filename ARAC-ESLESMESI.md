# Araç eşleşmesi (kitapta anonim, burada açık)

Kitabın 3. değişmez kuralı: **araç adı ve ekran görüntüsü sayfalara girmez**,
çünkü altı ayda eskir. Ama ölçümün izlenebilir olması şart. Çözüm: kitapta
"Araç A / B / C", gerçek adlar burada ve kanıt deposunda.

| Kitaptaki ad | Gerçek araç | Nasıl ölçüldü | Sürüm (ne biliniyor) |
|---|---|---|---|
| Araç A | Claude (Anthropic) | claude.ai, oturum açık, en güçlü model + "yüksek" düşünme ayarı, 2026-08-30 | Arayüzde model adı görünür; **tam sürüm kaydedilmedi** |
| Araç B | ChatGPT (OpenAI) | chatgpt.com, **oturum açılmadan**, varsayılan model, 2026-08-30 | Arayüz sürüm göstermiyor. Kendi beyanı **"GPT-5.6 Luna"**; sunucu kaydı **`gpt-5-6-mini`**, yönlendirme `auto` (ÖLÇÜM-19) |
| Araç C | Gemini (Google) | gemini.google.com, oturum açık, varsayılan "Flash" model, 2026-08-30 | Arayüzde ve kendi beyanında sadece **"Flash"**; sürüm numarası hiçbir yerde yok (ÖLÇÜM-19) |

Not: en az üç üretici kuralı (kitap tek markanın reklamına dönmesin diye,
bkz. `06-ACIK-SORULAR.md`) sağlandı.

⚠️ **ÖLÇÜM-19 bu tablonun sağ sütununu bir bulguya çevirdi.** Sürüm
numaralarının kaydedilmemiş olması kitabın dikkatsizliği değil: iki araçta da
arayüz sürümü kullanıcıya göstermiyor, araca sormak güvenilir değil ve doğru
bilgi ancak tarayıcının geliştirici tarafından okunabiliyor. Ayrıntı
`kanit/bolum-19/OLCUM-19_hangi-model_20260830.md`.

**Ölçüm koşulları neden yazılıyor:** oturum açık/kapalı, varsayılan model, arama
açık/kapalı - bunların hepsi sonucu değiştirir. Koşulu yazmayan ölçüm ölçüm değil.
