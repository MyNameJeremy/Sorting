from random import *
array = []
long = int(input("Wie lang soll das array sein? "))
while len(array) < long:
	rnd = randint(0,long)
	if rnd not in array:
		array.append(rnd)
print(array)

help = 0
while help < len(array)-1:
	i = 0
	while i < len(array)-1:
		x = 0
		help = 0
		if array[i] > array[i+1]:
			array[i], array[i+1] = array[i+1], array[i]
		for x in range(len(array)-1):
			if array[x] < array[x+1]:
				help += 1
		i += 1
print(array)