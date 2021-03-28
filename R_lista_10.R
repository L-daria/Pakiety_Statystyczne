

# Linki -------------------------------------------------------------------


#https://www.scribbr.com/statistics/anova-in-r/
#https://www.guru99.com/r-anova-tutorial.html
#http://www.sthda.com/english/wiki/one-way-anova-test-in-r
#https://cran.r-project.org/doc/contrib/Komsta-Wprowadzenie.pdf

# Zadanie 1 ---------------------------------------------------------------


'Wczytaj oraz przygotuj do dalszych analiz dane genomes.csv.'
#import genomes za pomocą import Dataset
library(plyr)
count(genomes$size == '.')
unique(genomes$size)
count(genomes$GC == 0.0)
unique(genomes$GC)

genomes$size[genomes$size == '.'] <- NA
genomes$size <- as.numeric(as.character(genomes$size))
genomes$size[is.na(genomes$size)] <- round(mean(genomes$size, na.rm = T), digits = 2)

genomes$GC[genomes$GC == 0] <- NA

# Zadanie 2 ---------------------------------------------------------------


'Skonstruuj trzy modele analizy wariacji
1) średnią wartość par GC względem miejsca bytowania mikroorganizmów.
2) średnią wartość par GC względem miejsca bytowania mikroorganizmów oraz
ich grupą bytowania, nie zakładając interakcji pomiędzy zmiennymi.
3) średnią wartość par GC względem miejsca bytowania mikroorganizmów oraz
ich grupą bytowania, zakładając interakcje pomiędzy zmiennymi.'

'1) średnią wartość par GC względem miejsca bytowania mikroorganizmów.'
#H0 nie ma zależności pomiędzy średnią wartością par GC a względem bytowania mikroorganizmow
#H1 jest zależność pomiędzy średnią wartością par GC a względem bytowania mikroorganizmów
a1 = aov(formula = GC~habitat, data = genomes)
summary(a1)

# Pr(>F) = 1.21e-10 
# Porównujemy otrzymaną wartość p z przyjętym poziomem istotności. Ponieważ p =
#0,000155 < 0,05, więc mamy podstawy do odrzucenia hipotezy zerowej. 

'2) średnią wartość par GC względem miejsca bytowania mikroorganizmów oraz
ich grupą bytowania, nie zakładając interakcji pomiędzy zmiennymi.'
#H0 nie ma zależności pomiędzy średnią wartoscią par GC a miejscem bytowana mikoorganizmow lub ich gr. bytowania
#H1 jest zleznosc omiedzy srednia wartoscia par gc a miejscem bytownia mikroorganizmow lub ich gr. bytowania 
a2 = aov(GC ~ habitat+temp.group, data = genomes)
summary(a2)
# PR(>F) dla obu przypadków jest mniejsze od 0.05 dlatego w obu przypadkach przymujemy H1



'3) średnią wartość par GC względem miejsca bytowania mikroorganizmów oraz
ich grupą bytowania, zakładając interakcje pomiędzy zmiennymi.'
#H0 nie ma zaleznosci miedzy srednia wartoscia par gc a miejscem bytowania mikroogranizmow oraz ich gr bytowania
#H1 jest zaleznosc miedzy srednia wartocia par gc a miejscem bytowania mikroorganizmow oraz ich gr bytowania 

a3 = aov(GC ~ habitat*temp.group, data = genomes)
summary(a3)
#lub
a3 = aov(GC ~ habitat+temp.group+habitat:temp.group, data = genomes)
summary(a3)
# Pr(>F) = 0.8957 --- jest wieksze niż 0.05 dlatego przyjmujemy H0



# Zadanie 3 ---------------------------------------------------------------


'Dla modeli, które wykażą istotne różnice pomiędzy grupami, przeprowadź test post-
hoc'

Ta1 = TukeyHSD(aov(formula = GC~habitat, data = genomes))
Ta1
plot(Ta1)

Ta2 = TukeyHSD(aov(GC ~ habitat+temp.group, data = genomes))
Ta2
plot(Ta2)

Ta3 = TukeyHSD(aov(GC ~ habitat*temp.group, data = genomes))
#lub
Ta3 = TukeyHSD(a3)
Ta3
plot(aov(GC ~ habitat+temp.group+habitat:temp.group, data = genomes))

#lub oneway.test

# Zadanie 4 ---------------------------------------------------------------


'Dla wszystkich stworzonych modeli, sprawdź czy:
1) reszty pochodzą z rozkładu normalnego.'
#H0 - reszty pochodza z rozkladu normalnego
#H1 - reszty nie pochodza z rozkladu normalnego 

shapiro.test(lm(GC~habitat,data =genomes)$residuals)  
shapiro.test(lm(GC~habitat+group, data = genomes)$residuals)
shapiro.test(lm(GC~habitat+group+habitat:group, data = genomes)$residuals)



'2) między grupami występuje jednorodność wariancji.'
# H0 - pomiedzy grupami wystepuje jednorodnoczsc wariancji
# H1 - pomiedzy grupami nie wystepuje jednorodnosc wariancji

#var.test(dane,dane2) # czy jest jednorodność wariancji?

bartlett.test(genomes$GC~genomes$habitat)
bartlett.test(genomes$GC~genomes$habitat+genomes$group)







