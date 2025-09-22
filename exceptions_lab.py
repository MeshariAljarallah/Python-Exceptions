def Value_Error():
    try:
        age = float(input("Enter ur age: "))
        return age
    except ValueError:
        print("That is a ValueError")
    except:
        print("It has nothing to do with the type of exception😑")


def Zero_Division_Error():
    try:
        num1 = float(input("Enter number1: "))
        num2 = float(input("Enter number2: "))
        return num1 / num2
    except ZeroDivisionError:
        print("That is a ZeroDivisionError")


def Type_Error():
    try:
        num1 = int(input("Enter number1: "))
        num2 = input("Enter number2: ")
        print(num1 + num2 )
    except TypeError:
        print("That is a TypeError")
    except:
        print("It has nothing to do with the type of exception😑")


def Index_Error():
    try:
        mylist = [10, 20, 30]
        index = int(input("Enter index: "))
        print(f"Value: {mylist[index]}")
    except IndexError:
        print("That is an IndexError")
    except:
        print("It has nothing to do with the type of exception😑")

def Key_Error():
    try:
        mydict = {"name": "mashari", "age": 506}
        key = input("Enter key: ")
        print("Value:", mydict[key])
    except KeyError:
        print("That is a KeyError")
    except:
        print("It has nothing to do with the type of exception😑")


def start():

    print("Welcome to Abu Youssef Exceptions")

    while True:
        try:
            exp = int(input('''\nTest any exception:
                        
            1- ValueError
            2- ZeroDivisionError
            3- TypeError
            4- IndexError
            5- KeyError
            6- Exit

            : '''))

            if exp == 6:
                print("Bye")
                break

            try:
                assert 1 <= exp <= 5, "Error: choose between 1 and 5"
            except:
                print("wrong input")
                
            if exp == 1:
                Value_Error()
            elif exp == 2:
                Zero_Division_Error()
            elif exp == 3:
                Type_Error()
            elif exp == 4:
                Index_Error()
            elif exp == 5:
                Key_Error()
        except ValueError:
            print("wrong input")
            continue

start()