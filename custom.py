
from random import randint, choice
from vec2d import vec2d as Vector
from graphics import Manager as Graphics
from graphics import Bitmap, Vector 
import physics

class Dummy(object):
      name = "dummy"
      priorities = (9999,1)

      def initilize(self):
            box = physics.StaticBox()
            box.initilize(16, 2, 32, 4)

            self.physics = physics.DynamicBox()
            self.physics.initilize(10, 26, 1, 1)

            self.renderable = Bitmap(
                  location = Vector(
                        randint(0, Graphics.SCREEN_WIDTH), 
                        randint(0, Graphics.SCREEN_HEIGHT)),
                  angle = 35,
                  filename="bluecreep.png")

            pass 

      def update(self,time_passed):
            # self.renderable.location = convert_to_screen(self.physics.body.position)
            self.renderable.angle = self.physics.body.angle
            self.renderable.render()
            # print self.renderable.location.x, self.renderable.location.y
            print self.physics.body.position

def convert_to_screen(point):
      px, py = point
      return Vector(px*16, 512-(py*16))
