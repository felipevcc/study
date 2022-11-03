from translate import Translator

def traductor():
    print('\nTRADUCTOR')
    lang = input('\nEscoge: \n[1]: English -> Spanish\n[2]: Spanish -> English\n')
    if lang == '1':
        text = input('Write: ')
        translator = Translator(to_lang='es', from_lang='en')
        x = translator.translate(text)
        print(x)
    elif lang == '2':
        text = input('Write: ')
        translator = Translator(to_lang='en', from_lang='es')
        x = translator.translate(text)
        print(x)
    else:
        print('No coincide\n-------------------------')
        return traductor()
    def decision():
        pregunta = input('\n¿Desea salir?\n[s/n]')
        if pregunta == 's':
            print('Bye')
        elif pregunta == 'n':
            print('\n-------------------------')
            return traductor()
        else:
            print('No coincide')
            return decision()
    decision()
traductor()