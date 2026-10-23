name=input("Enter Student name:")
marks=[]
for i in range(1, 6):
    mark=int(input("Enter subject{i} mark"))
    marks.append(mark)
total=sum(marks)
percentage= total/5
print("\n---Student Result")
print("Name:",name)
print("Total:",total,"/500")
print("Percentage:",percentage,"%")
if percentage >=90:
    print("Grade:A")
elif percentage >=75:
    print("Grade:B")
elif percentage >=50:
    print("Grade:C")
else:
    print("Grade:D")    