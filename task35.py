s = input("So'zlarni bo'sh joy bilan kiriting: ").strip()

qisqa, orta, uzun = [], [], []

for i in (s.split() if s else []):
    if len(i) <= 3:
        qisqa.append(i)
    elif len(i) <= 6:
        orta.append(i)
    else:
        uzun.append(i)

if not s:
    print("Hech narsa kiritilmadi.")
else:
    print("<=3 harfli:", qisqa)
    print("4-6 harfli:", orta)
    print(">6 harfli:", uzun)

