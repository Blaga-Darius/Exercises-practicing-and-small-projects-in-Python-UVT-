#Write a program that finds the roots of a second degree equation. Considering the equation of the form ax2+bx+cax2+bx+c, the program will read a, b, and c from standard input. The program will output the two solutions for when the equation equals 0, in ascending order. If the equation has no real solutions, the program will print exactly: no real solutions.

import math
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    a = float(data[0])
    b = float(data[1])
    c = float(data[2])

    delta = b**2 - 4 * a * c

    if delta < 0:
        print("no real solutions")
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)

        sol1 = min(x1, x2)
        sol2 = max(x1, x2)

        print(sol1)
        print(sol2)


if __name__ == "__main__":
    main()