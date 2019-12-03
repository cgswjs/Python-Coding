import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        #close matches will be sorted in decending order by sensitivity ratio
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn[0].upper() == "Y":  
            #output the highest sensitivity ratio if user confirm
            return data[get_close_matches(w, data.keys())[0]]
        elif yn[0].upper() == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)

i=0;
if type(output) == list:
    for item in output:
        i+=1
        print('Definition{}: {}'.format(i, item.title()))
else:
    print(output)


