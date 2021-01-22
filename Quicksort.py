'''
Wie benutzt man das Programm?
Ganz einfach: Man gibt ein, wie lang das array sein soll
(Ich empfehle eine hohe Zahl, damit sich Quicksort überhaupt lohnt.).
Dann drückt man Enter und bekommt die zufälligen Zahlen, die gewählt wurden als ein Diagramm angezeigt.
Das Diagramm schließt man dann wieder und drückt bei der Aufforderung Enter zu drücken Enter.
Dann bekommt man noch ein Diagramm angezeigt. Dieses Mal mit den sortierten Werten.
'''


import warnings
warnings.simplefilter("ignore")
from random import *
from matplotlib import pyplot as plt 

def quicksort(array):
    if len(array) <= 1:
        return(array)
    else:
        pivot = array.pop()

    larger = []
    smaller = []

    for i in array:
        if i > pivot:
            larger.append(i)

        else:
            smaller.append(i)

    return quicksort(smaller) + [pivot] + quicksort(larger)


length = int(input("Wie lang soll das array sein? "))
array = []
for i in range(length):
    array.append(randint(0, length))
plt.plot(array)
plt.show()
input("Drücke Enter zum sortieren")
plt.plot(quicksort(array))
plt.show()

