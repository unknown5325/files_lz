import docx
import matplotlib.pyplot as plt
import pandas as pd

doc = docx.Document('lion.docx')
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text.split())



words = {}
for item in text:
    if item in words:
        words[item] += 1
    else:
        words.update({item:1})

print(text)



"""
plt.hist(words)
plt.show()
"""