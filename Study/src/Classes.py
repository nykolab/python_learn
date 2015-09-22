class Snake(object):
    '''
    Write a module classes.py with declaration of the class describing 
    some animal by your choice. 
    Animal should have at least 2 attributes - name, hungry, color, etc.. 
    The class also should declare at least 3 methods:
    
    1. hello() – it should print some nice words describing object (animal) name 
    
    2. some "trick" action – sound or any other – for example for sound it 
    should print something randomly chosen sound - like a "bark" 
    or "gav-gav" for dog etc.
    
    3. "feed" action – the object should have from the beginning boolean 
    "hunger" attribute equals to True (it is hungry). 
    
    After performing .feed() object should thank you and became non-hungry. 
    Second time you try to feed him it should refuse. 
    After 3 "sound" action it should became hungry again and refuse to play tricks.

    '''
    def __init__(self, name, color, venomous):
        self.name = name
        self.hungry = True
        self.venomous = venomous
    
    def hello(self):
    
    def bite(self):
    
    def feed(self):
    
    