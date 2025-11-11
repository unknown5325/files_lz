import matplotlib.pyplot as plt  #импортируем библиотеки
import pandas as pd  #импортируем библиотеки


table = pd.read_parquet('titanic.parquet')  #читаем файл .parquet
table.to_csv('titanic.csv')
df = pd.read_csv('titanic.csv')  #загружаем данные
a = df.groupby(['Не выжило', 'Выжило']).size().unstack(fill_value=0)  #именуем колонки
surv = a.div(a.sum(axis=1), axis=0) * 100  #считаем проценты по строкам
surv.plot(kind='bar', stacked=True)  #строим гистограмму

plt.title('Выживаемость пассажиров от класса')  #настройки графика
plt.xlabel('Класс') 
plt.ylabel('% выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()


plt.show()  #выводим график