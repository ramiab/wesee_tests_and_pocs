

my_str1 = 'Eli Liberman'
VOWLS = ['a','e','o','u','i']
	
def translate(my_str):
	result = ""
	for i in my_str:
		if i.lower() not in VOWLS:
			result = result + i + 'o' + i
		else:
			result = result + i
	return result
			
a = translate(my_str1)
print(a)