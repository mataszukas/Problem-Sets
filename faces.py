def convert_smileys(text):

    text = text.replace(":(", "🙁") #replace frowny face with emoji
    text = text.replace(":)", "🙂") #replace smiley face with emoji
    return text #returns converted text

def main():

    final_text = convert_smileys(input()) #send input text as an argument
    print(final_text) #prints returned coverted text


main()
