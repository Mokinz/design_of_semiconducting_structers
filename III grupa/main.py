import csv

N_x = 1000

x_min = 0
x_max = 1
x = 0

g = 1
y = 0.2

dx = (x_max - x_min) / (N_x - 1)
dy = 0.01

# przerwy energetyczne
Eg_GaAs = 1.519
Eg_AlAs = 3.099
Eg_GaSb = 0.812
Eg_AlSb = 2.386

# bonding dla energii (b_Eg_AlGaAs oraz b_Eg_AlGaSb sa zdefiniowne potem poniewaz sa funkcja zalezna od x)
b_Eg_GaAsSb = 1.43
b_Eg_AlAsSb = 0.8

# stale sieci
alc_GaAs = 5.65325
alc_AlAs = 5.6611
alc_GaSb = 6.0959
alc_AlSb = 6.1355

# bonding sieci
b_alc_AlGaAs = 0
b_alc_AlGaSb = 0
b_alc_GaAsSb = 0
b_alc_AlAsSb = 0

# spin-orbit
so_GaAs = 0.341
so_AlAs = 0.28
so_GaSb = 0.76
so_AlSb = 0.676

# bonding spin-orbity
b_so_AlGaAs = 0
b_so_AlGaSb = 0.3
b_so_GaAsSb = 0.6
b_so_AlAsSb = 0.15

# masa cięzkich dziur
mhh_GaAs = 0.55
mhh_AlAs = 0.81
mhh_GaSb = 0.37
mhh_AlSb = 0.9

# bonding dla cięzkich dziur
b_mhh_AlGaAs = 0
b_mhh_AlGaSb = 0
b_mhh_GaAsSb = 0
b_mhh_AlAsSb = 0

# masa lekkich dziur
mlh_GaAs = 0.083
mlh_AlAs = 0.16
mlh_GaSb = 0.043
mlh_AlSb = 0.13

# bonding dla lekkich dziur
b_mlh_AlGaAs = 0
b_mlh_AlGaSb = 0
b_mlh_GaAsSb = 0
b_mlh_AlAsSb = 0

# masa efektywna elektronu
me_GaAs = 0.067
me_AlAs = 0.124
me_GaSb = 0.039
me_AlSb = 0.14

# bonding dla masa elektronu
b_me_AlGaAs = 0
b_me_AlGaSb = 0
b_me_GaAsSb = 0
b_me_AlAsSb = 0

# VBO
VBO_GaAs = -0.8
VBO_AlAs = -1.33
VBO_GaSb = -0.03
VBO_AlSb = -0.41

# bonding dla VBO
b_VBO_AlGaAs = 0
b_VBO_AlGaSb = 0
b_VBO_GaAsSb = -1.06
b_VBO_AlAsSb = -1.71

# przygotowanie plikow tekstowych
f1 = open("AlAsSb.csv", "w+", newline="")
f2 = open("GaAsSb.csv", "w+", newline="")
f3 = open("AlGaAs.csv", "w+", newline="")
f4 = open("AlGaSb.csv", "w+", newline="")
f5 = open("dane02.csv", "w+", newline="")
f6 = open("dane04.csv", "w+", newline="")
f7 = open("dane06.csv", "w+", newline="")
f8 = open("dane08.csv", "w+", newline="")

fieldnames1 = [
    "x",
    "Eg_AlAsSb",
    "alc_AlAsSb",
    "so_AlAsSb",
    "mhh_AlAsSb",
    "mlh_AlAsSb",
    "me_AlAsSb",
    "VBO_AlAsSb",
]
fieldnames2 = [
    "x",
    "Eg_GaAsSb",
    "alc_GaAsSb",
    "so_GaAsSb",
    "mhh_GaAsSb",
    "mlh_GaAsSb",
    "me_GaAsSb",
    "VBO_GaAsSb",
]
fieldnames3 = [
    "x",
    "Eg_AlGaAs",
    "alc_AlGaAs",
    "so_AlGaAs",
    "mhh_AlGaAs",
    "mlh_AlGaAs",
    "me_AlGaAs",
    "VBO_AlGaAs",
]
fieldnames4 = [
    "x",
    "Eg_AlGaSb",
    "alc_AlGaSb",
    "so_AlGaSb",
    "mhh_AlGaSb",
    "mlh_AlGaSb",
    "me_AlGaSb",
    "VBO_AlGaSb",
]
fieldnames5 = [
    "x",
    "Eg_AlGaAsSb",
    "alc_AlGaAsSb",
    "so_AlGaAsSb",
    "mhh_AlGaAsSb",
    "mlh_AlGaAsSb",
    "me_AlGaAsSb",
    "VBO_AlGaAsSb",
]

