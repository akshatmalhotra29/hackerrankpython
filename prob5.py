#Hackerrank
#https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    cnt=[0]*256
    op=''
    for i,c in enumerate(string):
        if i%k==0 and i!=0:
            cnt=[0]*256
            print(op)
            op=''
        if cnt[ord(c)]==0:
            op=op+c
            cnt[ord(c)]=cnt[ord(c)]+1
    print(op)


merge_the_tools("AABCAAADA",3)

