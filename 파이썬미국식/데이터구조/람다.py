wo = ['Mon', 'tue', 'wed', 'Thr', 'fri', 'sat']

def change_word(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

sample_func = lambda word: word.capitalize()

change_word(wo, sample_func)