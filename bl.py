from translate import Translator

tr = Translator(from_lang='en', to_lang='ru')

end_text = tr.translate('hello world')
print(end_text)