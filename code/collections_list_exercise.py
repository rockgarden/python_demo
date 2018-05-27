# Exercise: Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")
# Jack can't make it! Let's invite Gary instead.
del (guests[1])
guests.insert(1, 'gary snyder')
# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")
# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")
name = guests[3].title()
print(name + ", please come to dinner.")
name = guests[4].title()
print(name + ", please come to dinner.")
name = guests[5].title()
print(name + ", please come to dinner.")
# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")
name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")
name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")
name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")
# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
# Empty out the list.
del (guests[0])
del (guests[0])
# Prove the list is empty.
print(guests)

# Exercise: Seeing the World
locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
print("Original order:")
print(locations)
print("\nAlphabetical:")
print(sorted(locations))
print("\nOriginal order:")
print(locations)
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))
print("\nOriginal order:")
print(locations)
print("\nReversed:")
locations.reverse()
print(locations)
print("\nOriginal order:")
locations.reverse()
print(locations)
print("\nAlphabetical")
locations.sort()
print(locations)
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

# A number raised to the third power is called a cube
cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)
for cube in cubes:
    print(cube)
cubes = [number ** 3 for number in range(1, 11)]  # Cube Comprehension
for cube in cubes:
    print(cube)
