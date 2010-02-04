
About
=====

A 2D game made using Python, Pygame, and Box2d.

You have 10 seconds to get as much food as you can. 

100 pieces of food that are static bitmaps. 
a countdown timer with an onscreen text display
you a move-able bitmap, controlled with `wasd`


BUGS
====

  + there is a gap between the graphical sprites when under physics. 

TODO
====

  + There should be no singletons or global variables! e.g. remove Manager.SCREEN_HEIGHT. 
  + add render order, or depth. 
  + add an easy way to input new entity instances at start up
  + deal with collision, i.e. collision response
  + add input class
  + add game_states or something
  + add lipy as a process so I can change and add thins automatically
  + add neural net
  + add genetic algorithm
  + make ga control neural net 

Notes
=====

Anything that needs to Render must have `graphics.manager` passed in its constructor. That way we can swap out other Renderers without having to change other classes. It will also make it easier to test. In the same way Physics must be passed into the constructor is used. 


Classes & Files
====

Kernel & ProcessManager
----

State
----

Entity
----

Physics
----

Graphics
----


box(renderable, physicsobject)
