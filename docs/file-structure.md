### How the File Structure Works

Every subfolder has an init python script. This is for identifying a directory as a python package, you can leave it empty or you can also use it to simplify imports. Don't write any actual code here keep it VERY simple.

For example, a User class is written in the models folder in user.py. You can write
</br> ```from .user import User in init.py ``` </br>
other modules can import it by writing
</br> ```from productivity_app.models import User``` </br>

On the other hand, main.py provides the startup code when you run the app, so the GUI would be started there as well as its loop then the screens for each other part can be written and designed in the folder where the feature is meant located. For example, the login screen would be designed in gui/ but not started yet. Hence, main will be the only place where a window is created

What the folder names mean:
gui/ - where gui designs live
services/ - where any actions, permission checks and other services are located e.g. login verification
users/ - where user data is stored, e.g. admin and manager classes

ps you can make new subfolders if you have lots of files for some feature(s) and want to keep them organised, just make sure there's an init.py in that folder