# -*- coding: utf-8 -*-
"""Ek J · Butun olcumlerin toplu skoru.
Her satir bir kanit dosyasindan elle okunup buraya yazildi; kaynagi yaninda.
Amac: kitabin kendi verisinden dogrulanabilir istatistik uretmek."""
import json

# (kod, konu, aracin urettigi DOGRULANABILIR birim sayisi, dogru cikan, kaynak)
K = [
 ("01","Mahkeme künyesi, üç araç",           10, 10, "resmi karar arama"),
 ("02","Kesim tarihi sonrası olay",            1,  1, "haber kaynağı"),
 ("03","Harf sayımı (aynı cevapta)",           2,  1, "elle sayım"),
 ("06","Aynı soru, üç koşu",                   3,  3, "tutarlılık değil doğruluk: üçü de doğru"),
 ("07","TR/EN kalite",                         2,  2, "iki dilde de doğru"),
 ("08","Israr testi, Araç B",                  1,  1, "kanun metni"),
 ("08B","Israr testi, Araç A",                 1,  1, "kanun metni"),
 ("09","İstem A/B (B kolu)",                   4,  4, "toplantı notu"),
 ("09A","İstem A/B (A kolu)",                  4,  3, "toplantı notu"),
 ("10","Uzun metinde üç iğne",                 3,  3, "metin"),
 ("11","Tablo toplamı, metinden",             19, 19, "elle hesap"),
 ("12","Yokluk sorusu, kısıtlı",               3,  3, "metin"),
 ("13","Türkçe biçimbilgisi + İng. çoğul",    20, 20, "dilbilgisi"),
 ("16","Yerel model, zor sorular",             5,  0, "resmi kaynak"),
 ("17","Yerel model, yaygın sorular",          6,  5, "genel bilgi"),
 ("18","Sahte künye doğrulatıldı",             1,  0, "resmi karar arama"),
 ("20","Baştan sona iş (sayılar)",            13, 13, "belgeler"),
 ("21","Kamu destekleri",                     18, 16, "kurum yayını"),
 ("23","Marş kıtası, yerel model",             4,  1, "kamuya açık metin"),
 ("23B","Marş dizesi, uluslararası model",     1,  0, "kamuya açık metin"),
 ("25","Israr testi, Araç C",                  1,  1, "kanun metni"),
 ("26","Yokluk sorusu, kısıtsız",              6,  6, "belgeler"),
 ("27","Tablo toplamı, görselden",             1,  1, "elle hesap"),
 ("28","Benzer iğneler",                       4,  4, "metin"),
]
t=sum(x[2] for x in K); d=sum(x[3] for x in K)
print(f"{'Kod':5s} {'Konu':38s} {'Üretilen':>9s} {'Doğru':>6s} {'Oran':>7s}")
print("-"*72)
for kod,konu,n,dg,_ in K:
    print(f"{kod:5s} {konu:38s} {n:9d} {dg:6d} {dg/n*100:6.0f}%")
print("-"*72)
print(f"{'':5s} {'TOPLAM':38s} {t:9d} {d:6d} {d/t*100:6.1f}%")

# arama/belge olan vs olmayan ayrimi (kitabin ana tezi)
BAKACAK_YER_VAR = {"01","02","06","07","08","08B","09","09A","10","11","12","13","20","21","25","26","27","28"}
BAKACAK_YER_YOK = {"03","16","17","18","23","23B"}
for ad,kume in [("Bakabileceği yer VARDI",BAKACAK_YER_VAR),("Bakabileceği yer YOKTU",BAKACAK_YER_YOK)]:
    a=sum(x[2] for x in K if x[0] in kume); b=sum(x[3] for x in K if x[0] in kume)
    print(f"\n{ad:26s} üretilen={a:3d}  doğru={b:3d}  oran=%{b/a*100:.1f}")
json.dump({"satirlar":K,"toplam":t,"dogru":d}, open("kanit/tur-06/skor.json","w"), ensure_ascii=False, indent=1)
