def f(n,base=2):
    s = ""
    while n > 0:
        s = str(n%base) + s
        n //=base
    return int(s)

n = int(input("Введите число: "))
base = int(input("Введите значение СС: "))

print(f(n,base))

