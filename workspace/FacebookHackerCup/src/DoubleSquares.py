###############################################################################
# Jonathan M. Stout
###############################################################################

def find_double_squares(file):
    f = open(file)
    
    d = list()
    
    for line in f:
        n = int(line[:-1])
        r = find_squares(n)
        if r != None:
            d.append(r)
        
    print(len(d))

def find_squares(n):
    a = 0
    b = 0
    
    while(a**2 + b**2 < n):
        if a + b == n:
            return a, b
        else:
            
            return None
          
find_double_squares("test.txt")
sqrt(2147483647)