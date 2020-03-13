#Hackerrank
#https://www.hackerrank.com/challenges/matrix-script/problem

import re
str="$@This$#is% Matrix#  %!"
# pattern= re.compile('([a-zA-Z0-9][!|@|#|$|%|&| ]+[a-zA-Z0-9])')
#pattern= re.compile('([a-zA-Z0-9]+|([!|@|#|$|%|&| ]+$)|(^[!|@|#|$|%|&| ]+))')
words= re.compile('([a-zA-Z0-9]+)')
en_junk= re.compile('([a-zA-Z0-9][!|@|#|$|%|&| ]+$)')
st_junk= re.compile('(^[!|@|#|$|%|&| ]+)')

w_matches=words.findall(str)
s_matches=st_junk.findall(str)
e_matches=en_junk.findall(str)
#print(e_matches)
#results = [int(match.group(1)) for match in matches]
op=''
for x in s_matches:
    op=op+x
temp = " ".join(w_matches)
op=op+temp

for x in e_matches:
    op=op+x[1:len(x)]
#print([match.start() for match in matches])
#op=''
#for match in matches:
 #   st=match.start()
#for chars in matches:
 #   str=str.replace(chars[1:len(chars)-1],' ')
#print(str)
#print(' '.join(x[0] for x in matches))
#print(' '.join(x[0] for x in matches[0:len(matches)-2])+matches[len(matches) - 2][0])
import sys
print(op)
print(op)