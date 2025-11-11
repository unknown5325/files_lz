import docx  #импортируем библиотеки
import matplotlib.pyplot as plt  #импортируем библиотеки
import pandas as pd  #импортируем библиотеки

doc = docx.Document('lion.docx')  #файл docx
text = ''  #создаем пустую строку
for paragraph in doc.paragraphs:  #добавляем параграфы в нашу строку
    text += paragraph.text

punc = '/?!.,"«»[](){}-–:;—_1234567890xiv'  #убираем лишние символы
for i in range(0, len(punc)) :
    if punc[i] in text : 
        text = text.replace(punc[i], ' ')
text = text.lower()
text = text.split()




words = {}  #создаем словарь
for item in text:
    if item in words:
        words[item] += 1
    else:
        words[item] = 1

wor = []
ks = []
pr = []
for key in words.keys():  #проверка по ключу
    ks.append(words[key])  #столбик с ключами
    wor.append(key)  #столбик со словами
    pr.append(int(words[key])/len(words)*100)  #столбик со значениями





data = {  #создаем таблицу
    'Слово': wor,
    'Частота встречи, раз' : ks,
    'Частота встречи в %' : pr
}

df = pd.DataFrame(data)  #создаем именно таблицу
print(df)  #выводим таблицу




doc = docx.Document('lion.docx')  #файл docx
tex = ''
for paragraph in doc.paragraphs:  #добавляем параграфы в нашу строку
    tex += paragraph.text

punc = '/?!.,"«»[](){}-–:;—_1234567890xiv'  #убираем лишиние символы
for i in range(0, len(punc)) :
    if punc[i] in tex : 
        tex = tex.replace(punc[i], ' ')
tex = tex.lower()
chlist = [] 
for c in tex:   #добавляем в наш пусток ссписок chlist все буквы
    chlist.append(c)

ch = {}  #создаем пустой словарь для дальнейшего добавления туда значений и ключа
for item in chlist:
    if item in ch:
        ch[item] += 1
    else:
        ch[item] = 1



val = []
nuv = []
for key in ch.keys():  #подбираем значения для графика
    nuv.append(ch[key])
    val.append(key)

plt.bar(val, nuv)  #создаем график


plt.xlabel("буквы")  #называем оси
plt.ylabel("Количество")  #называем оси
plt.title("Гистограмма количества букв")  #называем график


plt.show()  #график
