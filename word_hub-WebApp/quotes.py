import glob
from pathlib import Path
import random


def get_quote(feel):
    feel = feel.lower()
    available_feelings = glob.glob('static/quotes/*.txt')
    available_feelings = [ Path(filename).stem for filename in 
                            available_feelings]
    if feel in available_feelings:
        with open(f"static/quotes/{feel}.txt",encoding='utf-8') as file:
            quotes = file.readlines()
        return random.choice(quotes)
    else:
        return 'Opps! Pick Another Feeling'
