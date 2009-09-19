
from graphics import Manager as Graphics
from graphics import Bitmap, Vector, Rect
import physics


class Manager(object):
      name = "entity-manager"
      priorities = (4,4)

      def initilize(self):
            self.entities = []
            # self.add(read_Entity("DynamicBox, 15, 26, 1, 1, bluecreep.png"))
            self.add(read_Entity("DynamicBox, 1, 32, 1, 1, bluecreep.png"))
            self.add(read_Entity("StaticBox, 16, 0, 32, 10, 255, 100, 0"))

      def update(self, time_passed):
            for item in self.entities:
                  item.update(time_passed)

      def add(self, entity):
            self.entities.append(entity)

def phy_point_to_gfx(point):
      px, py = point
      return px*16.0, 512.0-(py*16.0)

def gfx_point_to_phy(point):
      gx, gy = point
      return gx/16.0, (gy-512.0)/16.0

def pbox_to_gbox(px, py, pw, ph):
      gx, gy = phy_point_to_gfx((px, py))
      gw, gh = pw * 16.0 , ph * 16.0
      gx, gy = gx - gw/2.0 , gy - gh/2.0
      return gx, gy, gw, gh 

def gbox_to_pbox(gx, gy, gw, gh):
      px, py = gfx_point_to_phy((gx, gy))
      pw, ph = gw / 16.0 , gh / 16.0
      px, py = px + pw/2.0 , py + ph/2.0
      return px, py, pw, ph



def read_Entity(text):
      entity = None
      cols = [x.strip() for x in text.split(",")]
      assert len(cols) > 1

      if cols[0] == "DynamicBox":
            locx, locy, width, height, filename = cols[1:]
            entity = DynamicBox()
            entity.initilize(float(locx), float(locy), float(width), float(height), filename)

      elif cols[0] == "StaticBox":
            locx, locy, width, height, red, green, blue = cols[1:]
            entity = StaticBox()
            entity.initilize(float(locx), float(locy), 
                             float(width), float(height), 
                             float(red), float(green), float(blue))
            
      assert entity != None
      return entity

class DynamicBox(object):
      """A box with a bitmap and physics
         Has no AI at all.
         # type, locx, locy, width, height, filename
         DynamicBox, 10, 26, 1, 1, bluecreep.png
      """
      def initilize(self, locx, locy, width, height, filename):
            self.physics = physics.DynamicBox()
            self.physics.initilize(locx, locy, width, height)
            self.physics_size = [width, height]
            rect = pbox_to_gbox(locx, locy, width, height)
            self.renderable = Bitmap(rect[:2], 0, filename)

      def update(self, time_passed):

            rect = list(self.physics.body.position) + self.physics_size
            #            print "rect ", rect 
            self.renderable.location = Vector(pbox_to_gbox(*rect)[:2])
            self.renderable.angle = self.physics.body.angle
            self.renderable.render()
            # print self.renderable.location.x, self.renderable.location.y,
            # print self.physics.body.position


class StaticBox(object):
      """A box with a bitmap does not move!
         Has no AI at all.
         # type, locx, locy, width, height, red, green, blue
         StaticBox, 16, -5, 32, 10, 255, 100, 0 
      """
      def initilize(self, locx, locy, width, height, red, green, blue):
            self.physics = physics.StaticBox()
            self.physics.initilize(locx, locy, width, height)

                  # convert_to_screen([locx,locy]), 
                  # width, height, 
            rect = pbox_to_gbox(locx, locy, width, height)
            self.renderable = Rect(
                  rect[:2], rect[2], rect[3], 
                  (red, green, blue))

      def update(self, time_passed):
            self.renderable.render()
            pass 
