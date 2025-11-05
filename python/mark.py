print("score out of 100")
a=int(input("Tamil mark:"))
b=int(input("English mark:"))
c=int(input("Maths mark:"))
d=int(input("Science mark:"))
e=int(input("Social mark:"))
f=(a+b+c+d+e)
print(f)
score=int(input("score:"))
if(score>450):
      print("excellent student")
elif(score<450 and score>350):
      print("good student")
elif(score>300):
    print("average student")
else:
    print("poor student")
