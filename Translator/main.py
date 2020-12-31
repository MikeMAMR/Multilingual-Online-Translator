import sys
import requests
from bs4 import BeautifulSoup

list = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
        'Romanian', 'Russian', 'Turkish']

def juntar(cad, agregar):
    return cad + agregar

r = requests.session()

def translate(myLan, otherLan, word, id):
    texto = ""
    user_agent = 'Mozilla/5.0'
    url = 'https://context.reverso.net/translation/' + list[myLan - 1].lower() + '-' + list[
        otherLan - 1].lower() + '/' + word
    response = r.get(url, headers={'User-Agent': user_agent})
    s = BeautifulSoup(response.content, 'html.parser')
    if s:
        #if id == 0:
        #    texto = juntar(texto, str(response.status_code) + ' OK\n')  # print(response.status_code, 'OK')
        #    texto = juntar(texto, '\nContext examples:\n\n')  # print('\nContext examples:\n')
        A_transactions = s.find_all("a", {"class": "translation"})
        if otherLan == 1:
            A_examples = s.find_all("div", {"class": "trg rtl arabic"})
        elif otherLan == 6:
            A_examples = s.find_all("div", {"class": "trg rtl"})
        else:
            A_examples = s.find_all("div", {"class": "trg ltr"})

        A_examplesOther = s.find_all("div", {"class": "src ltr"})
        words = []
        examples = []
        Other = []
        texto = juntar(texto, list[otherLan - 1] + ' Translations:\n')  # print(Lang, 'Translations:')
        for tmp in A_transactions:
            words.append(tmp.text.strip())
        for tmp in A_examples:
            examples.append(tmp.text.strip())
        for tmp in A_examplesOther:
            Other.append(tmp.text.strip())
        # IMPRIMIR PALABRAS
        if id == 1:
            words = words[1:2]
        else:
            words = words[1:6]

        for tmp in words:
            texto = juntar(texto, tmp + '\n')  # print(tmp)
        texto = juntar(texto, '\n')  # print()
        idx = 0
        texto = juntar(texto, list[otherLan - 1] + ' Examples:\n')  # print(Lang, 'Examples:')
        for tmp in examples:
            if id == 1 and idx == 1:
                break
            texto = juntar(texto, Other[idx] + ":\n")  # print(Other[idx] + ":")
            texto = juntar(texto, tmp + '\n')  # print(tmp)
            texto = juntar(texto, '\n')  # print()
            idx += 1
    else:
        texto = 'No'  # print('No')
    return texto


"""print(Hello, you're welcome to the translator. Translator supports: 
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
13. Turkish)"""

args = sys.argv

#print('Type the number of your language:')
yourLeng = list.index(args[1].capitalize()) + 1 #int(input('> '))
#print('Type the number of language you want to translate to: ')
lenguaje = 0
if args[2] != 'all':
    lenguaje =  list.index(args[2].capitalize()) + 1 #int(input('> '))
#print('Type the word you want to translate:')
tipo =  args[3]  #input('> ')
Lang = list[lenguaje - 1]

file2 = open(f'{tipo}.txt', 'w', encoding='utf-8')

if lenguaje == 0:
    tmp = ""
    for idm in list:
        if idm != list[yourLeng - 1]:
            # print(list.index(idm))
            tmp = tmp + translate(yourLeng, list.index(idm) + 1, tipo, 1) + '\n'
    print(tmp)
    file2.write(tmp)
else:
    tmp = translate(yourLeng, lenguaje, tipo, 0)
    print(tmp)
    file2.write(tmp)

file2.close()
