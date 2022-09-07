
# tells python you want the math library in your program
import math

# modulus - integer remainder of the division
remainder = 10 % 3

# // is for integer division
print(" 10 / 3 is", 10 // 3, "with a remainder of", 10 % 3)


number_of_people_at_party = int(input("How many people are coming to the party?"))

number_of_slices_per_person = int(input("How many slices of pizza does an average person eat?"))

number_of_slices_per_pizza = int(input("How many slices are in a pizza?"))

total_slices_needed = number_of_people_at_party * number_of_slices_per_person

pizzas_needed = math.ceil(total_slices_needed / number_of_slices_per_pizza)

print("You need to order", pizzas_needed, "pizzas for the party")

first_name = 'Eric'
last_name = 'Charnesky'

name = first_name + " " + last_name

# can't divide by zero, it crashes, =(
# value = 10.0 / 0.0

#print(value)

print(name)

some_string = "na"

# multiplying strings just repeats it
some_other_string = some_string * 10

# can't divide strings
#some_new_string = some_other_string / 10

end_result = some_other_string + " batman!"

print(end_result)

# ord gets the numeric value of a character
print("The value for E is", ord("E"))
print("The value for r is", ord("r"))
print("The value for i is", ord("i"))
print("The value for c is", ord("c"))
print("The character for number 69", chr(69))
print(chr(69) + chr(114) + chr(105) + chr(99))


# make sure it's a positive value
shift = abs(int(input("How many letters should we shift in the cipher?")))

# capital A is 65
first_letter = (ord("E") - 65 + shift) % 26 + 65
second_letter = (ord("R") - 65 + shift) % 26 + 65
third_letter = (ord("I") - 65 + shift) % 26 + 65
fourth_letter = (ord("C") - 65 + shift) % 26 + 65

print(chr(first_letter) + chr(second_letter) + chr(third_letter) + chr(fourth_letter))

# \ is the escape character
print('\"Eric\n Charnesky\\')
print(r'Eric\Charnesky')

print("""
    Multiple lines
another     line
more \lines
wow!
""")

print("Menu")
print("$2\t\tCoffee")
print("$2.5\tEspresso")

print("""Menu
$2      Coffee
$2.5    Espresso""")
