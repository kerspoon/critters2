
from random import randint, choice
from vec2d import vec2d as Vector
from graphics import Manager as Graphics
from graphics import Bitmap, Vector, Rect
import physics

class Dummy(object):
      name = "dummy"
      priorities = (9999,1)

      def initilize(self):
            w = Graphics.SCREEN_WIDTH - 10 
            h = Graphics.SCREEN_HEIGHT - 10
            #                  x  y    w   h     r    g    b 
            self.rect1 = Rect((0, 0), 10, 10, (255,   0,   0)) # top-left     : red
            self.rect2 = Rect((0, h), 10, 10, (  0, 255,   0)) # bottom-left  : green 
            self.rect3 = Rect((w, 0), 10, 10, (  0,   0, 255)) # top-right    : blue
            self.rect4 = Rect((w, h), 10, 10, (255, 255, 255)) # bottom-right : white
            pass 

      def update(self,time_passed):
            self.rect1.render()
            self.rect2.render()
            self.rect3.render()
            self.rect4.render()
            pass
