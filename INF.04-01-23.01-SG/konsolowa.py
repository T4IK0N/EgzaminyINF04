def nwd(a: int, b: int):
    while a != b:

        if a > b:
            a%=a-b
        else:
            b%=b-a
    return a

print(nwd(27, 9))