my_tuple=(70,75,60,59,40,60,80)
def greater_60(x):
    if x>60:
        return x
x=list(filter(greater_60,my_tuple))
print(x)