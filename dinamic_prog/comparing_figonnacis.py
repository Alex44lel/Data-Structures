def fib2(n):
    if n == 0 or n == 1:
        return n
    return fib2(n - 1) + fib2(n - 2)

#print(fib2(35))

class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError(
                'Index was negative. '
                'No such thing as a negative index in a series.'
            )

        # Base cases
        if n in [0, 1]:
            return n

        # See if we've already calculated this
        if n in self.memo:
            print("grabbing memo[%i]" % n)
            return self.memo[n]

        print("computing fib(%i)" % n)
        result = self.fib(n - 1) + self.fib(n - 2)

        # Memoize
        self.memo[n] = result

        return result


print(Fibber().fib(35))