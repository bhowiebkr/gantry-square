import math

WIDTH = 550
HEIGHT = 400
DELTA = 2.31/2 # difference in measurement between the two diagonals devided by 2

def sqr(n):
    return math.pow(n, 2)

def main():

    # Calculate the hypotenuse
    # Parallelogram Law: The sum of the squares of the sides is equal to the sum of the squares of the diagonals
    hypt = math.sqrt(sqr(WIDTH) + sqr(HEIGHT) - sqr(DELTA)) + DELTA

    # Triangle A with cosine law
    a = 90 - math.acos((sqr(HEIGHT) + sqr(WIDTH) - sqr(hypt)) / (2 * HEIGHT * WIDTH)) * 180 / math.pi

    # Triangle B with sin law
    b = WIDTH * math.sin(math.radians(a)) / math.sin(math.radians(90))

    print(f'Move right limit switch {b:.2f}mm') # Eg: Move limit switch 3.92mm


if __name__ == '__main__':
    main()
