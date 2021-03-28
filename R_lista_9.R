'Zadanie_1'
'Wczytaj dane genomes. Zbiór danych zawiera informację na temat genomów bakteryjnych.
W jego składwchodzi siedem zmiennych.
a. Organism –nazwa organizmu,
b. Group – zmienna opisująca do jakiej grupy należy bakteria,
c. size – wielkość genomu w Mbp,
d. CG – zawartość par GC w genomie,
e. habitat – środowisko jakie zamieszkuje bakteria,
f. temp.group – w jakim zakresie temperatur żyje danych organizm,
g. temperature – optymalna temperatura.'

#dane=read.csv("", sep = ';') - można aplikowac dane z internetu
# lub aplikacja przez R 
genomy = read.csv('/Users/daria/Desktop/Pakiety_Statystyczne/genomes.csv', sep=';')
print(head(genomy))

'Zadanie_2'
'Sprawdź jak oznaczone są brakujące dane w kolumnach size i gc. W przypadku 
size zamień je na średnią wielkość, natomiast w przypadku GC zamień je na NA.'



'
library(plyr)
#genomy$size = as.double(genomy$size)
head(genomy$size)
?replace
replace(genomy$size,".",NA)
replace(genomy$size, is.na(genomy$size) , mean(genomy$size, na.rm = T))
print(mean(as.complex(genomy$size)))
replace(genomy$size, NaN , mean(genomy$size))
'

library(plyr)

summary(genomy$size)
unique(genomy$size)
count(genomy$size == '.')
count(genomy$GC == '.')



genomy$size[genomy$size == '.'] <- NA
genomy$size <- as.numeric(as.character(genomy$size))
genomy$size[is.na(genomy$size)] <- round(mean(genomy$size, na.rm = T), digits = 2)

#lub
genomy$size = ifelse(genomy$size == '.', NA, genomy$size)
genomy$size = as.numeric(genomy$size)
genomy$size = ifelse(is.na(genomy$size), mean(genomy$size, na.rm = T), genomy$size)


genomy$GC[genomy$GC == 0] <- NA
#lub
genomy$GC = ifelse(genomy$GC == '0', NA, genomy$GC)


'Zadanie_3'
'Za pomocą wykresu sprawdź, czy pomiędzy zmiennymi size i gc występuje
zależność liniowa.'

x=genomy$size
y=genomy$GC
cor.test(genomy$size, genomy$GC)
plot(x,y)
cor(x,y,use="complete.obs")

scatter.smooth(x = genomy$size, y = genomy$GC, main = 'genomy a GC')

qqnorm(genomy$GC)
qqline(genomy$GC, col = 'blue')

'Zadanie_4'
'Dla wczytanych danych odpowiedz na następujące pytania
a. Jaka jest mediana zawartości par GC w genomie?
b. W jakim środowisku najczęściej żyją bakterie?
c. Ile organizmów żyjących w skrajnie niskich temperaturach („Psychrophilic”) 
jest w zbiorze danych?
d. Jaka jest minimalna i maksymalna optymalna temperatura dla bakterii?'

library(plotmath)
print(paste('mediana zawartosc par GC w genomie', median(genomy$GC, na.rm=T)))
summary(genomy$GC)

table(genomy$habitat)
which.max(table(genomy$habitat))

print(paste('Psychrophilic w niskich temperaturach',count(genomy$temp.group == 'Psychrophilic')))
sum(genomy$temp.group == 'Psychrophilic')

print(summary(genomy$temperature))
print(paste('maksymalna temp', max(genomy$temperature, na.rm = T)))
print(paste('minimalna temp', min(genomy$temperature, na.rm = T)))
print(summary(genomy$size))


'Zadanie_5'
'Za pomocą modelu liniowego sprawdź czy istnieje zależność pomiędzy
zawartością par GC, a wielkością genomu. Sformułuj hipotezy.'
#H0 nie istnieje zaleznosc pomiedzy wielkością genomu a zawartością par GC
#H1 Istnieje zależność pomiędzy wielkoscia genomu a iloscia par gc

#korelacja
cor.test(genomy$GC, genomy$size)
x=genomy$GC
y=genomy$size
plot(x,y)
?cor
cor(x,y,use="complete.obs")

#Tabelki
testglm = glm(formula = genomy$GC ~ genomy$size,family = 'poisson' , data=genomy)
summary(testglm)

testlm = lm(genomy$GC~genomy$size, data = genomy)
summary(testlm)
#p<0,05
# korzystamy z lm



'Zadanie_6'
'Sprawdź czy reszty modelu pochodzą z rozkładu normalnego.'

reszty = resid(genomy_a_GC)
shapiro.test(reszty)
#6 p-value < 0.05 - reszty modelu nie pochodzą z rozkładu normalnego.

'Zadanie_7'
'Sprawdź czy współczynniki modelu są istotne statycznie na poziomie 0.05.
Podejmij decyzję o dorzuceniu bądź braku podstaw do odrzucenia hipotezy zerowej.'
#H0 nwspolczynniki modelu sa istotne statystycznie
#H1 wspolczynniki modelu nie sa istotne statystycznie
#Model nie jest istotny statystycznie 
# odrzucamy hipotezy 0
# P > |t| - cz model jest istotny statystycznie - mniejsze niz 0.05

testlm = lm(genomy$GC~genomy$size, data = genomy)
summary(testlm)

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
# R-squared = 0.38
# Wartość dopasowania modelu wynosi pomiędzy 0,2-0,4 - jest to słabe dopasowanie

'Zadanie_8'
'Oceń dopasowanie modelu.'
testlm = lm(genomy$GC~genomy$size, data = genomy)
summary(testlm)
#lub
summary(testlm)$r.squared

#R-squared - 0,3762
# słabe dopasowanie - im bliżej 1 tym lepiej 



'Zadanie_9'
'Zinterpretuj model i zapisz jego równanie. Jaką zawartość par GC miałaby bakteria,
której wielkość genomu wynosiła by 965 Mbp?'

testlm = lm(genomy$GC~genomy$size, data = genomy)
summary(testlm)
summary(testlm)$coef

#y = 34.480511 + 4.300554*x
y = 34.480511  +4.300554*965

y





'_________'

#Q-Q plot
qqnorm(genomy$size)
qqline(genomy$size, col='red')
grid()
hist(genomy$size, col="lightblue", freq=FALSE, main = "Rozklad genomy$size")
grid()

qqnorm(genomy$GC)
qqline(genomy$GC, col = 'blue')
hist(genomy$GC, col="red", freq=FALSE, main = "Rozklad genomy$GC")
grid()