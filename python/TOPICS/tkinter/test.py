from googletrans import Translator

trans = Translator()
try:
    t = trans.translate("hola", dest='en')
    output = t.text
except:
    output = '--No coincide--'
print(output)