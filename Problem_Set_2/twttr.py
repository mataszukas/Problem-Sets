def main():
    user_input = input("Input: ").strip()
    consonant(user_input)

def consonant(text):

    result = "" #initiate empty string

    for v in text:

        if v not in "aeiouAEIOU":
            result += v #add consonants to result string

    if text.isupper(): #checks if text is uppercase
        print("Output:", result, end = "")
    else:
        print("Output:", result.capitalize(), end = "") #capitalizes result string

main()
