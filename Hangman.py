import time
import pandas as pd
import random
import requests


def word_generator():  # ***NEED TO PRINT WORD WITHOUT HEADER***
    # so needed to find the file path of the csv. Done this by searching
    # up the document in windows search bar and copying the full file path
    # when you right click
    csv = pd.read_csv(r"C:\Users\Slurp God\Documents\dictionary.csv",
                      delimiter=',', names=['words list', 'extra', 'definition'])
    see = csv.sample()[['words list']]
    word = see.to_string(header=False, index=False)
    s = str(word.strip())
    # random.shuffle returns words rather than single elements like .choice does
    return s
    # A delimiter is one or more characters that separate text strings.
    # Common delimiters are commas (,), semicolon (;), quotes ( ", ' ),
    # braces ({}), pipes (|), or slashes ( / \ ).
    # hen a program stores sequential or tabular data,
    # it delimits each item of data with a predefined character.
    # For example, in the data "john|doe," a vertical bar (the pipe character, |)
    # delimits the two data items john and doe. When a script or program reads the
    # data and encounters a vertical bar, it knows that one data item has ended,
    # and another begins
    # NB: ****CSV=COMMA SEPARATED VALUES, SO USED COMMA AS THE DELIMITER
    # (you can use semi colon) but need to change regional settings
    # as in excel comma is default separator


word_generator()


# implement in the dictionary if they get it wrong

def define(word):
    app_id = "b0da1d3b"
    app_key = "4ce85c910382cf246a26706aeaa8b8aa"
    language = "en-us"
    endpoint = 'entries'
    word_id = '{}'.format(word)
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + '/' + language + '/' + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    data = r.json()
    result = data['results'][0]['lexicalEntries']
    result_list = []
    for subcategory in result:
        entries = subcategory['entries']
        for e in entries:
            senses = e['senses']
            for s in senses:
                d = s['definitions']
                for defines in d:
                    definition = defines.capitalize()
                    result_list.append(definition)

    return word,  " \n".join(map(str, result_list))


dict1 = {}


def hangman(words):
    first = list(words)
    words = str(words)
    count = len(words) + 3
    lines = []
    for i in words:
        lines.append('_')
        # this creates an underscore for every character in words

    print('It is a', len(words), 'letter word\n',
          'You have', count, 'guesses!')
    time.sleep(1)
    print('The first word is: ', first[0])
    # word[0] represents the first character in the variable word
    while count > 0:
        # this is a loop within a loop so it is running 10 times in total
        # had to put the if statement in the for loop as it was checking the outer loop
        # before the inner loop, which by this time had already gone below zero
        # because the word length is 5. It was going to -2 because 8-10=-2
        # (limit was set at 8 for that word-'hello')
        for i in words:
            count -= 1
            time.sleep(1)
            answer = input('please input a letter ')
            if count == 0:
                # this stops program if limit was reached
                print('You have failed. The word was:')
                try:
                    print(words)
                    print(define(word_generator()))
                    break
                    # this is an issue seek help

                except:
                    print(words)

                    break
            elif answer == '':
                print('This is incorrect. You have ', count, ' goes left')
            elif answer == '{}'.format(answer) in words:
                dict1.setdefault(answer, 0)
                dict1[answer] = dict1[answer] + 1
                # this adds the correct character into a dictionary to check if there are any duplicates, as if the
                # value in the dictionary is more than 1 then they have entered that character more than once
                for k, v in dict1.items():
                    if dict1[answer] > 1:
                        print('No duplicates! You have ', count, 'goes left')
                    else:
                        for c in range(0, len(words)):
                            # this basically loops through all of the characters in the word, (in range the length of
                            # the word) the character place for which c is equal to the answer, otherwise it will
                            # turn the whole of the list lines into one character (e.g. from h_____ to hhhhh)
                            # because we appended lines using a for loop of words,
                            # we can make lines[c] now be changed to
                            # the answer because the 'i' in the for loop of lines has the same index as the
                            # 'c' in the for loop of len(word)
                            if words[c] == answer:
                                lines[c] = answer
                        print('\n Well done! You have ', count, 'goes left!')
                        hangwords = ''.join(map(str, lines))
                # this turns the list lines with the new character into a string
                        print(hangwords)
                if hangwords == words:
                    print('You have won! You had', count, 'goes left!')
                    return hangwords
            else:
                print('This is incorrect! You have', count, 'goes left \n', hangwords)


hangman(word_generator())
