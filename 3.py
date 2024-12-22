#Calculating the half of a number

'''
def main():
    a = 5
    while a > 0:  
        a = a>>1
        # a = a//2        #this is similar to a>>1,it can be used to find the half of any number using a bitwise operator
        print(a)

if __name__ == "__main__":
    main()
'''

'''
Output:-
2
1
0
'''



# Calculating the twice of a number

def main():
    a = 5
    for i in range(5):  
        # a = a<<1
        a = a*2        #this is similar to a<<1,it can be used to find the twice of any number using a bitwise operator
        print(a)

if __name__ == "__main__":
    main()


'''
Output:-
10
20
40
80
160
'''