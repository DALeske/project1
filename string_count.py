# simple program to prompt for a string and then return the word count and character count, with and without spaces

# input string
str_input = input("Enter a string:")
 
 # Process the string for word count and character count
len_str = len(str_input) # length of string
len_str_no_space = len(str_input.replace(" ","")) # length of string without spaces
len_str_words = len(str_input.split()) # word count of string

# Output the word count and character counts
print ("This string has ",len_str_words, " words, ", len_str, " characters including spaces, and ",len_str_no_space," characters without spaces")