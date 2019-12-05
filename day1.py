import os

def module_fuel(mass):
    divisor = 3
    subtractor = 2
    mass = int(mass)

    if(mass <= 0):
        return 0

    fuel = mass//divisor - subtractor

    if(fuel < 0):
        fuel = 0

    return module_fuel(fuel) + fuel

def main():

    path = os.getcwd() + "/day1input.txt"
    file = open(path, "r")

    sum = 0
    for line in file:
        sum += module_fuel(line)

    print(sum)

main()