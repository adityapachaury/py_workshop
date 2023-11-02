x = 10 ### Global variable
def modify_global():
    global x       ##using Global keyword
    x = 20
    print(x)
modify_global()