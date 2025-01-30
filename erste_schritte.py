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

# Listen Aufgabe 1
#
#def meine_liste():
#    obst = []
#    obst.insert(0,"Banane")
#    obst.insert(1,"Apfel")
#    obst.insert(2,"Orange")
#    
#    #print("")
#    #print(f"Gebe das zweite element in der Liste aus ---> {obst[2]} ")
#    
#    umgekehrt = obst[::-1]
#    #print(f"Die Liste mit obst in Umgekehrter reihenfolge ---> {umgekehrt}")
#       
#    #zusatz =["Traube", "Erdbeere"]
#    #kombi = obst + zusatz
#    #print(f"{kombi}")
#
#    #obst.append("Traube")
#    #obst.append("Erdbeere")
#    #print(f"nach dem einfügen von 2 weiteren die ausgabe ---> {obst}")
#    
#meine_liste()
#

#Aufgabe Sets 
#
#set1={'123456'}
#set2={'5678910'}
#set3= set1.union(set2)
#set3=set1.intersection(set2)
#set1.add('7')
#'8' in set2 
#set2.discard('10')
#
#set1.intersection_update(set2)
#set1.symmetric_difference_update(set2)
#set1.symmetric_difference(set2)
#
#set1|set2 
#set1-set2
#set1&set2
#set1^set2

# Lotto generator
#import random
#
#def weiter():   
#    print("Als nächstes wollen wir die Super Zahl ")
#    print("Bereit ? ")
#    eingabe2=input("Ja oder Nein ? : ")
#    if eingabe2 == "j":
#        superziehung()
#    elif eingabe =="n":
#        print("Vielen dank für dein Intresse !")
#def superziehung():
#    superzahl = random.randint(1,10)
#    print(superzahl)
#
#def lotto():
#    lottozahlen = []
#    lottozahlen.extend(range(0,50))
#    random.shuffle(lottozahlen)
#    for x in range(6):
#        print(lottozahlen[x])
#    weiter()
#print("Willkommen bei der Ziehung der Lotto zahlen")
#print("Wollen wir mit der Ziehung beginnen ? ")
#eingabe=input("Ja oder Nein ? : ")
#if eingabe == "j":
#    lotto()
#elif eingabe =="n":
#    print("Vielen dank für dein Intresse !")
#

# Spiel Schere Stein Papier
import random
def nochmal():
    print("Willkommen züruck bei Schere Stein Papier")
    gesten = ['Schere','Stein','Papier']
    computer_geste = random.choice(gesten)
    spieler_geste = None
    while spieler_geste not in gesten :
        print("Verfügbare gesten ", *gesten)
        spieler_geste=input("Bitte wählen Sie eine Geste aus : ")
        print(f"Sie haben {spieler_geste} gewählt, der Computer {computer_geste} : ", end="")
        if spieler_geste == computer_geste:
            print("Unentschieden! ")
        elif (
            (spieler_geste == "Schere" and computer_geste == "Papier")
            or (spieler_geste == "Stein" and computer_geste == "Schere")
            or (spieler_geste == "Papier" and computer_geste == "Stein")
        ): 
            print("Sie haben gewonnen! ")
            print("Nochmal Spielen ? ")
            eingabe= input("Ja oder Nein ? j/n ")
            if eingabe == "j":
                nochmal()
            elif eingabe == "n":
                print("Danke das Sie gespielt haben.")
                break
def spiel():
    print("Willkommen bei Schere Stein Papier")
    gesten = ['Schere','Stein','Papier']
    computer_geste = random.choice(gesten)
    spieler_geste = None
    while spieler_geste not in gesten:
        print("Verfügbare gesten ", *gesten)
        spieler_geste=input("Bitte wählen Sie eine Geste aus : ")
        print(f"Sie haben {spieler_geste} gewählt, der Computer {computer_geste} : ", end="")
        if spieler_geste == computer_geste:
            print("Unentschieden! ")
            print("Nochmal Spielen ? ")
            eingabe= input("Ja oder Nein ? j/n ")
            if eingabe == "j":
                nochmal()
            elif eingabe == "n":
                print("Danke das Sie gespielt haben.")
                break
        elif ((spieler_geste == "Schere" and computer_geste == "Papier")
            or (spieler_geste == "Stein" and computer_geste == "Schere")
            or (spieler_geste == "Papier" and computer_geste == "Stein")):
            print("Sie haben gewonnen! ")
            print("Nochmal Spielen ? ")
            eingabe= input("Ja oder Nein ? j/n ")
            if eingabe == "j":
                nochmal()
            elif eingabe == "n":
                print("Danke das Sie gespielt haben.")
                break
            else:
                print("Leider verloren! ")
                print("Nochmal Spielen ? ")
                eingabe= input("Ja oder Nein ? j/n ")
                if eingabe == "j":
                    spiel()
        else: 
            print("Danke das Sie gespielt haben.")
spiel()