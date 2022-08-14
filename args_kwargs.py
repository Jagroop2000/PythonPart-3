def super_func(*args,  **kwargs):
    print(kwargs)
    return sum(args)

super_func(1,2,3,4,5 , num1=6, num2=7)

# Rul3 v: params , *args , default parameters , **kwargs