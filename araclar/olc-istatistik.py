# -*- coding: utf-8 -*-
"""Ek J icin: dil basina belirtec maliyeti + Turkcenin ek yuku.
Hepsi yerelde, model calistirmadan olculur."""
import json, tiktoken
from tokenizers import Tokenizer
import os
# Belirtecleyici tanim dosyasi depoda degil (kendi lisansiyla indirilir).
# Indirdikten sonra: VERI_DIZINI=/dosyanin/klasoru python3 betik.py
VERI = os.environ.get("VERI_DIZINI", ".")  # belirtecleyici dosyasinin bulundugu klasor

S=VERI
EN = tiktoken.get_encoding("o200k_base")
TR = Tokenizer.from_file(S+"/kumru-tokenizer.json")

# AYNI metin, alti dilde. Insan Haklari Evrensel Beyannamesi 1. madde (kamuya acik).
diller = {
 "Türkçe":  "Bütün insanlar hür, haysiyet ve haklar bakımından eşit doğarlar. Akıl ve vicdana sahiptirler ve birbirlerine karşı kardeşlik zihniyeti ile hareket etmelidirler.",
 "İngilizce":"All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.",
 "Almanca": "Alle Menschen sind frei und gleich an Würde und Rechten geboren. Sie sind mit Vernunft und Gewissen begabt und sollen einander im Geiste der Brüderlichkeit begegnen.",
 "Fransızca":"Tous les êtres humains naissent libres et égaux en dignité et en droits. Ils sont doués de raison et de conscience et doivent agir les uns envers les autres dans un esprit de fraternité.",
 "İspanyolca":"Todos los seres humanos nacen libres e iguales en dignidad y derechos y, dotados como están de razón y conciencia, deben comportarse fraternalmente los unos con los otros.",
 "İtalyanca":"Tutti gli esseri umani nascono liberi ed eguali in dignità e diritti. Essi sono dotati di ragione e di coscienza e devono agire gli uni verso gli altri in spirito di fratellanza.",
}
print("=== AYNI METIN, ALTI DIL · Ingilizce merkezli belirtecleyici ===")
ing = len(EN.encode(diller["İngilizce"]))
sonuc={}
for dil, m in diller.items():
    n = len(EN.encode(m))
    sonuc[dil]={"belirtec":n, "kat":round(n/ing,2), "karakter":len(m)}
    print(f"  {dil:12s} {n:4d} belirteç  ({n/ing:.2f} kat)  {len(m)} karakter")

print("\n=== TURKCE: eklerin bedeli (ayni kok, buyuyen kelime) ===")
zincir=["ev","evler","evlerim","evlerimiz","evlerimizde","evlerimizdeki","evlerimizdekiler","evlerimizdekilerden"]
ek=[]
for k in zincir:
    a=len(EN.encode(k)); b=len(TR.encode(k).ids)
    ek.append({"kelime":k,"ing":a,"tr":b})
    print(f"  {k:22s} İng.merkezli {a:2d}  ·  Türkçe {b:2d}")

print("\n=== SAPKALI/OZEL HARF: dogru yazim pahali mi ===")
ciftler=[("Türkçe karakterli","Görüşürüz, çok teşekkür ederim. Işığı söndürmeyi unutma."),
         ("ASCII'ye indirgenmiş","Gorusuruz, cok tesekkur ederim. Isigi sondurmeyi unutma.")]
sap={}
for ad,m in ciftler:
    a=len(EN.encode(m)); b=len(TR.encode(m).ids)
    sap[ad]={"ing":a,"tr":b}
    print(f"  {ad:22s} İng.merkezli {a:3d}  ·  Türkçe {b:3d}")

json.dump({"diller":sonuc,"ekler":ek,"sapka":sap}, open("kanit/bolum-04/OLCUM-29_dil-maliyeti.json","w"), ensure_ascii=False, indent=1)
print("\nyazildi: kanit/bolum-04/OLCUM-29_dil-maliyeti.json")
