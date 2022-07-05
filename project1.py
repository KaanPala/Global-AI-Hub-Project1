sData= []

def sCheck(lesdata1,lesdata2):
	avg= lesdata1*0.4+lesdata2*0.6
	if avg >100:
		return False
	elif avg >84:
		return "AA Successful"
	elif avg >65:
		return "BB Successful"
	elif avg >50:
		return "CC Successful"
	else :
		return "unsuccessful"

while True:
	sName= input("Student Name :")
	sSurName =input("Student Surname :")
	sNum= input("Student No :")
	lesData1 = int(input("Visa Not :"))
	lesData2 = int(input("Final Not :"))
	sData.append(["Student No: {}".format(sNum),
    "Student Name: {}".format(sName),
    "Student Surname: {}".format(sSurName),
    "Visa Not : {}".format(lesData1),
    "Final Not: {}".format(lesData2),
    "AVG : {}".format(lesData1*0.4+lesData2*0.6),
    sCheck(lesData1,lesData2)])
	for i in sData:
		print(i)
	break
sData=str(sData)
file=open("Student_File.txt","w")
file.write(sData)
file.close()
