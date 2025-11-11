import docx
import matplotlib.pyplot as plt
import pandas as pd

doc = docx.Document('lion.docx')
text = ''
for paragraph in doc.paragraphs:
    text += paragraph.text

punc = '/?!.,"«»[](){}-–:;—_1234567890xiv'
for i in range(0, len(punc)) :
    if punc[i] in text : 
        text = text.replace(punc[i], ' ')
text = text.lower()
text = text.split()




words = {}
for item in text:
    if item in words:
        words[item] += 1
    else:
        words[item] = 1

wor = []
ks = []
pr = []
for key in words.keys():
    ks.append(words[key])
    wor.append(key)
    pr.append(int(words[key])/len(words)*100)





data = {
    'Слово': wor,
    'Частота встречи, раз' : ks,
    'Частота встречи в %' : pr
}

df = pd.DataFrame(data)
print(df)