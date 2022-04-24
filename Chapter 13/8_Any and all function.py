# Any and All function
Number1 =[2,4,6,8]
Number2 =[3,7,5,9,11]
print(all([i%2==0 for i in Number1]))
print(any([num%2!=0 for num in Number2]))



# evens1 = []
# for i in Number1:
#     evens1.append(i %2 ==0)
# print(evens1)
# print(all([False, True, False, True, False]))