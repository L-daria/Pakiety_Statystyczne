"Dane są dwa wektory: 
A: {1,1,0,0,0,1} 
B: {2,1,0,2,0,1} 
Użyj funkcji ifelse by sprawdzić czy każdy element z wektora A i B jest równy 1. Użyj  zapisu skrótowego, aby wygenerować wektor. "
?ifelse
A <- c(1,1,0,0,0,1)
B <- c(2,1,0,2,0,1)
ifelse(A == 1 & B ==1, 'tak', 'nie')
ifelse(mean(A) == 1 & mean(B) == 1, 'tak', 'nie')
ifelse(B == 1, 'tak', 'nie')
ifelse(sd(A) == 0 & sd(B) == 0, 'tak', 'nie') #odchylenie standardowe

'Napisz pętlę for, która przyjmuje wektor zawierający lata od 2000 do 2021 i drukuje  
każdy element wektora z przędzonym ciągiem znaków: "The year is: ".'
x = c(2000:2021)
for(i in x) 
 print(paste("The year is:", i) )

for(i in 2000:2021){ 
 print(paste("The year is:", 2000:2021 ))
}


'Zmodyfikuj tak pętlę z zadania 3 aby nie został wydrukowany rok 2013'
x = c(2000:2021)
for(i in x[-(14)]){
 if (i == 2013){
  next
 }
 print(paste("The year is:", i) )
}



 
'Stwórz poniższy kod aby wygenerować macierz mat

mat < − matrix(data = seq(10: 20), nrow = 6, ncol = 2)

Napisz program, który drukuje wartość i wiersza i j kolumny z macierzy mat,
poprzedzony następującym ciągiem znaków: Row ‘i’ and column ‘j’ have values of 1.
Program za i ma postawiać i-ty numer wiersza i za j j-ty numer kolumny.'
mat <- matrix(data = seq(10:20),nrow = 6,ncol = 2)
i <- as.integer(readline(prompt="Podaj numer rzędu "))
j <- as.integer(readline(prompt="Podaj numer kolumny "))
c  <- mat[i,j]

for i in (0:6)
 for y in 2
  print(paste('Row', i ,'and column' ,j ,'have values of',mat[i,j]))
  y =y +1
 i =i +1



'Napisz pętlę for, która drukuje co drugi element z wektora zawierającego liczby  całkowite od 1 do 10. 
Pętla ma rozpocząć drukowanie liczb od liczby jeden. '
y <- seq(1,10,by=2)

x <-  c(1:10)
u <- 1
for(i in 1:5) {
 print(x[u])
 u = u+2
}

for(i in seq(10)) {
 if(i %% 2 ==0){
  next
 }
 cat(paste('liczba =', k, '\n'))


'Napisz program który tworzy listę zawierającą trzy elementy: wektor koszyk z czterema  dowolnymi owocami, 
wektor cena z ceną za każdy owoc oraz zmienną zakup  przechowującą wartość logiczną FALSE. Napisz pętlę, 
drukującą każdy element z listy. '
koszyk <- c('jabłka','gruszki','brzoskwinie','śliwki')
cena <-  c(4,7,9,10)
zakup <- c(TRUE,FALSE,TRUE,FALSE)
i = 1
for(i in 1:3) {
 print(paste(koszyk[i],cena[i],zakup[i]))
 i =+ 1
}


'Wykorzystaj pętlę while, który na początku przyjmuje wartość zmiennej i równą 1,  
niech ta pętla drukuje i+1, póki 1 będzie mniejsze od 20. '

i=1
while(i<=20){
 print(i)
 i= i+1
}


#Nie działa jak w Pythonie
i=1
while(i<=20){
 print(i)
 i =+1
}



'Napisz funkcje ‘fahrenheit_to_celsius’, której zadaniem będzie przyjmowanie  temperatury w stopniach Fahrenheita 
i ich konwertowanie to stopni celcjusza. '
fahrenheit_to_celsius=function (temp_F){
 wynik = (temp_F - 32) * 5/9
 return(wynik)
}
fahrenheit_to_celsius(200)


'Napisz funkcje ‘celsius_to_kelvin’, której zadaniem będzie przyjmowanie temperatury  w stopniach Celsjusza i 
ich konwertowanie to stopni Kelvina. '
celsius_to_kelvin=function (temp_C){
 wynik =  temp_C + 273,15
 return(wynik)
}
celsius_to_kelvin(37)
