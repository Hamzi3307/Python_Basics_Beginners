class egg:
    def __init__(self, kind= 'fried'):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = egg()
    scram = egg('scrambled')
    print("{} egg \n{} egg".format(scram.whatKind(), fried.whatKind()))

if __name__ == "__main__":
    main()