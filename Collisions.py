# Collisions

dictionary_of_fruits = {}
dictionary_of_fruits ['a'] = {'апельсин':'250','абрикос':'280'}
dictionary_of_fruits ['б'] = {'банан':'150'}

for key in dictionary_of_fruits:
    print (dictionary_of_fruits[key])

for key in dictionary_of_fruits:
    part_of_dictionary = dictionary_of_fruits[key]
    for key in part_of_dictionary:
        print (part_of_dictionary[key])