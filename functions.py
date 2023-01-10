from collections.abc import Callable
import my_library
# autre version du import 
from my_library import randint_list


def addition(a: float, b: float) -> float:
    """Cette fonction permet d'additionner deux nombres
    a float le premier nombre à additioner
    b float le deuxième nombre à additioner
    return float le résultat de l'addition
    """
    result = a + b

    return result

result = addition(123, 42)
print(result)

my_number1 = 123
my_number2 = 42
result = addition(my_number1, my_number2)
print(result)

def calculer(calcul1: Callable, calcul2: Callable, a: float, b: float, c: float) -> float: 
    result = calcul1(a, b)
    result = calcul2(result, c)
def randint_list(lower_value,higher_value,count):

    numbers=[]

    for i in range(0,count):
        number = random.randint(lower_value,higher_value)
        numbers.append(number)

    return numbers
 #préciser le nom de la librairie devant le nom de la fonction
my_list = my_library.randint_list(0, 100, 10)
print(my_list)

# le code "from my_library import randint_list" permet de ne pas préciser le nom de la librairie
my_list = randint_list(0, 100, 300)
print(my_list)

#écrire une fonction qui accepte en paramètre une liste et qui renvoie la moyenne des nombres de la liste 
def my_average(numbers: list) -> float:
    my_sum = 0

    for number in numbers:
        my_sum += number

    result = my_sum / len(numbers)

    return result

def my_averag2(numbers: list) -> float:
    my_sum = 0

    for number in numbers:
        if type(number) is int or type(number) is float: 
            my_sum += number

    result = my_sum / len(numbers)

    return result

my_list = [42, True, 'abc', 123]
result = my_average2(my_list)
print(result)