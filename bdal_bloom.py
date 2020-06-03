def h1(x):
	return ((3*x+3)%6)
def h2(x):
	return ((3*x+7)%8)
def h3(x):
	return ((2*x+9)%2)
def h4(x):
	return ((2*x+5)%5)

init_array=[]
for i in range(10):
	init_array.append(0)
inputSequence=[1,2,3,4]

for i in inputSequence:
	init_array[h1(i)]=1
	init_array[h2(i)]=1
	init_array[h3(i)]=1
	init_array[h4(i)]=1
print("Enter the input sequence")
testSequence=list(map(int,input().split()))

for i in testSequence:
	if(init_array[h1(i)]==0 or init_array[h2(i)]==0 or init_array[h3(i)]==0 or init_array[h4(i)]==0 ):
		print(i,"is definitely not present")
	else:
		print(i,"may or may not be present")
