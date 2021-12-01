# -------Q1---------
# seq=[1,2,3]
#
# def arryCheck(nums):
#     ans=False
#     for x in range (0,len(nums)-2):
#         if nums[x:x+3]==seq:
#             ans=True
#     return ans
# print(arryCheck([3,4,1,2,3]))


# # ----------Q2(given two string...)--------
# def end_other(s1,s2):
#     if len(s1)<len(s2):
#         swap(s1,s2)
#     s1=s1[::-1]
#     s2=s2[::-1]
#     ans=True
#     for i in range(0,len(s2)):
#         if s2[i]!=s1[i]:
#             ans=False
#             break
#     return ans
#
# answer=end_other('abcd', 'abcd')
# print(answer)

# ------Q3(no teen sum)-------

teens=[13,14,15,16,17,18,19]
def check_teen(a):
    if(teens.count(a)>0):
        return True
    else:
        return False

def find_sum(a,b,c):
    ans=0
    myList=[a,b,c]
    for x in myList:
        if not check_teen(x):
            ans=ans+x
    return ans
print(find_sum(19,13,15))
