#For Loop
# One character goes to x and it prints. And it continues until all characters are printed.
#If you just give a single parameter in range function it will consider that parameter as ending number and starting number will be 0 and sequence will be j+1 by default. [x = range(0,5,0+1)]
#Syntax => for variable1 in variable2:
#variable1 will be printed.
Name = "Cool_Kid_J"
for x in Name:
  print(x)

#For loop with range function 
a = range(5)
for i in a:
  print(i)
#alter way
for j in range(1,8,2):
  print(j)

#For loop with range function and index,length,print each index,from character to index stuff...
#to get index from character we have to use range function 
z = "CoolKidJ"
n = len(z)
for i in range(n):
  print(i,"=",z[i])

#For loop with else 
V=""
for l in V: #no character in variable "v" thats why else part printed.
  print(l)
else:
  print("Beast")
