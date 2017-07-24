'''
file1=open("test-1.txt","w")
file1.write("\npython is good .\n\nthe programing is fun .\n")
file1.close()

file2=open("test-1.txt","r")
txt0=file2.read()
file2.close()
print(txt0)



def main():
      fname=input("Enter file's name :\n")
      file1=open(fname,"r")
      content=file1.read()
      file1.close()
      print(content)
      
main()

'''

def main():
      f1=input("please input one file's name:").strip()
      f2=input("please input one file's name:").strip()

      file1=open(f1,"r")
      file2=open(f2,"w")

      countL=countC=0
      for line in file1:
            countL+=1
            countC+=len(line)
            file2.write(line)

            print(len(line))

      print(countL,"lines and",countC,"chars copied")
      

      file1.close()
      file2.close()

main()
            





            
