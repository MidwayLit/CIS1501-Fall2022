some_number = 10
some_number_with_a_decimal = 15.6
some_string = "some text in quotes or single quotes or raw or ...."

# python list - is just a list of things - order matters
erics_kids_names = ["Joy", "Jebriel", 'Jevavieve', 'Journey',
                    'Jubilee', 'Jackson', 'Jasper']

print(erics_kids_names)

# access individual items by INDEX using [ index_number ]
print("Happy Birthday", erics_kids_names[0])

# get or set using the same notation
erics_kids_names[0] = "JOY"

print("Happy Birthday", erics_kids_names[0])

print("Eric has", len(erics_kids_names), "kids")

# add an item to the end of the list
erics_kids_names.append("Jade")

print(erics_kids_names)

# this will crash, there is no value at index 10
#print(erics_kids_names[10])

things_to_remember = [42, "buy coffee",
                      'add the lab assignment', 10, 42 / 7]

things_to_remember.pop() # removes the last item
things_to_remember.pop(0) # removes the item at that index

list_of_lists = [ ['first item in sub list', 'second item in sub list'],
                  'second item in main list' ]

print(list_of_lists[0][1])

scores = [10, 9, 8, 10, 8, 9, 10]

highest_score = max(scores)
lowest_score = min(scores)
total_scores = sum(scores)
average_score = sum(scores) / len(scores)

print("highest", highest_score)
lowest_score_string = "lowest score: " + str(lowest_score)
print(lowest_score_string)
print("average", average_score)

slow_way_new_average_score = ( sum(scores) - lowest_score ) / ( len(scores) - 1 )

# only removes the first one it finds
scores.remove(lowest_score)


new_average_score = sum(scores) / len(scores)

print(new_average_score)
print(slow_way_new_average_score)

# tuple - TOO pull or TUH pull - use ( )
final_scores = (100, 95, 97, 90, 100, 100, 95)

highest_score = max(final_scores)
lowest_score = min(final_scores)
total_scores = sum(final_scores)
average_score = sum(final_scores) / len(final_scores)

# still use [ ]  for index even with a tuple
print("first final score", final_scores[0])

# you can't change individual values
# final_scores[0] = 90


# sets are an unordered collection of unique items
unique_numbers = set([1,2,3,4,5,6])
print(unique_numbers)

unique_numbers.add(4)

unique_numbers.add(42)

print(unique_numbers)
                    # key : associated value
names_and_scores = {'Alan': 100, 'Bob': 90, 'Carrie': 80, 'Don': 100}
print(names_and_scores)
                                        # key of - find the value associated with the key of
print("Alan's score is", names_and_scores['Alan'])

names_and_scores['Alan'] = 95

print("Alan's score is", names_and_scores['Alan'])

# remove the key/value pair
names_and_scores.pop('Alan')
print(names_and_scores)

# add a score for a key of
# add/update - if the key exists, it updates - if the key doesn't exist, it adds
names_and_scores['Eric'] = 100


print(names_and_scores)

names = ['Bob', 'Carrie', 'Don', 'Eric']
scores = [90, 80, 100, 100]

names.remove("Eric")
scores.pop(3)


names_and_scores['Bob'] = 'Failed'

names_and_scores[100] = 'Eric'

print(names_and_scores)

from_user_names_and_scores = {}

name = input("Enter the first student's name")
score = int(input("Enter " + name + "'s score"))

from_user_names_and_scores[name] = score

name = input("Enter the second student's name")
score = int(input("Enter " + name + "'s score"))

from_user_names_and_scores[name] = score

name = input("Enter the third student's name")
score = int(input("Enter " + name + "'s score"))

from_user_names_and_scores[name] = score

name = input("Enter the fourth student's name")
score = int(input("Enter " + name + "'s score"))

from_user_names_and_scores[name] = score


print(from_user_names_and_scores)

name = 'Eric Charnesky'
first_letter = name[0]

print("your name has", len(name), 'characters')

max_letter = max(name)
min_letter = min(name)
