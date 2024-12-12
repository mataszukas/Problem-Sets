def main():
    greeting = input("Greeting: ").lstrip().lower()
    pass
    if "hello" in greeting:
        print("$0")
    elif "h" in greeting:
        print("$20")
    else:
        print("$100")
main()
