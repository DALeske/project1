# code to sort the words in a sentence in alphabetical order
string_in = input("Enter a sentence:")
words = sorted(string_in.split())
print("Here are the sorted words in your text:""\n","\n".join(words))