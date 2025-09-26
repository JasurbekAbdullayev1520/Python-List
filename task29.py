text = []

for i in range(10):
    a = int(input("Son kiriting: "))
    text.append(a)
unique = []
for v in text:
    if text.count(v) == 1:
       unique.append(v)
print(f"Takrorlnamaydigan element: {unique}")


   

   



