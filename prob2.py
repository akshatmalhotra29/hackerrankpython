# Hackerrank
# https://www.hackerrank.com/challenges/compress-the-string/problem
import sys

S=sys.stdin.readline().rstrip()
cnt=0
op=''
for i,letter in enumerate(S):
    num = int(letter)
    if i==0:
        cnt=cnt+1
        continue
    elif num==int(S[i-1]):
        cnt=cnt+1
    else:
        op=op+str((cnt,int(S[i-1])))
        op=op+' '
        cnt=1
op=op+str((cnt,int(S[len(S)-1])))
sys.stdout.write(op)