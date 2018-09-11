import os
import sys
import datetime
sys.path.insert(0, 'venv/Lib/site-packages')

while True:
    if os.path.exists('install.ini'):
        print('importing app at %s' % datetime.datetime.now())
        from app import app
        print('importing layout at %s' % datetime.datetime.now())
        from app import layout
        print('importing GUIVar at %s' % datetime.datetime.now())
        from config import GUIVar
        print('importing app.functions.* at %s' % datetime.datetime.now())
        from app.functions import *

        for key in GUIVar.keys:
            app.bindKey(key, key_press)

        print('starting app at %s' % datetime.datetime.now())
        app.go()
        break
    else:
        try:
            from installation import *
            inst.go()
        except:
            print('installation failed')
            break
