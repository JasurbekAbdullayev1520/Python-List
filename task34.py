
raqam = list(map(int, input("6 ta sonni kiriting: ").split()))

juftliklar = []


for i in range(len(raqam)):
    for j in range(i+1, len(raqam)):  
        if raqam[i] + raqam[j] == 10:
            juftliklar.append((raqam[i], raqam[j]))

print("Yig'indisi 10 bo'lgan juftliklar:", juftliklar)
