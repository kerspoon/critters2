
#!/usr/bin/env python
"""
class Physics 
    this is the mian process, it holds the worlds and deals with updating

class DynamicBox, DynamicCircle
    these have operators like speed,position,angle,velocity
    to be updated from an Entity
    
"""
# http://www.box2d.org/wiki/index.php?title=Hello.py

import Box2D

# print Box2D.__version__      # '2.0.2b1'
# print Box2D.__version_info__ # (2,0,2,1)

class Manager(object):
    name = "physics-manager"
    priorities = (4,4)

    def initilize(self):
        # Define the size of the world. Simulation will still work
        # if bodies reach the end of the world, but it will be slower.
        worldAABB = Box2D.b2AABB()
        worldAABB.lowerBound.Set(-100, -100)
        worldAABB.upperBound.Set(100, 100)

        # Define the gravity vector.
        gravity = Box2D.b2Vec2(0, -10)
 
        # Do we want to let bodies sleep?
        doSleep = True
 
        # Construct a world object, which will hold and simulate the rigid bodies.
        Manager.world = Box2D.b2World(worldAABB, gravity, doSleep)

        self.counter = 0 
        self.update_time = 1000.0/60 # 16.666 
        

    def update(self,time_passed):
        # Prepare for simulation. Typically we use a time step of 1/60 of a
        # second (60Hz) and 10 iterations. This provides a high quality simulation
        # in most game scenarios.
        velocityIterations = 10
        positionIterations = 8

        # Instruct the world to perform a single step of simulation. It is
        # generally best to keep the time step and iterations fixed.
        # this updates every 16ms regardless of frame rate
        self.counter += time_passed
        while self.counter > self.update_time:
            self.counter -= self.update_time
            Manager.world.Step(1.0/60, velocityIterations, positionIterations)
            # print "physics step"

class StaticBox(object):
    def initilize(self, locx, locy, width, height):
        # Define the ground body.
        groundBodyDef = Box2D.b2BodyDef()
        groundBodyDef.position.Set(locx, locy)
        
        # Call the body factory which allocates memory for the ground body
        # from a pool and creates the ground box shape (also from a pool).
        # The body is also added to the world.
        groundBody = Manager.world.CreateBody(groundBodyDef)
 
        # Define the ground box shape.
        groundShapeDef = Box2D.b2PolygonDef()
 
        # The extents are the half-widths of the box.
        groundShapeDef.SetAsBox(width/2.0, height/2.0)
 
        # Add the ground shape to the ground body.
        groundBody.CreateShape(groundShapeDef)

class DynamicBox(object):
    
    def initilize(self, locx, locy, width, height):
	# Define the dynamic body. We set its position and call the body factory.
	bodyDef = Box2D.b2BodyDef()
	bodyDef.position.Set(locx, locy)
	self.body = Manager.world.CreateBody(bodyDef)
	 
	# Define another box shape for our dynamic body.
	shapeDef = Box2D.b2PolygonDef()
	shapeDef.SetAsBox(width/2.0, height/2.0)
	 
	# Set the box density to be non-zero, so it will be dynamic.
	shapeDef.density = 1
	 
	# Override the default friction.
	shapeDef.friction = 0.3
	 
	# Add the shape to the body.
	self.body.CreateShape(shapeDef)
	 
	# Now tell the dynamic body to compute it's mass properties base on its shape.
	self.body.SetMassFromShapes()
