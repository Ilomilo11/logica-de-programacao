m1 = int(input("insira a massa 1: "))  # massa de água fria (em gramas, 1 ml = 1 g para água)
T1 = int(input("insira a temperatura 1: "))   # temperatura inicial da água fria em graus Celsius
m2 = int(input("insira a massa 2: "))  # massa de água quente (também em gramas)
T2 = int(input("insira a temperatura 2: "))  # temperatura inicial da água quente em graus Celsius


# Resolver para Tf
Tf = (m1 * T1 + m2 * T2) / (m1 + m2)

print(f"A temperatura final é: {Tf:.1f}")