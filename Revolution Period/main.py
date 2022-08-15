import constant
import math

def main():
    radius = 1000 * get_float("Orbital radius (km): ")
    mass = get_float("Mass of center of gravity (kg): ")
        
    print(f"Orbital period: {(((2 * constant.PI) * radius)/(math.sqrt((constant.G * mass)/radius)))/(60*60*24):.2f} days")


def get_float(prompt):
    while True:
        str = input(prompt)
        try:
            return float(str)
        except ValueError:
            print(f"{str} is not a float")

if __name__ == "__main__":
    main()