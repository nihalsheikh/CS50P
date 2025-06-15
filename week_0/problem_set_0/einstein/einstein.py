# Week 0: Problem 4
# calculate E=mc**2 formula
def formula(mass):
    E = mass * (300000000)**2
    return E

def main():
    mass = int(input("Enter mass in kg: "))
    print(formula(mass))

main()
