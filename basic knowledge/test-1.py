'''
file1=open("test-1.txt","w")
file1.write("\npython is good .\n\nthe programing is fun .\n")
file1.close()

file2=open("test-1.txt","r")
txt0=file2.read()
file2.close()
print(txt0)

'''

def main():
      fname=input("Enter file's name :\n")
      file1=open(fname,"r")
      content=file1.read()
      file1.close()
      print(content)
      
main()

