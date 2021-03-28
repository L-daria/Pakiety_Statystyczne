import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib as mp
import math
from sklearn.linear_model import LinearRegression

from matplotlib import pyplot as plt



#Lista 3 

print('Zadanie1')

genomes_nazwy = pd.read_csv('/Users/daria/Desktop/Pakiety_Statystyczne/genomes.csv', sep = ';', encoding='latin1')
print(genomes_nazwy.head())
                            

genomes_nazwy.columns=['Organism –nazwa organizmu','Group – zmienna opisujaca do jakiej grupy nalezy bakteria','size – wielkosc genomu w Mbp','CG – zawartosc par GC w genomie','habitat – srodowisko jakie zamieszkuje bakteria','temp.group – w jakim zakresie temperatur zyje dany organizm','temperature – optymalna temperatura']


print('-------------------------------------------------------------------')
print('Zadanie2')

genomy = pd.read_csv('/Users/daria/Desktop/Pakiety_Statystyczne/genomes.csv', sep = ';')

genomy.isnull().values.any()

genomy['size'] = genomy['size'].replace('.', np.nan)
genomy['size'] = genomy['size'].apply(pd.to_numeric)
genomy['size'].fillna(genomy['size'].mean(), inplace = True) 

#lub

genomy['size'] = genomy['size'].replace('.', np.nan)
genomy['size'] = genomy['size'].astype(float) #zmiana typu zmiennych
genomy[genomy.columns[2]] = genomy[genomy.columns[2]].fillna(genomy[genomy.columns[2]].mean())



genomy['GC'] = genomy['GC'].replace(0.0, np.nan)


print('-------------------------------------------------------------------')
print('Zadanie3')


dane = genomy.copy()
dane = dane[dane['GC'].notna()]
x_3 = np.array(dane['size'])
y_3 = np.array(dane['GC'])
plt.plot(x_3, y_3, 'o')
m, b = np.polyfit(x_3, y_3, 1)
plt.plot(x_3, m*x_3 + b)


#Tworzymy wykres
# szkielet
# plt.figure
# ... wypełnienie
# plt.show()

x = genomy['size']
y = genomy['GC']
plt.figure(figsize = (5,5))
plt.plot(x, y, 'ro', alpha = 0.2)
plt.xlabel('wielkosc genomy mikroorganizmu')
plt.ylabel('zawartosc par GC w genomie')
plt.title('zaleznosc pomiedzy zawartoscia par GC, a wielkoscia genomu')
print(plt.show)




print('-------------------------------------------------------------------')
print('Zadanie4')

print('to jest mediana par GC',genomy['GC'].median())


print('środowisko',genomy['habitat'].value_counts())
#lub
print('środowisko',genomy['habitat'].value_counts().idxmax())
#lub
print(genomy.groupby('habitat').size())


print('temp min i maks', genomy.describe())
#lub
print(genomy['temperature'].max())
print(genomy['temperature'].min())
#lub
print(genomy.groupby('temp.group').size())


print(len(genomy[genomy['temp.group'] == 'Psychrophilic']))
print(genomy['temp.group'].value_counts('Psychrophilic'))
#lub
print(np.sum(genomy['temp.group'] == 'Psychrophilic'))


print('-------------------------------------------------------------------')

print('Zadanie5')

#H0= nie istnieje zależnosć
#H1= istnieje zaleznosc
'''
genomy = genomy.dropna(subset = ['size', 'GC'])
x1 = genomy['GC']
x1 = sm.add_constant(x1)
y1 = genomy['size']
model = sm.OLS(y1,x1).fit()
predictions = model.predict(x1) 
print_model = model.summary()
print(print_model)
'''
#lub


# sklearn: ml, nie mamy informacji o resztach i pv
dataLinear = genomy
dataLinear = dataLinear.dropna()
x = np.array(dataLinear['size']).reshape((-1, 1)) 
y = dataLinear['GC']
regSKL = LinearRegression()
regSKL.fit(x,y)
print(f"wyraz wolny: {regSKL.intercept_}")
print(f"współczynnik beta 1: {regSKL.coef_}")
print(f"R^2: {regSKL.score(x,y)}")
genomy = dataLinear

print('-------------------------------------------------------------------')

print('Zadanie6')


y_6 = np.array(genomy['GC'])
x_6 = np.array(genomy['size'])
x_6 = sm.add_constant(x_6)
model_6 = sm.OLS(y_6, x_6)
results_6 = model_6.fit()
print(results_6.summary())
'''
#lub

genomy = genomy.dropna(subset = ['size', 'GC'])
x1 = genomy['GC']
x1 = sm.add_constant(x1)
y1 = genomy['size']
model = sm.OLS(y1,x1).fit()
predictions = model.predict(x1) 
print_model = model.summary()
print(print_model)
'''




print('-------------------------------------------------------------------')
print('Zadanie7')

#print_model = model.summary()
#print(print_model)
# Adj. R- squared - ocenia dopasowanie modelu od 0 do 1, im blizej 1 tym lepiej 
# const jeżeli wartosc x i y są zerami na jakiej wysokosci y znajduje sie model 

# std err - okresla dokladnosc - im nizszy tym lepiej - tym wyższa dokładność
# P > |t| - cz model jest istotny statystycznie - mniejsze niz 0.05

# Prob(F-statistics) - jeżeli mniejsze od 0,01, 0,05 - model jest istot. staty.

# Durbin-Watson - mówi o korelacji pomiędzy x i y, gdy jej wartość jest <1






# H0 - im bliżej wartości 1 jest współczynnik determinancji, tym wielkość genomu zależy bardziej od ilości par GC
# H1 - im bliżej wartości 0 jest współczynnik determinancji, tym wielkość genomu zależy mniej od ilości par GC

# Prob(JB) < 0.05 - reszty modelu pochodzą z rozkładu normalnego
# P>|t| < 0.05 - współczynniki modelu są istotne staytystycznie, nie odrzucamy hipotezy zerowej
# model_5.score(x, y) = 0.38092729006531045
# R-squared = 0.381
# Wartość dopasowania modelu wynosi pomiędzy 0,2-0,4 - jest to słabe dopasowanie


print('-------------------------------------------------------------------')
print('Zadanie8')

# std err wynosi 0,33 model jest raczej dobrze dopasowany



print('-------------------------------------------------------------------')
print('Zadanie9')
# GC = (const coef) + (GC coef)*X1 
# GC = (34,0841) + 4.0409 * Ilość GC (1,234)
GC = 34.0841 + 4.0409 *1.234
print(GC)




