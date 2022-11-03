from googletrans import Translator
text = input('TRADUCTOR\n\n>')
trans = Translator()
try:
    t = trans.translate(text, dest='en')
    output = t.text
except:
    output = '--No coincide--'
print(output)