class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

if __name__ == '__main__':

    k = CountFromBy()
    print('k = %s' % k)

    l = CountFromBy(100)
    print('l = %s' % l)
    l.increase()
    print('l = %s' % l)

    m = CountFromBy(100, 10)
    print('m = %s' % m)
    m.increase()
    print('m = %s' % m)

    n = CountFromBy(i=15)
    print('n = %s' % n)
    n.increase()
    print('n = %s' % n)
