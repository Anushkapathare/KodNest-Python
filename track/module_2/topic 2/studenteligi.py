marks = int(input())
attendance = int(input())
project_status = str(input())
if marks>=60 and attendance>=75:
 if project_status == "yes":
  print("Eligible")
 else:
    print("Not Eligible")
else:
    print("Not Eligible")