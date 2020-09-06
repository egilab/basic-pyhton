string = 'my global string'

def myFunc():
	global string #tambahkan global
	string  = 'hei ganti aku sip'

myFunc() #inisialisasi buat ganti global var
print(string)