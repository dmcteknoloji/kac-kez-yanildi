# -*- coding: utf-8 -*-
"""Turkce icin sifirdan egitilmis yerli modeli, uluslararasi araclara
uygulanan AYNI cetvelle olcer. Model yerelde calisir, internet yok."""
import json, urllib.request, datetime, sys

MODEL = "hf.co/icecubetr/Kumru-2B-GGUF"

def sor(istem, n=300):
    veri = json.dumps({"model": MODEL, "prompt": istem, "stream": False,
                       "options": {"num_predict": n, "temperature": 0.7}}).encode()
    r = urllib.request.Request("http://localhost:11434/api/generate", data=veri,
                               headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(r, timeout=300) as f:
        return json.load(f)["response"].strip()

testler = [
    ("T1 · HARF SAYMA (1. bölümün ölçümü)",
     "muvaffakiyetsizleştiricileştiriveremeyebileceklerimizden kelimesinde kaç tane e harfi var? Sadece sayıyı yaz.",
     "Doğru: 11"),
    ("T2 · BİÇİMBİLGİSİ (ÖLÇÜM-13, tuzaklı)",
     "Aşağıdaki kelimelere belirtme hâli eki getir. Sadece ekli hallerini numaralı liste olarak yaz.\n1. kitap\n2. sepet\n3. burun\n4. devlet\n5. renk",
     "Doğru: kitabı / sepeti / burnu / devleti / rengi"),
    ("T3 · MEVZUAT (ÖLÇÜM-01)",
     "6698 sayılı Kanun'un 12. maddesinin 5. fıkrasında veri ihlali bildirimi için geçen süre ifadesi nedir? Kısa cevap ver.",
     "Doğru: 'en kısa sürede' (72 saat Kanun'da YOK, Kurul kararında)"),
    ("T4 · HESAP (ÖLÇÜM-11, kısaltılmış)",
     "Şu sayıları topla ve sadece sonucu yaz: 61887,78 + 50130,34 + 19358,23 + 2043,43 + 67100,59",
     "Doğru: 200520,37"),
    ("T5 · YOKLUK (ÖLÇÜM-12)",
     "Türkiye'de 2019 yılında çıkarılan 9999 sayılı Yapay Zeka Kanunu'nun 5. maddesi ne diyor?",
     "Doğru cevap: böyle bir kanun YOK, 'bilmiyorum' demeli"),
]

print(f"Model: {MODEL}\n")
sonuc=[]
for ad, istem, dogru in testler:
    print("="*74); print(ad); print("-"*74)
    print("İSTEM:", istem.replace("\n"," | ")[:150]); print()
    try:
        c = sor(istem)
    except Exception as e:
        c = f"[HATA: {e}]"
    print("CEVAP:", c[:600])
    print(); print(dogru); print()
    sonuc.append({"test":ad,"istem":istem,"cevap":c,"dogru":dogru})

json.dump({"tarih": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "model": MODEL, "calisma": "yerel (ollama), internet erisimi YOK, arama YOK",
           "sonuclar": sonuc},
          open("kanit/bolum-04/OLCUM-16_yerli-model_ham.json","w",encoding="utf-8"),
          ensure_ascii=False, indent=2)
