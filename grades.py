math=[]
fizika=[]
rus=[]
predmet=[math,fizika,rus]

def abiturient(line):
  res1=line.split(';')
  math.append(res1[1])
  fizika.append(res1[2])
  rus.append(res1[3])
  print((int(res1[1])+int(res1[2])+int(res1[3]))/3)


def sredbal():
  print(sum([int(item) for item in math])/len(math))
  print(sum([int(item) for item in fizika])/len(fizika))
  print(sum([int(item) for item in rus])/len(rus))


for line in open(file):
  abiturient(line)
if not line:
  sredbal()
