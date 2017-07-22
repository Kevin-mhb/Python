#将普通的文件操作利用函数实现
'''
file2=open("file-1.txt","w")
file2.write("python is a very excellent programing language .")
file2.close()

file3=open("file-1.txt","r")
data=file3.read()
file3.close()
print("The contents are :\n\n"+data)

'''

def writeFile():
      file1=open("file-1.txt","w")
      file1.write("Python is a very excellent programing language .\n")
      file1.close()

def readFile():
      file2=open("file-1.txt","r")
      data=file2.read()
      file2.close()
      print("The contents are :\n\n"+data)

def main():

      writeFile()
      readFile()


main()
