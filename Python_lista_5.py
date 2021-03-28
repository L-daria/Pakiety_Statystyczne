import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib as mp
import math
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt



from matplotlib import pyplot as plt

genomy = pd.read_csv('/Users/daria/Desktop/Pakiety_Statystyczne/genomes.csv', sep = ';')

#Liczenie brakujących wartości 
len(genomy[genomy['size'] == '.'])
len(genomy[genomy['GC'] == 0.0])

print(genomy.isnull().sum())
print(genomy.info())
print(genomy.shape)


print('-------------------------------------------------------------------')
print('Zadanie 1')



genomy.isnull().values.any()

genomy['size'] = genomy['size'].replace('.', np.nan)
genomy['size'] = genomy['size'].apply(pd.to_numeric)
genomy['size'].fillna(genomy['size'].mean(), inplace = True) 

#lub
'''
genomy['size'] = genomy['size'].replace('.', np.nan)
genomy['size'] = genomy['size'].astype(float) #zmiana typu zmiennych
genomy[genomy.columns[2]] = genomy[genomy.columns[2]].fillna(genomy[genomy.columns[2]].mean())
'''

genomy['GC'] = genomy['GC'].replace(0, np.NaN)
genomy.dropna(subset = ["GC"], inplace=True)
# notna za pomocą pętli?????






print('-------------------------------------------------------------------')
print('Zadanie_2')
# Usunąć wielkości nan
# Należy zakodowanie naszą grupę jako różne wartości ciągłe:
    
# genomy['temperature'] = genomy['temperature'].astype('category')
#genomy.dropna(subset = ['temperature'], inplace=True)


print('-------------------------------------------------------------------')
print('Zadanie_3')
# Czy GC i Size pochodzą z rozkładu normalnego ??


normalVar = pd.DataFrame(genomy['GC'])
normalVar.columns = ['GC']
plt.title("GC")   
sns.distplot(normalVar)
print(plt.show())



normalVar = pd.DataFrame(genomy['size'])
normalVar.columns = ['size']
sns.distplot(normalVar)
plt.title("SIZE")   
print(plt.show())




import numpy as np 
import statsmodels.api as sm 
import pylab as py

sm.qqplot(genomy['GC'], fit = True,line='45') 
plt.title('GC')
print(py.show())
# Lub 
wykres_GC = genomy['GC'].plot.kde()
print(wykres_GC)


sm.qqplot(genomy['size'], fit = True,line='45') 
py.title('SIZE')
print(py.show())
# Lub
wykres_size = genomy['size'].plot.kde()
print(wykres_size)



from scipy.stats import normaltest
stats, p = normaltest(genomy['GC'])
print(stats, p)

stats, p = normaltest(genomy['size'])
print(stats, p)

