file_object = open('datafile.txt','r')
lines = file_object.readlines()
file_object.close()
file_object = open('datafile1.txt','w')
for line in lines:
    if (int(line)%2) == 0:
        file_object.write(line)

file_object.close()
