# Übung 1 Aufgaben von 1 bis 5 Python Basics

#print("Hallo Welt!") 
#name = "Umut"
#print("Hallo Welt!"+name)
#satz="Hallo Welt! "
#print(satz, name) 
#eingabe = input("Bitte geben Sie Ihren Namen ein: ")
#print("Der Name lautet : "+eingabe)

## Übung 2 Aufgaben von 1 bis 4 

#while True:
#    secret_number = 7
#    guess_number = int(input("Gib eine Zahl zwischen 1 und 10 ein: "))
#    if guess_number == secret_number:
#        print("Treffer!")
#        break
#    elif guess_number > secret_number:
#        print("Die Zahl ist zu groß.")
#    else:
#        print("Die Zahl ist zu klein.")

### Übung 3 Aufgaben mit While

#def summe_naturzahlen(n):
#    summe = 0
#    i = 1
#    while i <= n:
#        summe += i
#        i += 1
#    return summe
#print(summe_naturzahlen(10)) 

def anzahl_stellen(n):
    return len(str(abs(n)))
zahl = int(input("Bitte eine Zahl eingeben: "))
result = anzahl_stellen(zahl)
print(f"Die Zahl {zahl} hat {result} Stellen.")