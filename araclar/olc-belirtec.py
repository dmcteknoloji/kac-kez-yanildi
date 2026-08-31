# -*- coding: utf-8 -*-
"""Ayni metnin Turkce ve Ingilizce hallerinin kac belirtece bolundugunu olcer.
Gercek tokenizer kullanir (tiktoken, o200k_base). Sonuc kanit/bolum-02/ altina yazilir."""
import tiktoken, json, datetime, sys

enc = tiktoken.get_encoding("o200k_base")

# Paralel metinler. Kaynak her cift icin ayri yazilir.
ciftler = [
    {
        "ad": "Insan Haklari Evrensel Beyannamesi, 1. madde",
        "kaynak": "BM resmi metin (TR ve EN resmi cevirileri)",
        "tr": "Butun insanlar hur, haysiyet ve haklar bakimindan esit dogarlar. Akil ve vicdana sahiptirler ve birbirlerine karsi kardeslik zihniyeti ile hareket etmelidirler.",
        "en": "All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.",
    },
    {
        "ad": "Gundelik cumle: toplanti",
        "kaynak": "Yazarin kendi cevirisi (kitapta boyle isaretlenir)",
        "tr": "Yarinki toplantida gorusebilecegimizi dusunuyorum, ama once raporu gozden gecirmemiz gerekiyor.",
        "en": "I think we will be able to meet at tomorrow's meeting, but we need to review the report first.",
    },
    {
        "ad": "Gundelik cumle: is",
        "kaynak": "Yazarin kendi cevirisi",
        "tr": "Musteriye gonderdigimiz faturada bir hata oldugunu fark ettik ve duzeltilmis halini ekte gonderiyoruz.",
        "en": "We noticed that there was an error in the invoice we sent to the customer and we are sending the corrected version attached.",
    },
    {
        "ad": "Mevzuat cumlesi",
        "kaynak": "6698 sayili Kanun m.12/5 (TR resmi metin) ve GDPR Art.33(1) (EN resmi metin) - ayni konu, birebir ceviri DEGIL",
        "tr": "Islenen kisisel verilerin kanuni olmayan yollarla baskalari tarafindan elde edilmesi halinde, veri sorumlusu bu durumu en kisa surede ilgilisine ve Kurula bildirir.",
        "en": "In the case of a personal data breach, the controller shall without undue delay notify the personal data breach to the supervisory authority.",
    },
]

satirlar = []
toplam_tr = toplam_en = 0
for c in ciftler:
    ttr = enc.encode(c["tr"]); ten = enc.encode(c["en"])
    c["tr_belirtec"] = len(ttr); c["en_belirtec"] = len(ten)
    c["tr_karakter"] = len(c["tr"]); c["en_karakter"] = len(c["en"])
    c["oran"] = round(len(ttr)/len(ten), 2)
    toplam_tr += len(ttr); toplam_en += len(ten)

# Tek kelime: Turkcede ek yigilmasi
kelimeler = ["ev", "evler", "evlerimiz", "evlerimizden", "evlerimizdekiler",
             "gorusebilecegimizi", "muvaffakiyetsizlestiricilestiriveremeyebileceklerimizden",
             "house", "houses", "unbelievable", "internationalization"]
kelime_sonuc = []
for k in kelimeler:
    ids = enc.encode(k)
    parcalar = [enc.decode([i]) for i in ids]
    kelime_sonuc.append({"kelime": k, "belirtec": len(ids), "parcalar": parcalar})

cikti = {
    "tarih": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "tokenizer": "tiktoken o200k_base (acik kaynak, yerelde calisti)",
    "not": "Bu bir model ciktisi degil, olculebilir bir metin isleme adimidir. Her araca gore sayilar biraz degisir, oran degismez.",
    "ciftler": ciftler,
    "toplam": {"tr": toplam_tr, "en": toplam_en, "oran": round(toplam_tr/toplam_en, 2)},
    "kelimeler": kelime_sonuc,
}
print(json.dumps(cikti, ensure_ascii=False, indent=2))
