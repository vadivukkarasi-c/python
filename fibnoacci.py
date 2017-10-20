previous, curent = 0, 1
total = 0
while True:
    previous, curent = curent, previous + curent
    if curent >= 4000000:
        break
    if curent % 2 == 0:
        total += curent
        print(total)