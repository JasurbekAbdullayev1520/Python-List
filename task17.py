names = [] 
while True:
    text = input("Ism kiriting (to'xtatish uchun 'stop' yozing): ")
    if text.lower() == "stop":
        break
    names.append(text)   

print("Kiritilgan ismlar soni:", len(names))
