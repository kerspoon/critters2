
import pygame 
import sys
from vec2d import vec2d as Vector

class Manager(object):
      name = "graphics-manager"
      priorities = (1,99)

      def initilize(self):
          Manager.SCREEN_HEIGHT = 512
          Manager.SCREEN_WIDTH = 512
          Manager.BG_COLOR = 150, 150, 80

          pygame.init()
          Manager.screen = pygame.display.set_mode(
              (Manager.SCREEN_WIDTH, Manager.SCREEN_HEIGHT), 
              0, 32)
          Manager.screen.fill(Manager.BG_COLOR)

      def update(self,time_passed):
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
          pygame.display.flip()
          Manager.screen.fill(Manager.BG_COLOR)

def Image(filename):
      return pygame.image.load(filename).convert_alpha()

class Bitmap(object):
      def __init__(self, location=Vector(0,0), angle=0, filename="bluecreep.png"):
            self._base_image = Image(filename)
            self.location = Vector(location)
            self.angle = angle
            self.screen = Manager.screen

      def get_angle(self):
            return self._angle

      def set_angle(self, val):
            self._angle = val
            self.image = pygame.transform.rotate(self._base_image, -self._angle)
            self.image_w, self.image_h = self.image.get_size()
            self.draw_location = self.image.get_rect().move(
                  self.location.x - self.image_w / 2, 
                  self.location.y - self.image_h / 2)

      angle = property(get_angle, set_angle)

      def render(self):
            self.screen.blit(self.image, self.draw_location)

class Rect(object):
      """http://www.pygame.org/docs/ref/draw.html
         pygame.draw.rect(Surface, color, Rect, width=0): return Rect
         pygame.surface.fill(color, rect)
         
      """
      def __init__(self, location, width, height, color):
            self.color = color
            self.rect = location[0], location[1], width, height
            self.screen = Manager.screen
            print self.color, self.rect

      def render(self):
            # self.screen.fill(self.color, self.rect)
            pygame.draw.rect(self.screen, self.color, self.rect)
