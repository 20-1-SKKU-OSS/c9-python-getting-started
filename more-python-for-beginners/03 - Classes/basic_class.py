class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
    def say_hello(self):
        # Method
        print('Hello, ' + self.name)

presenter = Presenter('Chris')
presenter.name = 'Christopher'
presenter.say_hello()
