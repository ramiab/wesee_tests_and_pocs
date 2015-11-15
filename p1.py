my_str = "I like bananas"

def reverse_str(my_str):
	reversed_str = ""
	for i in range(len(my_str)-1, 0, -1):
		c = my_str[i]
		reversed_str = reversed_str + c
	
	return reversed_str

a = reverse_str(my_str)
print("a = %s" % a)