def getPermutation(self,n, k):
        if n == 1:
            return "1"

        result = ""
        choice = [(i + 1) for i in range(n)]

        Pw = [1]
        for i in range(n - 1):
            Pw.append(Pw[-1] * (i + 2))

        if k / Pw.pop(-1) == 1:
            for i in range(n):
                result += str(choice[n - 1 - i])
        else:
            while True:
                tmp = Pw.pop(-1)
                num = k / tmp
                k -= num * tmp
                if k == 0:
                    result += str(choice.pop(num - 1))
                    for i in range(len(choice)):
                        result += str(choice[-1-i])
                    break
                else:
                    result += str(choice.pop(num))
                if tmp == 1:
                    result += str(choice[0])
                    break

        return result


