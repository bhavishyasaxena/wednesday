import os
import eel


    
eel.init("www")

os.system('start msedge.exe --app="http://localhost:5500/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)