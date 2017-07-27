def processLine(line,wordCounts):
	line=replacePunctuations(line)
	words=line.split()
	for word in words:
		if word in wordCounts:
			wordCounts[word]+=1
		else:
			wordCounts[word]=1