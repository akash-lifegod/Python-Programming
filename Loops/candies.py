# There are N kids in a play Group. The kid with number K (1 ≤ K ≤ N) will be happy if he receives at 
# least AK candies. There is C candies in all. 
# The school staff is interested in knowing whether it is possible to make all the N kids happy by 
# giving each kid at least as many candies as he wants, that is, the Kth kid should receive at least AK 
# candies. Each candy can be given to only one kid. Print Yes if it is possible and No otherwise. 
# Input 
# Input N, C and N integers A1, A2, ..., AN. 
# Output 
# Yes if it possible to make all kids happy and No otherwise.


n,c=int(input("Kids ")),int(input("Candies "))
sum=0
for i in range(1,n+1):
    a=int(input())
    sum=sum+a
if sum<=c:
    print("Yes")
else:
    print("No")