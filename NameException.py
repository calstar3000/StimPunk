class NameException(Exception):
    '''Defines a name exception'''
    
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return self.value
