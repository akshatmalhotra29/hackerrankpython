#Hackerrank
#https://www.hackerrank.com/challenges/the-minion-game/problem
import sys
S = sys.stdin.readline().rstrip()
st=0
kev=0
for i,letter in enumerate(S):
    if letter in ['A','E','I','O','U']:
        kev=kev+ (len(S)-i)
    else:
        st=st+(len(S)-i)
op=''
if st>kev:
    op='Stuart '+str(st)
elif kev>st:
    op='Kevin '+str(kev)
else:
    op='Draw'

sys.stdout.write(op)