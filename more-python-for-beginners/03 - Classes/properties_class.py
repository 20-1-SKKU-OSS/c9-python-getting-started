class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
        
        #getter function
        @property
        def name(self):
            print('Retrieving name...')
            return self.__name
        
        #setter function
        @name.setter
        def name(self, value):
            # cool validation here
            print('Validating name...')
            self.__name = value

presenter = Presenter('Chris') 
presenter.name = 'Christopher'
print(presenter.name)
