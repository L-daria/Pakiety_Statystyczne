import pandas as pd
import numpy as np
import random
import datetime
#Lista 2 

print('Zadanie1')
A = np.array([[4,5,8],[-7,1,0],[1,1,1]])
B = np.ones((3,3))
C = np.zeros((3,3))
D = np.array([[0.5,0,0],[0,(-1),0],[0,0,3]])

print(A)
print(B)
print(C)
print(D)

diagonal = np.array([0.5,-1,3])
D = np.diag(diagonal)
print(D)


print('-------------------------------------------------------------------')
print('Zadanie2')


print(A.transpose()) #transpozycja
print(A.dot(B)-D) #działania na macierzach
print(np.linalg.inv(D)) #do potęgi 
print(np.linalg.det(D))
print(np.linalg.solve(A,D))  #równanie liniowe


print('-------------------------------------------------------------------')
print('Zadanie3')

print(np.random.randn(5,4))
macierz= np.random.randn(5,4)

print('średnia',np.mean(macierz))
print('suma',np.sum(macierz))
print('minimum',np.min(macierz))
print('maksimum',np.max(macierz))

print(np.where(macierz > 0, 2, -2))


print('-------------------------------------------------------------------')
print('Zadanie4')

start = datetime.datetime.now()
sample1 = np.random.normal(10000, 0 ,1)
koniec = datetime.datetime.now()
print('to jest czas random',koniec - start)

start= datetime.datetime.now()
sample2 = [random.normalvariate(0,1) for i in range(10000)]
koniec = datetime.datetime.now()
print('to jest czas normalvariate', koniec - start)

#lub
#N = 100000
#a = %timeit sample1 = np.random.normal(N,0,1)
#b = %timeit sample2 = [random.normalvariate(0, 1) for i in range(N)]



print('-------------------------------------------------------------------')

print('Zadanie5')
#dataframes have a top level and a column name, when series have only top level






print('-------------------------------------------------------------------')

print('Zadanie6')

series = pd.Series({'a':'1','b':'0.4','c':'9','d':'9','e':'0','f':'2.5','g':'5.6'})
print(series)
print(series[['a', 'g', 'f']])


print('-------------------------------------------------------------------')
print('Zadanie7')

data = {'miasto':['Gdynia','Wrocław', 'Radom', 'Wrocław', 'Warszawa', 'Warszawa', 'Gdynia', 'Wrocław', 'Radom', 'Wrocław', 'Warszawa', 'Warszawa'],'rok':[1989, 1990, 1995, 1998, 2000, 2001, 1989, 1990, 1995, 1998, 2020, 2001],'freq':[1.5,3.5,7.1,4.5,None,None,2.3,3.1,1.1,4.5,5.5,6.7]}
lista = pd.DataFrame(data)
print(pd.DataFrame(data,index=[1,2,3,4,5,6,7,8,9,10,11,12]))
print(data['freq'])
print(lista.loc[11])

# można też
# Dict = []
# Dict['miasto] = ['Gdynia','Wrocław', 'Radom', 'Wrocław', 'Warszawa', 'Warszawa', 'Gdynia', 'Wrocław', 'Radom', 'Wrocław', 'Warszawa', 'Warszawa']
# Dict['rok'] = [1989, 1990, 1995, 1998, 2000, 2001, 1989, 1990, 1995, 1998, 2020, 2001]
# Dict['freq'] = [1.5,3.5,7.1,4.5,None,None,2.3,3.1,1.1,4.5,5.5,6.7]

print('-------------------------------------------------------------------')
print('Zadanie8')

anemia = pd.read_csv('/Users/daria/Desktop/anemia.csv',sep = ';')

anemia['Sex'].replace({'F':1,'M':0},inplace = True)
anemia['Sex'].replace['F':0]
anemia['Sex'].replace['M':1]

print(anemia['City'].value_counts())
Dane3['City']=

anemia['City'] = np.where(anemia['City']== '.', 'NA', anemia['City'])
anemia['City'] = np.where(anemia['City']== '0', 'NA', anemia['City'])
anemia['City'] = np.where(anemia['City']== '-999999', 'NA', anemia['City'])
anemia['City'] = np.where(anemia['City']== '-9', 'NA', anemia['City'])


print(pd.set_option('display.max_rows',110))
print(anemia['Hemoglobin'].value_counts())

print(anemia.Hemoglobin)



print('-------------------------------------------------------------------')
print('Zadanie9')

print(anemia.info())
anemia.describe()
print(anemia.transpoze())


print('-------------------------------------------------------------------')
print('Zadanie10')

print(anemia[(anemia['City'] == 'Warszawa') & (anemia['age'] >= 100)]
print(anemia['age'].max())
      
print(anemia.loc[anemia['YOB']<1920])
print(anemia.loc[anemia['age']>100])
