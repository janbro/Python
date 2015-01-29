class Totient:
    def __init__(self, n):
        self.totients = [1 for i in xrange(n)]
        for i in xrange(2, n):
            if self.totients[i] == 1:
                for j in xrange(i, n, i):
                    self.totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]
if __name__ == '__main__':
    from itertools import imap
    totient = Totient(32002880064)
    print sum(imap(totient, xrange(10000)))
