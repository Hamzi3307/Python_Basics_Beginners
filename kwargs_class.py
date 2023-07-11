class duck:
    def __init__(self, **kwargs):
        self.properties = kwargs
    def talk(self):
        print('quack')

    def set_property(self, *args):
        if len(args) != 2:raise TypeError('Expected 2 arguments, got {}'.format(len(args)))
        elif len(args) == 2:
            self.properties.setdefault(args[0],args[1])
    def get_property(self, key):
        return self.properties.get(key, None)
    def get_properties(self):
        return self.properties

def main():
    donald = duck(color='blue', fur='feathers')
    donald.set_property('voice','nice')
    print(donald.get_properties())

if __name__ == '__main__': main()