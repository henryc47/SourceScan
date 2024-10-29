#module to detect presence of random strings in text
#uses bigram frequency as given here https://norvig.com/mayzner.html
#and a few other tricks given here https://medium.com/atlantbh/random-string-detection-1ed48de05a0e
def detect_random(lines):
    random_detected = False
    for line in lines:
        new_random = detect_random_in_line(line)
        random_detected = random_detected or new_random#will turn True if a random is detected in any of the lines
    return random_detected

#eventually add support for line by line breakdown
def detect_random_in_line(line):
    words = line.split() #break each up line into words (parts of the line separated by whitespace)
    for word in words:
        possible_random_words = []
        if is_word_random(word):
            possible_random_words = []
    return False

#test, just sees if first three letters of word are "foo"
def is_word_random(word):
    if len(word)>3:
        if word[0:2]=='foo':
            return True
    return False

def TODO_is_word_random(word):
    word = word.lower() #case is irrelevant for this sort of detection
    min_length_for_random = 4 #minimum length for a word to be considered "random"
    if len(word)<min_length_for_random:
        return False
    elif word_single_character(word): #we are suspicious of single character words
        return True
    return False


#words made up of a single character are considered to be random
def word_single_character(word):
    first_char = word[0]
    for char in word:
        if char!=first_char:
            return False
    return True
