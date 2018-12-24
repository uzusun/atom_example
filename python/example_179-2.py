file_object = open('datafile.txt','a')

for num in range(11,21,2):
    write_data = str(num)
    file_object.write(write_data)
    file_object.write("\n")

file_object.close()
