import pandas as pd

namelist=[]
familyNamelist=[]
SchoolNamelist=[]
avglist=[]
student_number=int(input("How many student save ?: "))

i=1
while True:
    
    name=input("Enter Name: ")
    familyName=input("Enter Surname: ")
    SchoolName=int(input("Enter School Number: "))
    visaNot=int(input("Enter Visa Not: "))
    if visaNot>100:
        print("Visa not cannot be greater than 100, enter again.")
        continue
    if visaNot<0:
        print("Visa not cannot be less than 0, enter again.")
        continue
    finalNot=int(input("Enter Final Not:"))
    if finalNot>100:
        print("Final not cannot be greater than 100, enter again.")
        continue
    if finalNot<0:
        print("Final not cannot be less than 0, enter again.")
        continue

    avg=(visaNot*0.4)+(finalNot*0.6)
    namelist.append(name)
    familyNamelist.append(familyName)
    SchoolNamelist.append(SchoolName)
    avglist.append(avg)
    if i==student_number:
        break
    i+=1
   

seri1=pd.DataFrame({"Name":namelist,"Surname":familyNamelist,"School_Number":SchoolNamelist,"Avg":avglist})
seri1.loc[seri1['Avg'] <= 40, 'conclusion'] = 'Left' 
seri1.loc[seri1['Avg'] > 40, 'conclusion'] = 'Passed'


if avg>90 and avg<=100:
    print("Avg = AA ")
elif avg>80 and avg<=90:
    print("Avg = BA ")
elif avg>70 and avg<=80:
    print("Avg = BB ")
elif avg>60 and avg<=70:
    print("Avg = CB ")
elif avg>50 and avg<=60:
    print("Avg = CC ")
elif avg>40 and avg<=50:
    print("Avg = DC ")
elif 0<avg<=40:
    print("Avg = FF ")

print(seri1)
