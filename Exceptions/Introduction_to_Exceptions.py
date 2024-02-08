"""
Exceptions are special events that happen when something out of the ordinary happens while our code is running.
--> An exception is generally unexpected behavior we can deal with and continue from out code.
--> An exception is not necessarily an error
--> try..except...finally block can be used in for or while loops, as well as if-statements

                EXCEPTION TERMINOLOGY
--> An exception is a special type of object in python
--> raising means starting an exception event flow
--> Exception handling means interacting with an exception flow in some manner
--> Unhandled exception is an exception that is not handled by our code. It generally causes the code to terminate
abruptly

            EXCEPTION HIERARCHY
--> Exceptions form a hierarchy
--> This basically meanas exceptions can be sub-divided into sub-exceptions that are more specific
    --> For example, a broad exception might be LookupError (which is a type of exception).
        --> IndexError and a KeyError are sub-divisions of a LookupError.
    --> For example, a broad exception might be OSError (which is a type of exception).
        --> FileNotFoundError and NotADirectoryError are sub-divisions of OSError
--> If an exception is an IndexError exception, it is also a/an:
    --> LookupError exception
    --> Exception exception
--> Custom Exception types are written using Classes
--> To handle an IndexError, we can choose to:
    --> handle IndexError exceptions (which is very specific for IndexError exceptions)
    --> hadnle LookupError exceptions
    --> handle Exception exception (which is very broad way of handling exceptions)

           COMMON PYTHON BUILT-IN EXCEPTION TYPES
--> SyntaxError
--> ZeroDivisionError
--> IndexError
--> KeyError
--> ValueError
--> TypeError
--> FileNotFoundError, etc

                EAFP vs LBYL
--> LBYL which means they have to Look Before You Leap
--> EAFP which means it is Easiier to Ask Forgiveness than Permission

            EXCEPTION HANDLING FLOW
--> An exception occurs
    --> An exception object is created
    --> An exception flow is started
--> We can either do nothing about the exception and the program terminates, or we intercept the exception flow,
by trying to handle the exception, if possible then resume running program uninterrupted or let the exception resume
so we can make a log of the exception or we can start a new exception.

        RAISING EXCEPTIONS
--> We can start an exception flow by raising an exception
--> An exception object is associated with an exception flow by:
    --> creating a new exception object and raising the exception
    ex = ValueError('Name must be at least five characters long')
        raise ex
        raise ValueError('custom message')
"""

# RAISING EXCEPTIONS
# a = 1
# b = 0
# result = a/b #Creating exception
# print(result) #Raising exception

ex = ValueError('Name must be at least 5 characters long')
print(type(ex))
print(repr(ex))
print(ex)
print(str(ex))

# raise ex

name = input('Enter name (5 characters min): ')
if len(name) < 5:
    raise ValueError(f'{name} is not five characters or more...')

print(f'Hello {name}!')

print(issubclass(KeyError, LookupError))
print(issubclass(KeyError, Exception))
print(issubclass(IndexError, LookupError))
ex = KeyError('some message')

print(type(ex))
print(isinstance(ex, KeyError))
print(isinstance(ex, Exception))
print(isinstance(ex, IndexError))























