import pygame 
import graphics
import physics
import entity
import custom

class Ping(object):
      name = "ping"
      priorities = (99999,99999)

      def initilize(self):
            print "ping"
            self.counter = 0 
            self.ping_time = 1000
            pass 

      def update(self,time_passed):
            self.counter += time_passed
            if self.counter > self.ping_time:
                  self.counter -= self.ping_time
                  print "ping"
            pass 

class ProcessManager(object):
      def __init__(self):
            self.processes = []
            self.initilized = False

      def add(self,process):
            if self.initilized:
                  raise Exception("can't do that")
            if self.get(process.name):
                  raise Exception("you already added " + process.name)
            self.processes.append(process)

      def get(self, name):
            for item in self.processes:
                  if name == item.name:
                        return item
            return None

      def initilize(self):
            if self.initilized:
                  raise Exception("can't do that")
            self.initilized = True
            self.process_init_list = sorted(self.processes,lambda x, y: cmp(x.priorities[0],y.priorities[0]))
            self.process_update_list = sorted(self.processes,lambda x, y: cmp(x.priorities[1],y.priorities[1]))

            for item in self.process_init_list:
                  print "initilize", item.name
                  item.initilize()
            
      def update(self,time_passed):
            if not self.initilized:
                  raise Exception("can't do that")
            quitting = False
            for item in self.process_update_list:
                  # print "update", item.name
                  if item.update(time_passed) == False:
                        quitting = True
            return not quitting

class Kernel(object):
      def __init__(self):
            self.clock = pygame.time.Clock()
            self.pm = ProcessManager()
            self.pm.add(physics.Manager())
            self.pm.add(graphics.Manager())
            self.pm.add(entity.Manager())
            self.pm.add(custom.Dummy())
            self.pm.add(Ping())
            self.pm.initilize()

      def update(self):
            time_passed = self.clock.tick(60)
            return self.pm.update(time_passed)

def main():
      kernel = Kernel()
      while(kernel.update()):
            continue
      print "done"
main()
