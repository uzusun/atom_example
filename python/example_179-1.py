file_object = open('datafile.txt','w')

for num in range(11):
    write_data = str(num)
    file_object.write(write_data)
    file_object.write("\n")

file_object.close()
