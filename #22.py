__author__ = 'yuyue'

"""
def solution(n):
    result = [[] for i in range(n*2)]

    def recur(l, r, n, position, result):
        if position==2*n-1:
            result[position] = ')'
            print str(result)
            return
        if l < n:
            result[position] = '('
            recur(l + 1, r, n, position + 1, result)
        if r < l:
            result[position] = ')'
            recur(l, r + 1, n, position + 1, result)

    recur(0, 0, n, 0, result)

solution(3)"""


def solution(n):
    tempresult = [[] for i in range(n * 2)]
    result = []

    def recur(l, r, n, position, result, final):
        if position == 2 * n - 1:
            result[position] = ')'
            final.append(''.join(result))
            return
        if l < n:
            result[position] = '('
            recur(l + 1, r, n, position + 1, result, final)
        if r < l:
            result[position] = ')'
            recur(l, r + 1, n, position + 1, result, final)

    recur(0, 0, n, 0, tempresult, result)
    print result


solution(3)
