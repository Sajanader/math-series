def fibonacci(n):
    if n == 0:
       return 0
    if n == 1:
       return 1
    else:
         return fibonacci(n-1) + fibonacci(n-2)



def lucas(n):
    if n == 0:
       return 2
    if n == 1:
       return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(required_arg, optional_arg1=0, optional_arg2=1):

    if optional_arg1 == 0 and optional_arg2 == 1:
       return(fibonacci(required_arg))

    if optional_arg1 == 2 and optional_arg2 == 1:
       return(lucas(required_arg))


  













