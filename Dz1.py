def check():
    if a + b > c and a > 0 and b > 0 and c > 0:
        g = (a + b + c) / 2

        apfer = (g * (g - a) * (g - b) * (g - c)) ** 0.5
        print(apfer)
    else:
        print('пиши по новой')


while True:
    try:
        a = float(input())
        b = float(input())
        c = float(input())
        check()
        break
    except:
        print('Введите число')
