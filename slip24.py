def Convert_fun(tuple_str):
    result = tuple((int(x[0]),int(x[1])) for x in tuple_str)
    return result 
tuple_str = (('333','33'),('1416','55'))
print("original tuple values:")
print(tuple_str)
print("\n new tuple values:")
print(Convert_fun(tuple_str))