#replace uppercase letter with _,"lowercase letter"

def main():

    user_input = input("camelCase: ")
    replace(user_input)

def replace(camelcase):

    for s in range(len(camelcase)):
        if camelcase[s].isupper(): #checks if letter is uppercase
            camelcase = camelcase.replace(camelcase[s], "_" + camelcase[s].lower()) #replaces uppercase letter with "_{lowercase}" in a name
    print(camelcase)

main()
