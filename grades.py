math=[]
fizika=[]
rus=[]

def abiturient(line):
  res=line.split(';')
  math.append(res[1])
  fizika.append(res[2])
  rus.append(res[3])
  print((int(res[1])+int(res[2])+int(res[3]))/3)


def sredbal():
  print(sum([int(item) for item in math])/len(math))
  print(sum([int(item) for item in fizika])/len(fizika))
  print(sum([int(item) for item in rus])/len(rus))


for line in open(file):
  abiturient(line)
if not line:
  sredbal()
