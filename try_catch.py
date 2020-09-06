text = input('input your username: ')
try:
	number = int(text)
	print(number)
except Exception as e:
	print(e)
