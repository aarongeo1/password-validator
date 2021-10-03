#--------------------------------------------
#   Name: AARON GEO BINOY
#   ID: 1720456
#   CMPUT 274
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 
# FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

import sys

def get_file_name():   
    filename = sys.argv[1]
    
    while True:
        try:
            f = open(filename,"r")
            return(f)
        except FileNotFoundError:
            print("file not found")
        except OSError:
            print("OS ERROR")
        except EOFError:
            break
def read(f):
    j=f.readlines()
    words=[]
    for i in j:
        k = i.strip().split()
        words += k
    return(words)
def count(l):
    length=len(l)
    c=0
    d={}
    for i in l:
        if i not in d:
            for j in l:
                if i not in d:
                    d[i]=0
                    continue
                if i==j:
                    c += 1
            freq=[c,round(c/length,3)]
            d[i]=freq
            print(d[i])
    return(d)
def write(d):
    filename = sys.argv[1]
    f=open(filename+".out","w")
    keys=d.keys()
    for i in keys:
        line=i+" "
        for j in d[i]:
            line+=str(j)+" "
        print(line)
        line+="\n"
        f.write(line)        
    f.close()

if __name__ == "__main__":
    file=get_file_name()
    words=read(file)
    no=count(words)
    write(no)

    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    pass