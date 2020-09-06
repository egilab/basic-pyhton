# for x in range(0, 11, 1): #start, stop, step : default 1
# 	print(x)

word = ['cat','mouse','tiger','lion']

for x in word[:]:
	print(x)
	if(len(x) == 3):
		word.insert(2, x)

print('-------')
print(word)