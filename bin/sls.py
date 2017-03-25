from sfml import sf

window = sf.RenderWindow(sf.VideoMode(640, 480), 
                         "pySFML Window", 
                         sf.Style.TITLEBAR | sf.Style.RESIZE)

while window.is_open:
   # process events
   for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

   window.clear() # clear screen
   window.display() # update the window
