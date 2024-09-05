numbers=[10,20,30,40]

def addplus(num):
    return num+1
map_obj=map(lambda num:num+1 addplus,numbers)

new_numbers=list(map_obj)
print(numbers)