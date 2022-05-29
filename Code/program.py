import sys

def hello(a,b):
    for i in range(a,b+1):
    if(i%2 == 0):
    print ("even", i, , sep=", ")
    for a in range(a,b+1):
    if(a%2 != 0):
    print ("odd", a, , sep=", ")

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    hello(a, b)