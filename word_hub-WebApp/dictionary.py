import json
from difflib import get_close_matches

data = json.load(open('static/data.json'))
z = None

def diction(w):
    global z
    try:
        w = w.lower()
        if w in data:
            return(','.join(data[w]))
        elif w.title() in data:
            return(','.join(data[w.title()]))
        elif w.upper() in data:
            return(','.join(data[w.upper()]))
        elif w not in data:
            x = get_close_matches(w,data.keys(),n=1)[0]
            z = x
            return f'did you mean {z}, Enter Yes or No below:'
    except:
        return 'The Word does not exist'
    
def diction2(w):
    if w.lower() == 'yes':
        return(','.join(data[z]))
    else:
        return 'The Word does not exist'



