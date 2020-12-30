import requests
from bs4 import BeautifulSoup

list = ['Arabic','German','English','Spanish','French','Hebrew','Japanese','Dutch','Polish','Portuguese','Romanian','Russian','Turkish']
print("""Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish""")

print('Type the number of your language:')
yourLeng = int(input('> '))
print('Type the number of language you want to translate to: ')
lenguaje = int(input('> '))
print('Type the word you want to translate:')
tipo = input('> ')

user_agent = 'Mozilla/5.0'

Lang = list[lenguaje - 1]

url = 'https://context.reverso.net/translation/' + list[yourLeng - 1].lower() + '-' + list[lenguaje - 1].lower() + '/'+tipo
#print(url)
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
