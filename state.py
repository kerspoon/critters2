


class Manager(object):
    name = "state-manager"
    priorities = (9999,100000)
    
    def initilize(self):
        state = Main()
        state.initilize()
        pass 
    
    def update(self,time_passed):
        state.update(time_passed)
        pass
    
class Main(object):
    
    def initilize(self):
        pass 
    
    def update(self,time_passed):
        pass
    
