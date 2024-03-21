for i in range(5):
    angka = 2 if i % 2 == 0 else 3
    for j in range(5, i, -1):
        print(angka, end=" ")
    print()
