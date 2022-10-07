def shout(text: str) -> str:
    return text.upper()

def whisper(text: str) -> str:
    return text.lower()

def greet(func):
    """
    Storing the function in a variable.
    Les fonctions qui peuvent accepter d'autres fonctions comme arguments sont également appelées
    fonctions d'ordre supérieur.
    """
    greeting = func("Hey, j'ai été créé par une fonction passée en argument.")
    print(greeting)

def create_adder(x):
    def adder(y):
        return x+y

    return adder

# print(shout("small world"))
# yell = shout
# print(yell("small world"))

# greet(shout)
# greet(whisper)

add_15 = create_adder(15) # En fait add_15 est la fonction adder

print("type(add_15) = ", type(add_15))
print("add_15 = ", add_15)
print("add_15(10) = ", add_15(10))