'''

print('-------------------------------------------------------------------')
print('Zadanie_4')

#Test D’Agostino–Pearson
#W przypadku kiedy wartość p jest mniejsza/równa od 5 %, odrzucamy naszą hipotezę. Jeżeli wartość p jest większa od 5%, to prawdopodobnie zmienna ma wartości pochodzące z rozkładu normalnego

from scipy.stats import normaltest
stats, p = normaltest(genomy['GC'])
print(stats, p)
if p > 0.05:
    print ("Rozkład GC wygląda na normalny")
else:
    print('Rozkład GC nie wygląda na rozkład normlany')
    
    
stats, p = normaltest(genomy['size'])
print(stats, p)    
if p > 0.05:
    print ("Rozkład size wygląda na normalny")
else:
    print('Rozkład size nie wygląda na rozkład normlany')

# Lub test Shapiro-wilka

from scipy import stats

# H0: brak różnic pomiędzy zakładanym rozkładem a rozkładem wartości - wartości pochodzą z rozkładu normalnego
# H1: istnieją różnice pomiędzy rozkładami - wartości nie pochodzą z rozkładu normalnego

rozmiar = np.array(genomy['size'])
test_shapiro_size = stats.shapiro(rozmiar)
print(test_shapiro_size)

if test_shapiro_size.pvalue > 0.05:
    print('Przyjmujemy hipotezę zerową')
else:
    print('Odrzucamy hipotezę zerową, przyjmujemy hipotezę alternatywną')


pary_GC = np.array(genomy['GC'])
test_shapiro_GC = stats.shapiro(pary_GC)
print(test_shapiro_GC)

if test_shapiro_GC.pvalue > 0.05:
    print('Przyjmujemy hipotezę zerową')
else:
    print('Odrzucamy hipotezę zerową, przyjmujemy hipotezę alternatywną')


print('-------------------------------------------------------------------')
print('Zadanie_5')

#5.1 Należy przekształcić dane:
# - przekształcenie arcus sinus - przy danych mających rozkład dwumianowy wyrażanych w procentach
# - usunięcie zmiennych odstających - przy występowaniu daleko odstających wartości
# - zlogarytmowanie wartości - najczęściej kiedy wraz ze wzrostem wartości średniej zwiększa się wariancja
# (a tym samym odchylenie standardowe), czyli występuje korelacja między średnią a wariancją
# - potęgowanie
# - pierwiatkowanie
# - transformacja Boxa-Coxa - przy rozkładach asymetrycznych
# - standaryzacja - przy sprowadzeniu wartości do wspólnej skali


#5.2 Należy wtedy zastosować testy nieparametryczne:
# - test Manna-Whitney’a - odpowiednik testu t Studenta dla prób niezależnych,
# - test Kruskala-Wallisa - odpowiednik jednoczynnikowej analizy wariancji (ANOVA) dla prób niezależnych,
# - test Wilcoxona – odpowiednik testu t Studenta dla prób zależnych,
# - test Friedmana – odpowiednik jednoczynnikowej analizy wariancji (ANOVA) dla prób zależnych,
# - korelacje nieparametryczne – rho Spearmana i tau b Kendalla,
# - test Chi kwadrat zgodności rozkładu lub test Chi kwadrat niezależności


print('-------------------------------------------------------------------')
print('Zadanie_6')
from statsmodels.formula.api import ols
from statsmodels.stats.api import anova_lm

#6 H0: średnia zawartość par GC w genomie nie wpływa na miejsce bytowania organizmów
# H1: średnia zawartość par GC w genomie  wpływa na miejsce bytowania organizmów

ANOVA_model = ols('GC ~ habitat', data = genomy)
ANOVA_results = ANOVA_model.fit()


ANOVA_table = anova_lm(ANOVA_results, type = 1)
print(ANOVA_table)

#6 PR(>F) < 0.05 - odrzucamy hipotezę zerową, przyjmujemy hipotezę alternatywną

# później test post hoc 



print('-------------------------------------------------------------------')
print('Zadanie_7')

genomy = genomy.rename(columns = {'temp.group': 'temp_group'})
print(genomy)



print('-------------------------------------------------------------------')
print('Zadanie_8')
# H0 średniepary gc nie mają wplywu 
# H1 mają wpływ 

ANOVA_model_bez_interakcji = ols('GC ~ habitat+temp_group', data = genomy)
ANOVA_results_bez_interakcji = ANOVA_model_bez_interakcji.fit()
print(ANOVA_results_bez_interakcji.summary())

ANOVA_table_bez_interakcji = anova_lm(ANOVA_results_bez_interakcji, type = 1)
print(ANOVA_table_bez_interakcji)


ANOVA_model_interakcja = ols('GC ~ habitat*temp_group', data = genomy)
ANOVA_results_interakcja = ANOVA_model_interakcja.fit()
print(ANOVA_results_interakcja.summary())

ANOVA_table_interakcja = anova_lm(ANOVA_results_interakcja, type = 1)
print(ANOVA_table_interakcja)
'''