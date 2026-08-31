# -*- coding: utf-8 -*-
"""Turkce icin egitilmis bir tokenizer ile Ingilizce merkezli bir tokenizer'i
ayni Turkce metinlerde karsilastirir. Iki taraf da yerelde calisir."""
import json, datetime, sys
import tiktoken
from tokenizers import Tokenizer
import os
# Belirtecleyici tanim dosyasi depoda degil (kendi lisansiyla indirilir).
# Indirdikten sonra: VERI_DIZINI=/dosyanin/klasoru python3 betik.py
VERI = os.environ.get("VERI_DIZINI", ".")  # belirtecleyici dosyasinin bulundugu klasor


EN = tiktoken.get_encoding("o200k_base")
TR = Tokenizer.from_file(os.path.join(VERI,"kumru-tokenizer.json"))

metinler = [
    ("İnsan Hakları Evrensel Beyannamesi, 1. madde",
     "Bütün insanlar hür, haysiyet ve haklar bakımından eşit doğarlar. Akıl ve vicdana sahiptirler ve birbirlerine karşı kardeşlik zihniyeti ile hareket etmelidirler."),
    ("Gündelik cümle: toplantı",
     "Yarınki toplantıda görüşebileceğimizi düşünüyorum, ama önce raporu gözden geçirmemiz gerekiyor."),
    ("Gündelik cümle: fatura",
     "Müşteriye gönderdiğimiz faturada bir hata olduğunu fark ettik ve düzeltilmiş halini ekte gönderiyoruz."),
    ("Mevzuat cümlesi (6698 m.12/5)",
     "İşlenen kişisel verilerin kanuni olmayan yollarla başkaları tarafından elde edilmesi hâlinde, veri sorumlusu bu durumu en kısa sürede ilgilisine ve Kurula bildirir."),
]

kelimeler = ["ev","evler","evlerimiz","evlerimizden","evlerimizdekiler",
             "görüşebileceğimizi","çocuklarımız","muvaffakiyetsizleştiricileştiriveremeyebileceklerimizden"]

print(f"{'Metin':46s} {'İng.merkezli':>13s} {'Türkçe':>8s} {'Fark':>8s}")
print("-"*80)
tEN=tTR=0
satirlar=[]
for ad, m in metinler:
    a=len(EN.encode(m)); b=len(TR.encode(m).ids)
    tEN+=a; tTR+=b
    fark = (a-b)/b*100
    satirlar.append({"ad":ad,"ingilizce_merkezli":a,"turkce":b,"fazla_yuzde":round(fark,1)})
    print(f"{ad[:46]:46s} {a:13d} {b:8d} {'%+.0f'%fark:>8s}")
print("-"*80)
tf=(tEN-tTR)/tTR*100
print(f"{'TOPLAM':46s} {tEN:13d} {tTR:8d} {'%+.0f'%tf:>8s}")
print()
print("Tek kelimeler:")
kl=[]
for k in kelimeler:
    a=len(EN.encode(k)); b=len(TR.encode(k).ids)
    kl.append({"kelime":k,"ingilizce_merkezli":a,"turkce":b})
    print(f"  {k[:56]:58s} {a:3d} parça  ->  {b:3d} parça")

json.dump({
 "tarih": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
 "ingilizce_merkezli_tokenizer": "tiktoken o200k_base",
 "turkce_tokenizer": "Kumru-2B tokenizer (VNGRS, Apache 2.0, Hugging Face'ten indirildi)",
 "not": "Iki taraf da yerelde calistirildi. Bu bir model karsilastirmasi DEGIL, yalnizca metnin kac parcaya bolundugunun olcumudur.",
 "metinler": satirlar,
 "toplam": {"ingilizce_merkezli": tEN, "turkce": tTR, "fazla_yuzde": round(tf,1)},
 "kelimeler": kl,
}, open("kanit/bolum-04/OLCUM-15_turkce-tokenizer_20260830.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
