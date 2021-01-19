spoj_1 = input("Serijski: ")
spoj_2 = input("Paralelno: ")
R1 = int(input("R1: "))
R2 = int(input("R2: "))
R3 = int(input("R3: "))


def serijski(r1, r2, r3):
    ruk = r1 + r2 + r3
    print(ruk)


def paralelno(rx, ry, rz):
    ruk = 1/rx + 1/ry + 1/rz
    print(ruk**-1)


def paralelno_2(rx, ry):
    ruk = 1/rx + 1/ry
    print(ruk**-1)


def mjesoviti(x, y, z):
    ruk = 1/x + 1/y
    print(ruk, z)
    ruk**-1
    ruk = ruk + z
    print(ruk)


if spoj_2 == "R1 R2 R3":
    paralelno(R1, R2, R3)

elif spoj_1 == "R1 R2 R3":
    serijski(R1, R2, R3)

else:
    if spoj_2 == "R1 R2":
        paralelno_2(R1, R2)

    elif spoj_2 == "R2 R3":
        mjesoviti(R2, R3, R1)

    elif spoj_2 == "R1 R3":
        paralelno_2(R1, R3)

    elif spoj_1 == "R1 R2":
        serijski(R1, R2, 0)

    elif spoj_1 == "R2 R3":
        serijski(0, R2, R3)

    elif spoj_1 == "R1  R3":
        serijski(R1, 0, R3)
