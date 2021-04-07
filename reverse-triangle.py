row=int(input())
#column=int(input())

r = 0
l = 0

while r<row:
    while l<row:
        print ("*", end=" ")
        l = l + 1
   
    r = r + 1
    l = r
    print ("")
 

