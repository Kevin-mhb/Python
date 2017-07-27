words=[]
data=[]
count=10

def main():
	infilename=input("Please enter a file's name:\n")
	infile=open(infilename,"r")

	wordCounts={}

	for line in infile:
		processLine(line.lower(),wordCounts)

	pairs=list(wordCounts.items())

	items = [[x,y]for (y,x)in pairs] 
    items.sort() 

    for i in range(len(items)-1, len(items)-count-1, -1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
         
    infile.close()
