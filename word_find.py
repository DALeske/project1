# File to find a word in a sentence
sent_in = input("type a sentence:").lower()
word_in = input("What word do you want to find? ").lower()
def count_word(s,word):
    words = s.split()
    word_count = sum(1 for w in words if w==word)
    return word_count

if count_word(sent_in,word_in) >0:
    print("I found",count_word(sent_in,word_in),"occurence(s) of the word",word_in,"in your sentence")
else:
    print("I did not find",word_in,"in your sentence")
