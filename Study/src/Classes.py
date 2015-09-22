# -*- coding: utf-8 -*-
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

    def __init__(self, name, color):
        self.name = name
        self.hungry = True
        self.action = 0
        self.color = color
    
    def hello(self):
        if self.action > 3:
            self.hungry = True
        if not self.hungry:
            if self.name and self.color:
                print "I'm {} snake, my name is {}".format(self.color, self.name)
            elif self.name:
                print "I'm snake, my name is {}".format(self.name)
            elif self.color:
                print "I'm {} snake".format(self.color)
            else:
                print "I'm {} snake"
            self.action += 1
        else:
            print "You need to feed me before"
        
    def bite(self):
        if self.action > 3:
            self.hungry = True
        if not self.hungry:
            print "I'm biting you!!!"
            self.action += 1
        else:
            print "You need to feed me before"
    
    def feed(self):
        if self.hungry:
            print "Thanks"
            self.hungry = False
        else:
            print "I'm not hungry"    

# ===============================================

if __name__ == '__main__':
    a = Snake("Snakky","Black")
    a.name = "Doggy"
    a.hello()
    a.bite()
    a.bite()
    a.bite()
    a.bite()
    a.feed()
    a.hello()
    a.bite()
    a.bite()
    a.bite()
    a.bite()
    
    