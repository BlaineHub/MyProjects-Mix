from googletrans import Translator

def trans(text,dest):
    translator=Translator()
    translation = translator.translate(text=text,dest=dest)
    return translation.text
