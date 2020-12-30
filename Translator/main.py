import requests
from bs4 import BeautifulSoup

list = ['Arabic','German','English','Spanish','French','Hebrew','Japanese','Dutch','Polish','Portuguese','Romanian','Russian','Turkish']

print(
    'Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
tipo = input('> ')
print('Type the word you want to translate:')
lenguaje = input('> ')
print('You chose "' + tipo + '" as the language to translate "' + lenguaje + '" to.')
user_agent = 'Mozilla/5.0'

Lang = ""

url = 'https://context.reverso.net/translation/'
if tipo == 'fr':
    url = url + 'english-french/' + lenguaje
    Lang = "French"
else:
    url = url + 'french-english/' + lenguaje
    Lang = "English"

response = requests.get(url, headers={'User-Agent': user_agent})
s = BeautifulSoup(response.content, 'html.parser')

if s:
    print(response.status_code, 'OK')
    print('\nContext examples:\n')

    A_transactions = s.find_all("a", {"class": "translation"})
    A_examples = s.find_all("div", {"class": "trg ltr"})
    A_examplesOther = s.find_all("div", {"class": "src ltr"})

    words = []
    examples = []
    Other = []

    print(Lang, 'Translations:')

    for tmp in A_transactions:
        words.append(tmp.text.strip())
    for tmp in A_examples:
        examples.append(tmp.text.strip())
    for tmp in A_examplesOther:
        Other.append(tmp.text.strip())
    words = words[1:6]
    #examples = examples[:5]
    #Other = Other[:5]
    for tmp in words:
        print(tmp)
    print()
    idx = 0
    print(Lang, 'Examples:')
    for tmp in examples:
        print(Other[idx] + ":")
        print(tmp)
        print()
        idx += 1

else:
    print('No')
