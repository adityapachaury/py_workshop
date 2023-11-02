[1.73, 1.68, 1.71, 1.89]

fam1 = [1.73, 1.68, 1.71, 1.89]
fam1
print(type(fam1))

fam2 = [["liz", 1.73], ["emma",  1.68], ["mom", 1.71], ["dad", 1.89]]
fam2
print(type(fam2))
print(fam2)

fam = ["liz", 1.73, "mom", 1.71,      "dad", 1.89]
print(fam)
print(fam[3])
print(fam[4])
print(fam[5])
print(fam[-2])
print(fam[-1])
print(fam[1:])
print(fam[:-1])
fam.append(25)
print(fam)
fam.remove(1.71)
print(fam)