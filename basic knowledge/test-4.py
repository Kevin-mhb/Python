import turtle

#定义全局变量
count=10
data=[]
words=[]
yScale=6
xScale=30

def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto (x1, y1)
    t.pendown()
    t.goto (x2, y2)
 
# 在坐标(x,y)处写文字
def drawText(t, x, y, text):
    t.penup()
    t.goto (x, y)
    t.pendown()
    t.write(text)
 
def drawGraph(t):
    #绘制x/y轴线
    drawLine (t, 0, 0, 360, 0)
    drawLine (t, 0, 300, 0, 0)
 
    #x轴: 坐标及描述
    for x in range(count):
        x=x+1 #向右移一位,为了不画在原点上
        drawText(t, x*xScale-4, -20, (words[x-1]))
        drawText(t, x*xScale-4, data[x-1]*yScale+10, data[x-1])
    drawBar(t)
 
#绘制一个柱体
def drawRectangle(t, x, y):
    x = x*xScale
    y = y*yScale#放大倍数显示
    drawLine(t, x-5, 0, x-5, y)
    drawLine(t, x-5, y, x+5, y)
    drawLine(t, x+5, y, x+5, 0)
    drawLine(t, x+5, 0, x-5, 0)
     
#绘制多个柱体
def drawBar(t):
    for i in range(count):
        drawRectangle(t, i+1, data[i])

def processLine(line,wordCounts):
      
      line=replacePunctuations(line)
      
      words=line.split()
      for word in words:
            if word in wordCounts:
                  wordCounts[word]+=1
            else:
                  wordCounts[word]=1
      
def replacePunctuations(line):
      for ch in line:
            if ch in "~@#$%^&*()_+-=<>?/,.:{}[]\|';""":
                  line=line.replace(ch," ")
            return line
      
      
def main():
      filename=input("please enter a filename:").strip()
      infile=open(filename,"r")

      wordCounts={}

      for line in infile:
            processLine(line.lower(),wordCounts)

      pairs=list(wordCounts.items())

      items=[[x,y]for (y,x) in pairs]
      items.sort()

      for i in range(len(items)-1,len(items)-count-1,-1):
            print(items[i][1]+"\t"+str(items[i][0]))
            data.append(items[i][0])
            words.append(items[i][1])


      infile.close()

      turtle.title("词汇结果柱状图")
      turtle.setup(900,750,0,0)
      t=turtle.Turtle()
      t.hideturtle()
      t.width(3)
      drawGraph(t)
      
if __name__ == '__main__':
    main()
