
list1 = list(map(int, input("1-ro'yxat elementlarini probel bilan kiriting: ").split()))
list2 = list(map(int, input("2-ro'yxat elementlarini probel bilan kiriting: ").split()))


if len(list1) == len(list2):
   
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]

    print("Almashtirilgandan keyin:")
    print("list1 =", list1)
    print("list2 =", list2)
else:
    print("Ikkala ro'yxatning uzunligi teng bo'lishi kerak!")
