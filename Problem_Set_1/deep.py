def main():
    forty_two = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower() #ignores whitespaces,
    #lowercases letters to make them case insensitive
    match forty_two: #match input with case str
        case "42" | "forty-two" | "forty two": #when it is a variation of 42
            print("Yes")
        case _:
            print("No") #when it's not a variation of 42

main()
