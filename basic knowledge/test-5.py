
data=[]
words=[]
count=20

def processLine(line,wordCounts):
	line=replacePunctuations(line)
	words=line.split()
	for word in words:
		if word in wordCounts:
			wordCounts[word]+=1
		else:
			wordCounts[word]=1


def replacePunctuations(line):
	for ch in "~`@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
		line=line.replace(ch," ")
	return line


def main():
      filename=input("Please enter a file's name:\n")
      infile=open(filename,"r")

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

if __name__ == '__main__':
    main()
