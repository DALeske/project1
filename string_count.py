str_input = input("Enter a string:") # input string
len_str = len(str_input) # length of string
len_str_no_space = len(str_input.replace(" ","")) # length of string without spaces
len_str_words = len(str_input.split()) # word count of string
print ("This string has ",len_str_words, " words, ", len_str, " characters including spaces, and ",len_str_no_space," characters without spaces")