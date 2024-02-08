# Parent function
def greet(lang: str):
    # Child function
    def greeting(name: str):
        if lang == 'english':
            return f'Hello, {name}'
        elif lang == 'french':
            return f'Bonjour, {name}'
        elif lang == 'spanish':
            return f'Hola, {name}'
        else:
            return f'Sorry, I don\'t know how to greet in {lang}'

    return greeting


# print(greet('english')('Karol'))  # lol, just tested this out
greetOne = greet('english')

print(greetOne('Salamot'))

my_var = 34


def pet_counter(pet_owner):
    # local scope: To manipulate outside variables in a local scope, you use keyword global
    pet_name = 'Buddy'
    counting = 0

    def counters():
        # enclosing scope: to manipulate local variables in an enclosing scope, you use keyword "nonlocal"
        nonlocal counting
        counting += 1
        return f'Pet owner: {pet_name} {pet_owner} has been called {counting} times'

    return counters


buddy_count = pet_counter('Brother')
print(buddy_count())

for i in range(4):
    print(buddy_count())