import numpy as np
import math
import json

classes = [[],[],[],[]]
nums = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
cores = [[],[],[],[]]
core = [[],[],[],[]]
distan = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
def getfile(path, num):
	file = path
	with open(file) as f:
		nums[num] = json.load(f)

getfile('json1.json', 0)
classes[0].append('json1.json')
getfile('json2.json', 1)
classes[0].append('json2.json')
getfile('json3.json', 2)
classes[0].append('json3.json')

cores [0] = (np.array(nums[0]) + np.array(nums[1]) + np.array(nums[2]))/3
core [0] = np.array(cores [0])

getfile('json4.json', 3)
classes[1].append('json4.json')
getfile('json5.json', 4)
classes[1].append('json5.json')
getfile('json6.json', 5)
classes[1].append('json6.json')

cores [1] = (np.array(nums[3]) + np.array(nums[4]) + np.array(nums[5]))/3
core [1] = np.array(cores [1])

getfile('json7.json', 6)
classes[2].append('json7.json')
getfile('json8.json', 7)
classes[2].append('json8.json')
getfile('json9.json', 8)
classes[2].append('json9.json')

cores [2] = (np.array(nums[6]) + np.array(nums[7]) + np.array(nums[8]))/3
core [2] = np.array(cores [2])

getfile('json10.json', 9)
classes[3].append('json10.json')
getfile('json11.json', 10)
classes[3].append('json11.json')
getfile('json12.json', 11)
classes[3].append('json12.json')

cores [3] = (np.array(nums[9]) + np.array(nums[10]) + np.array(nums[11]))/3
core [3] = np.array(cores [3])

getfile('json13.json', 12)
i = 0
for i in range(4):
	dist = 0
	for i2 in range(10):
		for i3 in range(10):
			distance = nums[12][i2][i3] - cores[i][i2][i3]
			dist += distance*distance
	di = math.sqrt(dist)
	distan[0][i].append(di)
print ('расстояния объекта от ядер 1-4 соответсвенно')
print (distan[0])
point = min(distan[0])
l = len(distan[0])
for i in range(l):
	if distan[0][i] == point:
		print("минимальное расстояние до ядра ", (i+1))
		classes[i].append('json13.json')
		print ('выведем новый объект в кдасс ', (i+1))
		print (classes[i])
		break

getfile('json14.json', 13)
i = 0
for i in range(4):
	dist = 0
	for i2 in range(10):
		for i3 in range(10):
			distance = nums[13][i2][i3] - cores[i][i2][i3]
			dist += distance*distance
	di = math.sqrt(dist)
	distan[1][i].append(di)
print ('расстояния объекта от ядер 1-4 соответсвенно')
print (distan[1])
point = min(distan[1])
l = len(distan[1])
for i in range(l):
	if distan[1][i] == point:
		print("минимальное расстояние до ядра ", (i+1))
		classes[i].append('json14.json')
		print ('выведем новый объект в кдасс ', (i+1))
		print (classes[i])
		break

getfile('json15.json', 14)
i = 0
for i in range(4):
	dist = 0
	for i2 in range(10):
		for i3 in range(10):
			distance = nums[14][i2][i3] - cores[i][i2][i3]
			dist += distance*distance
	di = math.sqrt(dist)
	distan[2][i].append(di)
print ('расстояния объекта от ядер 1-4 соответсвенно')
print (distan[2])
point = min(distan[2])
l = len(distan[2])
for i in range(l):
	if distan[2][i] == point:
		print("минимальное расстояние до ядра ", (i+1))
		classes[i].append('json15.json')
		print ('выведем новый объект в кдасс ', (i+1))
		print (classes[i])
		break

getfile('json16.json', 15)
i = 0
for i in range(4):
	dist = 0
	for i2 in range(10):
		for i3 in range(10):
			distance = nums[15][i2][i3] - cores[i][i2][i3]
			dist += distance*distance
	di = math.sqrt(dist)
	distan[3][i].append(di)
print ('расстояния объекта от ядер 1-4 соответсвенно')
print (distan[3])
point = min(distan[3])
l = len(distan[3])
for i in range(l):
	if distan[3][i] == point:
		print("минимальное расстояние до ядра ", (i+1))
		classes[i].append('json16.json')
		print ('выведем новый объект в кдасс ', (i+1))
		print (classes[i])
		break
