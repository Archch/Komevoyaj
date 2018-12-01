#a, b, c, d, e, f, g, h = range(8)
#N = [
#	{b:3, c:2, d:1, e:4, f:8}, # a
#	{c:2, e:4}, # b
#	{d:1}, # c
#	{e:4}, # d
#	{f:8}, # e
#	{c:2, g:9, h:4}, # f
#	{f:8, h:4}, # g
#	{f:8, g:9} # h
#]

#print(N)
a, b, c, d = range(4)
# a b c d
N =  [[0,3,1,8], # a
	 [3,0,4,4], # b
	 [1,4,0,7], # c
	 [8,4,7,0], # d
]
print(N)
ma = N[1][1]
for i in range (4):
    for j in range(4):
        if N[i][j]>ma:
            ma=N[i][j]
print(ma)