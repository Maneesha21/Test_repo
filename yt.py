print("Hello world")
def even_odd(num):
    """ To check whether the given number is even or odd"""
    try:
        if num%2==0:
            print("even number")
        else:
            print("odd number")
    except(Exception,en):
        print(en)
num=5
even_odd(num)
