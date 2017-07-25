

infile=open("test-1.txt","r")

for i in range(5):
      line=infile.readline()
      print(line[:-1])
