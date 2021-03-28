import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib as mp
import math
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from matplotlib import pyplot as plt

uni = pd.read_csv('/Users/daria/Desktop/Pakiety_Statystyczne/uni.csv')
print(uni.isnull().sum()))
print(uni.info())
print(uni.shape)

#-----------------------------------------------------------------------------
#                                   Zadanie 2a
#https://www.statisticshowto.com/probability-and-statistics/f-statistic-value-test/

#0LS  tyczy sie wielkości liniowych

#H0 - nie istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a wynikiem egzaminu
# H1 - istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a wynikiem egzaminu

x = np.array(uni['gre'])
y = np.array(uni['admit'])
x = sm.add_constant(x)
model = sm.GLM(y, x, family=sm.families.Binomial())
results = model.fit()
print(results.summary())

#gdy p < 5% to odrzucamy H0
'''
no. Observations - ilość obserwacji
Df Residuals - ilość stopni swobody
Df Model - ilu modeli zostało użytych 

Tabelka na dole
coef (od coefficient)- jest to współczynnik znajdujący się przy x
std err (standard efficient error - błędy do współczynników po lewej stronie
z - statystyka z
P > |z| - przyjęcie lub odrzucenie hipotezy zerowej
przeważnie alfa 0.05 
gdy P > |z| < 0.05 to odrzucenie H0
[0.025     0,975] - przedziały ufności współczynnika kierunkowego -  określa gdzie powinna znaleść się wielkosc estymatora. Określa w jakim przedziale znajduje się błąd.
         


'''



#-----------------------------------------------------------------------------
#                                   Zadanie 2b


#2.2 H0 - nie istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a średnią ocen
# H1 - istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a średnią ocen

'''

x = np.array(uni['gpa'])
y = np.array(uni['admit'])
x = sm.add_constant(x)
model = sm.GLM(y, x, family=sm.families.Binomial())
results = model.fit()
print(results.summary())

'''
'''
określa które zmienna mają wpływ na dostanie się na studia, jeżeli wieksze od
0.05 to wielkość nie ma wpływu na dostanie się na studia 
'''

#-----------------------------------------------------------------------------
#                                   Zadanie 2c

#2.3 H0 - nie istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a pozycją w rankingu
# H1 - istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a pozycją w rankingu

x = np.array(uni['rank'])
y = np.array(uni['admit'])
x = sm.add_constant(x)
model = sm.GLM(y, x, family=sm.families.Binomial())
results = model.fit()
print(results.summary())

#gdy p < 5% to odrzucamy H0
# 0,038 < 0,05
# z 
# Dolna i górna granica wystąpienia estymatora
# 0,063 znajduje się w granicy - dolna granica  0,037, górna granica - 1,237

#-----------------------------------------------------------------------------
#Zadanie2d


'''
#                                   Zadanie 2.4 
H0 - nie istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a wynikiem egzaminu,
# średnią ocen oraz pozycją w rankingu
# H1 - istnieje logistyczna zależność pomiędzy przyjęciem na uczelnię a wynikiem egzaminu,
# średnią ocen oraz pozycją w rankingu





x1 = uni[['gre']]
x1 = sm.add_constant(x1)
x2 = uni[['gpa']]
x2 = sm.add_constant(x2)
x3 = uni[['rank']]
x3 = sm.add_constant(x3)
x4 = uni[['gre','gpa','rank']]
y = uni['admit']
model = sm.GLM(y, x4, family=sm.families.Binomial())
results = model.fit()
print(results.summary())


'''
#-----------------------------------------------------------------------------
#                                   Zadanie3
#Znajdź informację o kryterium informacyjnym Akaikego oraz Bayesowskim kryterium
#informacyjne. Jak należy je interpretować.
'''
AIC	The Akaike Information Criterion. Adjusts the log-likelihood based on the number of observations and the complexity of the model.
BIC	The Bayesian Information Criterion. Similar to the AIC, but has a higher penalty for models with more parameters.

Akaike zaproponował, aby wybierać ten model dla którego najmniejsza jest wartość:
z wzoru

https://pl.wikipedia.org/wiki/Kryterium_informacyjne_Akaikego



BIC - znajduje się w przedziale 0 - +10; im większy tym model lepiej dopasowany +10 

https://en.wikipedia.org/wiki/Bayesian_information_criterion

'''
#https://www.statsmodels.org/stable/regression.html
'''
#3.1 Kryterium informacyjnym Akaikego - Kryterium informacyjne Akaike jest powszechnie używane do porównywania
# modeli statystycznych. Nie dostarcza ono miary dopasowania modelu do danych, ale może być użyteczne
# do pomiaru i testu względnej mocy predykcyjnej testowanych modeli. Dany zestaw modeli statystycznych
# może zwracać różne miary AIC, ale pożądany i lepszy jest ten z wyraźnie mniejszą miarą AIC.
# Na podstawie tej miary możemy wybrać najbardziej oszczędny i informatywny model statystyczny.

#3.2 Bayesowskie kryterium informacyjne - jeden ze wskaźników dopasowania modelu.
# Najlepszym modelem jest ten dla którego wartość kryterium informacyjnego jest najniższa.

#3+ BIC oraz AIC są najpowszechniej wykorzystywanymi kryteriami informacyjnymi,
#a więc metodami porównywania modeli dla zmiennej zależnej, aby dokonać selekcji najlepszego modelu.
# Zgodnie z przyjętą konwencją, najlepszym modelem jest ten dla którego wartość kryterium informacyjnego
# jest najniższa.
'''



#-----------------------------------------------------------------------------
#                                   Zadanie4
#Co możesz powiedzieć o dopasowaniach modeli, na podstawie AIC i BIC, który z nich jest najlepszy?
'''
AIC - Kryterium informacyjne Akaikego - Akaike Information Criterion- 
zaproponowane przez Hirotugu Akaikego kryterium wyboru pomiędzy modelami statystycznymi o różnej liczbie predyktorów. Jest to jeden ze wskaźników dopasowania modelu. Na ogół model o większej liczbie predyktorów daje dokładniejsze przewidywania, jednak ma też większą skłonność do przeuczenia.

Przyuczenie
różne, stosowane w statystyce nazwy tego samego zjawiska, zachodzącego gdy model statystyczny ma zbyt dużo parametrów w stosunku do rozmiaru próby, na podstawie której był konstruowany. Absurdalne i fałszywe modele mogą świetnie pasować do danych uczących gdy model ma wystarczającą złożoność, jednak będą dawały gorsze wyniki, gdy zastosujemy je do danych, z którymi się nie zetknęły podczas uczenia.


BIC - When fitting models, it is possible to increase the likelihood by adding parameters, but doing so may result in overfitting. Both BIC and AIC attempt to resolve this problem by introducing a penalty term for the number of parameters in the model; the penalty term is larger in BIC than in AIC.




x = np.array(uni['rank'])
y = np.array(uni['admit'])
x = sm.add_constant(x)
model_1 = sm.GLM(y, x,family=sm.families.Binomial())
results_1 = model_1.fit()



x = np.array(uni['gre'])
y = np.array(uni['admit'])
x = sm.add_constant(x)
model = sm.GLM(y, x, family=sm.families.Binomial())
results = model.fit()

print('AIC_1',results_1.aic)
print('BIC_1',results_1.bic)

print('AIC_2',results.aic)
print('BIC_2',results.bic)

#drugi model względem AIC jest lepszy od pierwszego - wyższa wartość
# 
'''






