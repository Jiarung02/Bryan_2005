import student

stu1 = student.Student("吳家榕", 86, 91, 74)  #module名稱 /＃class名稱
print(stu1.chinese)#實體attribute
print(stu1.english)
print(stu1.math)
print(stu1.total()) #實體method
print(stu1.average)#實體property不括號
print(stu1)