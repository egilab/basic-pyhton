data = ['a','b','c','d','e','a']
print(data)
data.append('fg')
print(data)
data.extend('1212') #append tapi per character (string)
print(data)
data.insert(2,'tes') #append data tapi pake index
print(data)
data.remove('tes') #remove by value array
print(data)
data.pop(5) #remove by index, jika kosong akan menghapus index terakhir
print(data)
print(data.index('1',7))
data.reverse() #dibalik
print(data)
data2 = data.copy()
print(data2)
#data.clear()
#print(data)