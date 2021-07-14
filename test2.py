data = [0]*7
data[0],data[1],data[2],data[4] = map(int,input("Enter the data: "))
data[6] = data[0]^data[2]^data[4]
data[5] = data[0]^data[1]^data[4]
data[3] = data[0]^data[1]^data[2]

print("Encoded bits are: ",*data)

rec = list(map(int, input("Enter the received data: ")))
p1 = rec[6]^rec[4]^rec[2]^rec[0]
p2 = rec[5]^rec[4]^rec[1]^rec[0]
p3 = rec[3]^rec[2]^rec[1]^rec[0]

c = p3*4+p2*2+p1
if c==0:
    print("No error found")
else:
    print("error on the position: ",c)
    if rec[7-c] == 0:
        rec[7-c] = 1
    else:
        rec[7-c] = 0
    print("Correct data is: ",*rec)