# A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with
# the word "APPLE", you can add an "A" and anagram to get "APPEAL".
#
# Given a dictionary of words and an input word, create a function that returns all valid step words.
from Step_Word import step_word

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dictionary = ['appeal', 'appel', 'appple', 'appplle', 'bapple', 'ba']
    word = 'apple'
    print(f"The step words of {word} are: ")
    step_words = step_word(word, dictionary)
    if len(step_words) == 0:
        print('no step words')
    else:
        for w in step_words:
            print(w)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
