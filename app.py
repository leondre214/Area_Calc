# This is a calculator that finds the areas of shapes!

while True:

    print("Welcome to the area calculator!")
    option = input("Enter S for square, T for triangle, R for rectangle or C for circle or Q to quit : ")
    letter1 = 'S'
    letter2 = 'T'
    letter3 = 'R'
    letter4 = 'C'
    letter5 = 'Q'
    letters = [letter1, letter2, letter3, letter4, letter5]

    # if letters[:] != letters:
    # print("Invalid response. Enter S for square, T for triangle, R for rectangle or C for circle or Q to quit : ")

    if option == 'Q':
        print("Have a nice day")
        break

    if option == 'S':
        length = float(input("Enter the length "))
        width = float(input("Enter the width "))
        height = float(input("Enter the height "))
        area = length * width * height
        print(str(area))

    if option == 'T':
        base = float(input("Enter the base "))
        height = float(input("Enter the height "))
        area = 0.5 * base * height
        print("Here is the area " + str(area))

    if option == 'R':
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input(" Enter the height: "))
        area = length * width * height
        print("The area of a rectangle is " + str(area))

    if option == 'C':
        radius = float(input("Enter the radius "))
        pi = 3.14159
        area = (radius ** 2) * pi
        print("The area of a circle is " + str(area))



