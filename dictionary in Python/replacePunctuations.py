def replacePunctuations(line):
	for ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
		line=line.replace(ch," ")
	return line

	
