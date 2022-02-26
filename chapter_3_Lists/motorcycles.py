motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# To add an element to a list, use the Append method

motorcycles.append('kawasaki')
print(motorcycles)


# To add elements to a list in a specific spot, use the Insert method

motorcycles.insert(0, 'triumph')
print(motorcycles)

#  To remove an element from a list, use the del method

del motorcycles[0]
print(motorcycles)

# Delete an element using the pop() method. This method allows you to use the value after removing it. Pops from the bottom of the list if no location is specified.

popped_motorcycles = motorcycles.pop(0)
print(popped_motorcycles)
print(motorcycles)

# Remove an item by value by using the remove() method.
motorcycles.remove('suzuki')
print(motorcycles)

# Activity for chapter 3 is provided below. Pg. 42

people = ['Jocko', 'McRaven', 'Stumpf']
print(f'{people[0].title()}, would you like to come to dinner?')
print(f'{people[1].title()}, would you like to come to dinner?')
print(f'{people[2].title()}, would you like to come to dinner?')
print('\nModified\n')
print(f"{people[1].title()} can't make it.")
people[1] = 'Mike Glover'
print('\nNew List\n')
print(f'{people[0].title()}, would you like to come to dinner?')
print(f'{people[1].title()}, would you like to come to dinner?')
print(f'{people[2].title()}, would you like to come to dinner?\n')
print('More Guests\n')
print('Hey! I found a bigger table!')
people.insert(0, 'Scojo')
people.insert(2, 'Dan Daley')
people.append('Kevin Owen')
print('\nNew Invitations\n')
print(f'{people[0].title()}, would you like to come to dinner?')
print(f'{people[1].title()}, would you like to come to dinner?')
print(f'{people[2].title()}, would you like to come to dinner?')
print(f'{people[3].title()}, would you like to come to dinner?')
print(f'{people[4].title()}, would you like to come to dinner?')
print(f'{people[5].title()}, would you like to come to dinner?')
print('\nI can only invite two people for dinner\n')
popped_people = people.pop(0)
print(f'Sorry, {popped_people.title()}, but I can no longer invite you to dinner.')
popped_people = people.pop(1)
print(f'Sorry, {popped_people.title()}, but I can no longer invite you to dinner.')
popped_people = people.pop(3)
print(f'Sorry, {popped_people.title()}, but I can no longer invite you to dinner.')
popped_people = people.pop(1)
print(f'Sorry, {popped_people.title()}, but I can no longer invite you to dinner.')
print(f"{people[0].title()}, you're still invited!")
print(f"{people[1].title()}, you're still invited!")
print('\nEmptying List\n')
del people[0]
del people[0]
print(people)


