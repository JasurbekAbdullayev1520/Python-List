s = input("So'zlarni bo'sh joy bilan kiriting: ").strip()
if not s:
    print("Hech narsa kiritilmadi.")
else:
    soz = s.split()
    uzun = ""
    mx = 0
    for i in soz:
        if len(i) > mx:   
            uzun = i
            mx = len(i)
    print("Eng uzun so'z:", uzun)
