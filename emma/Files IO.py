open_file = open('C:/Users/WeSEE18/Desktop/Python/Homework/openfile.txt', 'r')
write_file= open('C:/Users/WeSEE18/Desktop/Python/Homework/writefile.txt', 'w')
input=open_file.read()
write_file.write(input)
write_file.close()
print(input)


