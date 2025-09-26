
palindrom = []
for i in range(5):
    a = input("Matn kiriting: ")
    if a[::-1] == a:
       palindrom.append(a)
print(f"Palindrom ro'yhati: {palindrom}")