thewriter1 = csv.DictWriter(f1, fieldnames=fieldnames1, delimiter=",")
thewriter2 = csv.DictWriter(f2, fieldnames=fieldnames2, delimiter=",")
thewriter3 = csv.DictWriter(f3, fieldnames=fieldnames3, delimiter=",")
thewriter4 = csv.DictWriter(f4, fieldnames=fieldnames4, delimiter=",")
thewriter5 = csv.DictWriter(f5, fieldnames=fieldnames5, delimiter=",")
thewriter6 = csv.DictWriter(f6, fieldnames=fieldnames5, delimiter=",")
thewriter7 = csv.DictWriter(f7, fieldnames=fieldnames5, delimiter=",")
thewriter8 = csv.DictWriter(f8, fieldnames=fieldnames5, delimiter=",")

""" thewriter1.writeheader()
thewriter2.writeheader()
thewriter3.writeheader()
thewriter4.writeheader()
thewriter5.writeheader()
thewriter6.writeheader()
thewriter7.writeheader()
thewriter8.writeheader() """


for i in range(4):
    for j in range(N_x):
        x = x_min + j * dx

        b_Eg_AlGaAs = -0.127 + 1.31 * x
        b_Eg_AlGaSb = -0.044 + 1.22 * x

        # AlGaAs
        Eg_AlGaAs = Eg_GaAs * (1 - x) + Eg_AlAs * x - x * (1 - x) * b_Eg_AlGaAs
        alc_AlGaAs = alc_GaAs * (1 - x) + alc_AlAs * x - x * (1 - x) * b_alc_AlGaAs
        so_AlGaAs = so_GaAs * (1 - x) + so_AlAs * x - x * (1 - x) * b_so_AlGaAs
        mhh_AlGaAs = mhh_GaAs * (1 - x) + mhh_AlAs * x - x * (1 - x) * b_mhh_AlGaAs
        mlh_AlGaAs = mlh_GaAs * (1 - x) + mlh_AlAs * x - x * (1 - x) * b_mlh_AlGaAs
        me_AlGaAs = me_GaAs * (1 - x) + me_AlAs * x - x * (1 - x) * b_me_AlGaAs
        VBO_AlGaAs = VBO_GaAs * (1 - x) + VBO_AlAs * x - x * (1 - x) * b_VBO_AlGaAs

        # AlGaSb
        Eg_AlGaSb = Eg_GaSb * (1 - x) + Eg_AlSb * x - x * (1 - x) * b_Eg_AlGaSb
        alc_AlGaSb = alc_GaSb * (1 - x) + alc_AlSb * x - x * (1 - x) * b_alc_AlGaSb
        so_AlGaSb = so_GaSb * (1 - x) + so_AlSb * x - x * (1 - x) * b_so_AlGaSb
        mhh_AlGaSb = mhh_GaSb * (1 - x) + mhh_AlSb * x - x * (1 - x) * b_mhh_AlGaSb
        mlh_AlGaSb = mlh_GaSb * (1 - x) + mlh_AlSb * x - x * (1 - x) * b_mlh_AlGaSb
        me_AlGaSb = me_GaSb * (1 - x) + me_AlSb * x - x * (1 - x) * b_me_AlGaSb
        VBO_AlGaSb = VBO_GaSb * (1 - x) + VBO_AlSb * x - x * (1 - x) * b_VBO_AlGaSb

        # GaAsSb
        Eg_GaAsSb = Eg_GaAs * y + Eg_GaSb * (1 - y) - y * (1 - y) * b_Eg_GaAsSb
        alc_GaAsSb = alc_GaAs * y + alc_GaSb * (1 - y) - y * (1 - y) * b_alc_GaAsSb
        so_GaAsSb = so_GaAs * y + so_GaSb * (1 - y) - y * (1 - y) * b_so_GaAsSb
        mhh_GaAsSb = mhh_GaAs * y + mhh_GaSb * (1 - y) - y * (1 - y) * b_mhh_GaAsSb
        mlh_GaAsSb = mlh_GaAs * y + mlh_GaSb * (1 - y) - y * (1 - y) * b_mlh_GaAsSb
        me_GaAsSb = me_GaAs * y + me_GaSb * (1 - y) - y * (1 - y) * b_me_GaAsSb
        VBO_GaAsSb = VBO_GaAs * y + VBO_GaSb * (1 - y) - y * (1 - y) * b_VBO_GaAsSb

        # AlAsSb
        Eg_AlAsSb = Eg_AlAs * y + Eg_AlSb * (1 - y) - y * (1 - y) * b_Eg_AlAsSb
        alc_AlAsSb = alc_AlAs * y + alc_AlSb * (1 - y) - y * (1 - y) * b_alc_AlAsSb
        so_AlAsSb = so_AlAs * y + so_AlSb * (1 - y) - y * (1 - y) * b_so_AlAsSb
        mhh_AlAsSb = mhh_AlAs * y + mhh_AlSb * (1 - y) - y * (1 - y) * b_mhh_AlAsSb
        mlh_AlAsSb = mlh_AlAs * y + mlh_AlSb * (1 - y) - y * (1 - y) * b_mlh_AlAsSb
        me_AlAsSb = me_AlAs * y + me_AlSb * (1 - y) - y * (1 - y) * b_me_AlAsSb
        VBO_AlAsSb = VBO_AlAs * y + VBO_AlSb * (1 - y) - y * (1 - y) * b_VBO_AlAsSb

        # GaAlAsSb
        Eg_AlGaAsSb = (
            x * (1 - x) * (y * Eg_AlGaAs + (1 - y) * Eg_AlGaSb)
            + y * (1 - y) * (x * Eg_AlAsSb + (1 - x) * Eg_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))
        alc_AlGaAsSb = (
            x * (1 - x) * (y * alc_AlGaAs + (1 - y) * alc_AlGaSb)
            + y * (1 - y) * (x * alc_AlAsSb + (1 - x) * alc_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))
        so_AlGaAsSb = (
            x * (1 - x) * (y * so_AlGaAs + (1 - y) * so_AlGaSb)
            + y * (1 - y) * (x * so_AlAsSb + (1 - x) * so_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))
        mhh_AlGaAsSb = (
            x * (1 - x) * (y * mhh_AlGaAs + (1 - y) * mhh_AlGaSb)
            + y * (1 - y) * (x * mhh_AlAsSb + (1 - x) * mhh_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))
        mlh_AlGaAsSb = (
            x * (1 - x) * (y * mlh_AlGaAs + (1 - y) * mlh_AlGaSb)
            + y * (1 - y) * (x * mlh_AlAsSb + (1 - x) * mlh_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))
        me_AlGaAsSb = (
            x * (1 - x) * (y * me_AlGaAs + (1 - y) * me_AlGaSb)
            + y * (1 - y) * (x * me_AlAsSb + (1 - x) * me_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))
        VBO_AlGaAsSb = (
            x * (1 - x) * (y * VBO_AlGaAs + (1 - y) * VBO_AlGaSb)
            + y * (1 - y) * (x * VBO_AlAsSb + (1 - x) * VBO_GaAsSb)
        ) / (x * (1 - x) + y * (1 - y))

        if g == 1:

            thewriter1.writerow(
                {
                    "x": x,
                    "Eg_AlAsSb": Eg_AlAsSb,
                    "alc_AlAsSb": alc_AlAsSb,
                    "so_AlAsSb": so_AlAsSb,
                    "mhh_AlAsSb": mhh_AlAsSb,
                    "mlh_AlAsSb": mlh_AlAsSb,
                    "me_AlAsSb": me_AlAsSb,
                    "VBO_AlAsSb": VBO_AlAsSb,
                }
            )

            thewriter2.writerow(
                {
                    "x": x,
                    "Eg_GaAsSb": Eg_GaAsSb,
                    "alc_GaAsSb": alc_GaAsSb,
                    "so_GaAsSb": so_GaAsSb,
                    "mhh_GaAsSb": mhh_GaAsSb,
                    "mlh_GaAsSb": mlh_GaAsSb,
                    "me_GaAsSb": me_GaAsSb,
                    "VBO_GaAsSb": VBO_GaAsSb,
                }
            )

            thewriter3.writerow(
                {
                    "x": x,
                    "Eg_AlGaAs": Eg_AlGaAs,
                    "alc_AlGaAs": alc_AlGaAs,
                    "so_AlGaAs": so_AlGaAs,
                    "mhh_AlGaAs": mhh_AlGaAs,
                    "mlh_AlGaAs": mlh_AlGaAs,
                    "me_AlGaAs": me_AlGaAs,
                    "VBO_AlGaAs": VBO_AlGaAs,
                }
            )

            thewriter4.writerow(
                {
                    "x": x,
                    "Eg_AlGaSb": Eg_AlGaSb,
                    "alc_AlGaSb": alc_AlGaSb,
                    "so_AlGaSb": so_AlGaSb,
                    "mhh_AlGaSb": mhh_AlGaSb,
                    "mlh_AlGaSb": mlh_AlGaSb,
                    "me_AlGaSb": me_AlGaSb,
                    "VBO_AlGaSb": VBO_AlGaSb,
                }
            )

        if y == 0.2:
            thewriter5.writerow(
                {
                    "x": x,
                    "Eg_AlGaAsSb": Eg_AlGaAsSb,
                    "alc_AlGaAsSb": alc_AlGaAsSb,
                    "so_AlGaAsSb": so_AlGaAsSb,
                    "mhh_AlGaAsSb": mhh_AlGaAsSb,
                    "mlh_AlGaAsSb": mlh_AlGaAsSb,
                    "me_AlGaAsSb": me_AlGaAsSb,
                    "VBO_AlGaAsSb": VBO_AlGaAsSb,
                }
            )

        if y == 0.4:
            thewriter6.writerow(
                {
                    "x": x,
                    "Eg_AlGaAsSb": Eg_AlGaAsSb,
                    "alc_AlGaAsSb": alc_AlGaAsSb,
                    "so_AlGaAsSb": so_AlGaAsSb,
                    "mhh_AlGaAsSb": mhh_AlGaAsSb,
                    "mlh_AlGaAsSb": mlh_AlGaAsSb,
                    "me_AlGaAsSb": me_AlGaAsSb,
                    "VBO_AlGaAsSb": VBO_AlGaAsSb,
                }
            )

        if y > 0.6 - dx and y < 0.6 + dy:

            thewriter7.writerow(
                {
                    "x": x,
                    "Eg_AlGaAsSb": Eg_AlGaAsSb,
                    "alc_AlGaAsSb": alc_AlGaAsSb,
                    "so_AlGaAsSb": so_AlGaAsSb,
                    "mhh_AlGaAsSb": mhh_AlGaAsSb,
                    "mlh_AlGaAsSb": mlh_AlGaAsSb,
                    "me_AlGaAsSb": me_AlGaAsSb,
                    "VBO_AlGaAsSb": VBO_AlGaAsSb,
                }
            )

        if y == 0.8:

            thewriter8.writerow(
                {
                    "x": x,
                    "Eg_AlGaAsSb": Eg_AlGaAsSb,
                    "alc_AlGaAsSb": alc_AlGaAsSb,
                    "so_AlGaAsSb": so_AlGaAsSb,
                    "mhh_AlGaAsSb": mhh_AlGaAsSb,
                    "mlh_AlGaAsSb": mlh_AlGaAsSb,
                    "me_AlGaAsSb": me_AlGaAsSb,
                    "VBO_AlGaAsSb": VBO_AlGaAsSb,
                }
            )
    y += 0.2
    g = 2

# zamkniecie plikow
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
