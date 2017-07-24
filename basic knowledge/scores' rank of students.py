#将学生成绩等级化（满分100分）



print("Please input a student's score:\n")

score=int(input())
if score>=90 and score<=100:
      print("This student's rank is A .")

elif score>=80 and score<90:
      print("This student's rank is B .")

elif score>=70 and score<80:
      print("This student's rank is C .")

elif score>=60 and score<70:
      print("This student's rank is D .")

else:
      print("This student's rank is E .")

print("\nIt's over...")


