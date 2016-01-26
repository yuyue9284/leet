__author__ = 'yuyue'


def solution(a):
    length=len(a)
    shortpath = [[[] for i in range(length)] for i in range(length)]
    for i in range(length):
        shortpath[0][i]=a[length-1][i]
    for i in range(1,length):
        for j in range(length-i):
            shortpath[i][j]=min(shortpath[i-1][j],shortpath[i-1][j+1])+a[length-i-1][j]
    return shortpath[length-1][0]


s=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print solution(s)