trip_obj = open("tripin.txt" , "r")
trip_str_lines = trip_obj.read().splitlines()

n = int(trip_str_lines[0])
integer_stringlist = trip_str_lines[1:(n+1)]


# calculate the result
k = 0
pre_result = ""
for i in range(n-1):
    if ((int(integer_stringlist[i])/3)*3)==int(integer_stringlist[i]):
        k+=1
        pre_result = pre_result + str(i+1) + " " 

if ((int(integer_stringlist[(n-1)])/3)*3)==int(integer_stringlist[(n-1)]):
    k+=1
    pre_result+=str(n)

if k==0:
    result = "Nothing here!"
else:
    result = str(k) + "\n" + pre_result


# write down the answer
trip_obj_out = open("tripout.txt" , "w")
trip_obj_out.write(result)
trip_obj_out.close()