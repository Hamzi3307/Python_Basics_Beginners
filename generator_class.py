class InclusiveRange:
    def __init__(self, *args):
        numarg = len(args)
        if numarg<1 : raise TypeError('At least one argument required')
        elif numarg==1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numarg==2:
            (self.start,self.stop) = args
            self.step = 1
        elif numarg==3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError('Expected at most 3 arguments, got {}'.format(numarg))

    def __iter__(self):
        j = self.start
        while j <= self.stop:
            print(j,end=' ')
            j += self.step
def main():
    print('Range is a builtin class which give us the number\nexcluding the one we give it')
    o = range(1,25)
    for i in o : print(i, end=' ')
    print('\nInclusive Range is a user class which give us the number\nincluding the one we give it')
    for i in InclusiveRange(2,8,3):
        print(i,end=' ')

if __name__ == '__main__': main()