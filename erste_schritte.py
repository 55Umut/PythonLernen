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

#def anzahl_stellen(n):
#    return len(str(abs(n)))
#zahl = int(input("Bitte eine Zahl eingeben: "))
#result = anzahl_stellen(zahl)
#print(f"Die Zahl {zahl} hat {result} Stellen.")

# Aufgabe

#x=0
#for i in range(1, 100, 1):
#    if i % 4 == 0:
#     x=x+1
#     print(i)
#    if x==10:
#        break

## Aufgabe

#x=0
#for i in range(1, 51, 1):
#    if i % 2 == 0:
#     x=x+1
#     print(i)
#    if x==50:
#        break

# Aufgabe

#x=0
#for i in range(1, 6, 1):
#    if i % 4 == 0:
#     x=x**2
#     print(i)
#    if x==100:
#        break

# Aufgabe 
#summe=0
#for i in range(1, 10, 1):
#     summe+=i
#     print(f"Die Summe der Zahlen von 1 bis 10 ist {summe}")

# Strings Aufgabe 1
# 

#def string_zaehler () :
#    string1 = input("Bitte gebe etwas ein ")
#    string2 = input("Bitte gebe noch etwas ein ")
#    print(" Deine erste Eingabe war ",len(string1)," Zeichen lang")
#    print(" Deine zweite eingabe war ",len(string2)," Zeichen lang")
#    if string1 < string2:
#        print("Deine erste eingabe war kürzer als deine zweite eingabe ", string1)
#    elif string1 == string2:
#        print("Deine eingaben waren gleich lang ", string1,string2)
#    elif string2 > string1:
#        print("Deine zweite eingabe war länger als deine erste eingabe ",string2)
#string_zaehler()

# Strings Aufgabe 2
# 

#def satz_zaehlen ():
#    satz = input("Bitte gebe einen Satz ein: ")
#    x = satz.split(" ")
#    print(len(x))
#satz_zaehlen()

# Strings Aufgabe 3
# 
#def gross_schrift():
#    gross = input("Bitte gebe etwas ein: ")
#    print(gross.swapcase())
#gross_schrift()

# Strings Aufgabe 4
# 

#def palindrom_check():
#    eingabe= input("Bitte gebe ein Wort ein was vorwärts wie rückwärts gelesen werden kann: ")
#    if eingabe == eingabe[::-1]:
#        print(f"Treffer dein wort war --> {eingabe} <--")
#    else :
#        print(f"Schade marmelade dein Wort --> {eingabe} <-- ist kein Palindrom")
#palindrom_check()

# Strings Aufgabe 5
# 
#def vokal_entferner():
#    text= input("Bitte gebe etwas ein um die Vokale zu entfernen: ")
#    for i in "aeiouAEIOU":
#        text = text.replace(i,"")
#        print(text)
#vokal_entferner()

#def vokal_entferner():
#    text = input("Bitte gebe etwas ein um die Vokale zu entfernen: ")
#    tabelle = str.maketrans("", "", "aeiouAEIOUäÄüÜöÖ")
#    text = text.translate(tabelle)
#    print(text)
#vokal_entferner()

# Strings Aufgabe 6
#  
#from collections import Counter
#def haeufigstes_zeichen(s):
#    return Counter(''.join(filter(str.isalpha, s.lower()))).most_common(1)[0][0] if s else None
#string = input("Gib einen Text ein: ")
#print("Das häufigste Zeichen ist:", haeufigstes_zeichen(string) if string else "Es wurde kein Text eingegeben.")

# Strings Aufgabe 7
#  
#def anagramme():
#    string1 = input("Gib den ersten String ein: ")
#    string2 = input("Gib den zweiten String ein: ")

