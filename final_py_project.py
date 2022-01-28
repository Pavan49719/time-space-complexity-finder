#Reading the input python file
f=open("test1.py","r")
contents=f.read()
l=contents.split("\n")

f.close()

flag_for="for"
flag_while="while"

#Function for calculating time complexity

def func(l):
    f=[]
    
    #Iterating through the input file line by line    
    for i in l:
        n=0
        space=0
        
        #Searching for "for" loops in the file
        if flag_for in i:
            for j in i:
                if j==' ':
                    space+=1
                else:
                    break
            if(space==4):
                f.append(1)        
            for k in range(0,space,4):
                n+=1
            f.append(n)
            
        #Searching for "while" loops in the file
        elif flag_while in i:
            for j in i:
                if j==' ':
                    space+=1
                else:
                    break
            if(space==4):
                f.append(1)        
            for k in range(0,space,4):
                n+=1
            f.append(n)
        
        #Checking for absence of loops in the file
        else:
            n=0
            f.append(n)
            
    return max(f)        

#Calling the function for calculating time complexity
t=func(l)

#Writing the time complexity in a text file 
with open("result.txt","w") as fh:
    
    if(t==0):   
        fh.write("Time complexity of the code: O(1)")
        print("Time complexity of the code: O(1)")
    else:
        string="Time complexity of the code: O(n^"+str(t)+")"
        print("Time complexity of the code: O(n^"+str(t)+")")
        fh.write(string)
  
import sys
import keyword

#Reading the input python file
f=open("test1.py","r")
contents=f.read()
l=contents.split("\n")
f.close()
lines_in_function=1
flag="def"

#Storing all the keywords present in python in k_list
k_list=keyword.kwlist
k_list.append('print')

g=[]
m=[]

#Extracting the function present in the input file
for i in l:
    
    #Checking for function headers in the input file
    if flag in i:
        func_invoke=i[4:-1]
        # print("FUNC_INVOKE",func_invoke)
    #Checking for function calling in the input file
    elif func_invoke==i:
        l=[x for x in l if x!=func_invoke]
        l.append("    ss=locals()")
        l.append("    return ss")
        
    #Appending the local variables
    else:
        space=0
        for j in i:
            if j==" ":
                space+=1
            else:
                break
        if space==0:
            g.append(i)
        for k in k_list:
            if k in i:
                g.append(i)
   

with open('test4.py', "w") as nf:
    for i in l:
        if i not in g:
            nf.write("%s\n" % i)
        elif i=='':
            continue

#Appending the global variables
for i in range(len(g)):
    if g[i].startswith(" ") or g[i].startswith("def") or len(g[i])==0:
        continue
    else:
        m.append(g[i])

#Importing our created module

f=open("test4.py","r")
contents4=f.read()
l4=contents4.split("\n")
f.close()
l4.pop(0)
l4.pop(-1)
for i in l4:
    if '=' not in i:
        l4.remove(i)
# print(l4)
space_complexity={}
for i in l4:
    temp=i.split('=')
    # print(temp)
    temp[0]=temp[0].strip()
    # print(temp[0])
    space_complexity[temp[0]]=temp[1]
# print('SPACE COM',space_complexity)
print(space_complexity)

total_size=0

with open("result.txt", "a") as fh:
    
    #Writing the space complexity in a text file
    for i in space_complexity.keys():
        for j in i:
            if keyword.iskeyword(j):
                continue
        else:
            total_size=total_size + sys.getsizeof(space_complexity[i])
            string="\nSize of the value "+str(space_complexity[i])+" of the variable "+i+" is: "+str(sys.getsizeof(space_complexity[i]))+" bytes"
            fh.write(string)
            print(string)
    for i in range(len(m)):
        c=0
        for j in k_list:
            if m[i].startswith(j):
                c+=1
        if(c==0):    
            string="\nSize of variable "+m[i]+" is = "+str(sys.getsizeof(m[i]))+" bytes"
            fh.write(string)
            print(string)

    fh.write("\nTotal size used of the code is "+str(total_size)+" bytes")
    print("\nTotal size used of the code is "+str(total_size)+" bytes")

