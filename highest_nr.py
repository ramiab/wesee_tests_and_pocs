

my_list = [1,33,456,45]

def highest_number ( my_list ):
	my_number = 0
	for each in my_list:
		if each > my_number:
			my_number = each
	print (my_number)
		
highest_number(my_list)

#print check_highest_number(my_list)