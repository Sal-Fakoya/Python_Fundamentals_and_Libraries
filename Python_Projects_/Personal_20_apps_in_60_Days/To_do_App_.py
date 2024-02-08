from my_app_funcs_ import _add, _edit, _complete, creation_date, to_dos, dt_time_update

flag = 1
new_flag = 1
date_of_creation = creation_date()

# Introduction -- Say Hi and display date of creation.
print(f"""
\tWelcome!
\tCreation date: {date_of_creation}
""")

while flag:

    user_action = input(f"\n\tType add, show, edit, complete, or exit: ").casefold().strip()
    new_flag = 1

    match user_action:
        # matching with option "add"
        case 'add':
            _add(new_flag=1)

        # matching with option "show"
        case 'show' | 'display':
            if len(to_dos) == 0:
                print('\tNothing to show.')
            else:
                for idx, item in enumerate(to_dos):
                    print(f'{idx + 1}. {item.title()}')

        # matching with option "edit"
        case 'edit':
            # checking length of list. Print "Nothing to edit" if list is empty
            if len(to_dos) == 0:
                print('\n\tNothing to edit.')
            else:
                # else print to-do list
                for idx, item in enumerate(to_dos):
                    print(f'{idx + 1}. {item.title()}')
                print('\n\tGot it!')
                # calling edit function
                _edit(new_flag=1)

        # Deleting marked "complete" option
        case 'complete' | 'check':
            while new_flag:

                if len(to_dos) == 0:
                    print('\n\tNothing to edit.')
                    new_flag = 0
                else:
                    number = input(
                        '\n\tEnter the line number you want to mark complete.\n\t'
                        'Else exit this action by entering "leave": ')

                    # calling complete function
                    if number.casefold() == 'leave'.casefold() or number.casefold() == 'exit'.casefold():
                        new_flag = 0
                    else:
                        _complete(number)

        # Leave/exit/quit option
        case 'exit' | 'leave' | 'quit':
            while new_flag:
                sure = input('\n\tAre you sure you want to leave? Enter yes/no')
                if sure.casefold() == 'yes'.casefold():
                    new_flag = 0
                    flag = 0
                elif sure.casefold() == 'no'.casefold():
                    new_flag = 0
                else:
                    print('\n\tInvalid Command', end=" ")
                    continue

        # Other cases not available
        case _:
            print('\n\tThis action does not exist. Try again')

last_edit = dt_time_update()

print(f"""
\tBye!
\tStart Date: {date_of_creation}
\tLast edit: {last_edit}
""")
