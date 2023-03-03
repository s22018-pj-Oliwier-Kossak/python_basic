
def PrintCat():
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)


def PrintBear():
    txt = r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`'''
    print(txt)

def PrintBat():
    txt = r'''
      /\                 /\
     / \'._   (\_/)   _.'/ \
    /_.''._'--('.')--'_.''._\
    | \_ / `;=/ " \=;` \ _/ |
     \/ `\__|`\___/`|__/`  \/
             \(/|\)/       '''
    print(txt)

def PrintAnimal(animal = '', quantity = 1):
    if animal.lower() == 'cat':
        for i in range(quantity):
            PrintCat()

    elif animal.lower() == 'bear':
        for i in range(quantity):
            PrintBear()

    elif animal.lower() == 'bat':
        for i in range(quantity):
            PrintBat()

    else:
        print("incorrect animal")
        return False
    return True



PrintAnimal('cat')
