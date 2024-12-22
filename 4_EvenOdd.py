# To find if the number is even or odd by using bitwise operator
'''
We Know that if a number is even the most significant bit(MSB) is 0 and if it is odd the MSB is 1
for example :-
Even number is [6] the binary form of [6] is 0110,
Similarly another example is [100] the binary form of [100] is 01100100
    in the above example we can see that the MSB is 0 in both the examples 
Now Let's see for odd 
let us take a number [9] the binary form of 9 is 1001
and similarly for any odd number the MSB will be 1
    So by using this method we can find if the number is odd or even 
    It will also reduce the time and complexity of the operation
'''


# the normal way of finding if the number is even or odd 
'''
num = int(input("Enter a number :- "))
if num % 2 == 0:
    print ("The number is even")
else:
    print("The number is odd")
'''

#Now by using the bitwise operator
'''
to find the number is odd or even using bitwise operator we can use the following code
'''

num = int(input("Enter a number :- "))
if num & 1 == 0:
    print ("The number is even")
else:
    print("The number is odd")
    
    
'''
The above code performs and(&) operation with the number and 1 and if the result is 0 then the number is even and if the result is 1 then the number is odd
'''