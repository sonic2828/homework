math=[]
fizika=[]
rus=[]
predmet=[math,fizika,rus]

def sredbal(predmet):
	print(sum(predmet[0])/len(predmet[0]))
	print(sum(predmet[1])/len(predmet[1]))
	print(sum(predmet[2])/len(predmet[2]))

	  

	  
	  
def abiturient(line):
	res1=line.split(";")
	math.append(res1[1])
	fizika.append(res1[2])
	rus.append(res1[3])
  print(sred1=(int(res1[1])+int(res1[2])+int(res1[3]))/3)



for line in open(file):
  abiturient(line)
if not line:
  sredbal(predmet)
