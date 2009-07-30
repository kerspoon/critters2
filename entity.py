


class Manager(object):
      name = "entity-manager"
      priorities = (4,4)

      def initilize(self):
            self.entities = []

      def update(self,time_passed):
            for item in self.entities:
                  item.update(time_passed)

      def add(entity):
            self.entities.append(entity)


