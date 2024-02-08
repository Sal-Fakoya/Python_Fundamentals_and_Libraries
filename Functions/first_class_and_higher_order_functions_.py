"""
                                FIRST CLASS FUNCTIONS
--> A first class function is a function that can be seen and treated as variables and items.

                                HIGHER-ORDER FUNCTIONS
--> A higher order function is a function that can call a first class function.

"""


def dog_sound():
    return 'woof'


def cat_sound():
    return 'meow'


bulldog_sound = dog_sound
animal_sounds = [dog_sound, cat_sound]

print(bulldog_sound())

for animal_sound in animal_sounds:
    print(animal_sound())


def identify_animal_sound(animal_sound):
    if animal_sound() == 'woof':
        print('The animal is a dog.')
    else:
        print('The animal is a cat.')


identify_animal_sound(cat_sound)
identify_animal_sound(dog_sound)

