row=int(input())
#column=int(input())

r = 0
l = 0

while r<row:
    while l<=r:
        print ("*", end=" ")
        l = l + 1
   
    r = r + 1
    l = 0
    print ("")
 

