# Code to count the vowels in the sentence
sent_in = input("type a sentence:")
def count_vowels(x):
    vowels = 'aieouAEIOU'
    vow_count = sum(1 for char in x if char in vowels)
    return vow_count
print("There are",count_vowels(sent_in),"vowels in your sentence")