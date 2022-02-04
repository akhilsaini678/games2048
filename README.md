# 2048-Game
2048 Game is a web-application, which I made for the Application Based Problem for Ather.


Steps which I am doing :
    
    1. 
        a.  Created a git repository on github.
        b.  Clone it into my local disk.
        c.  Created Virtual Enviroment.
        d.  Installed Django in virtual Environment.
        e.  Starting a new Python Django App named as games2048.
        f.  Create a new app inside games2048 folder names as games2048_app (Main app in which all work will be done.)
        g.  Now , created two folder in it names as static and templates to keep HTML and CSS file.
    
    
    
    2.
        a.  View is created in views.py and a index file is created in templates.
        b.  Static Files location is set in setting.py and templates directory location is also added in setting.py.
        c.  Url path is added in urls.py.
        d.  Now app is at it's initial phase now, I am going to create simple UI for the app.

    ** Also, before going further, I am going to first deploy it on heroku.
        Reason behind this : Last time when I created a project in Django, there came some name conflict and because of that I have to copy all the files in new name folder. So, just to check if everything is okay I am going to deploy it.

    Deployment Process :
            1. Now, 3 files I need to add in my app folder
                a. runtime.txt           : Python version
                b. Procfile              : For Heroku.
                c. Requirements.txt      : All modules and framework which are needed.
            
            2. Debug = False

     Deployment is working fine.
    

    3.
        Now, it's to work on UI.
        I have created basic UI with some CSS.
        UI is completed.
        I have used divison to make UI, now I just need to put data from 2-D list from views.py function to here.

    4. 
        a.  Now it's main logic turn.
            Taking a 2-D list of size N where N is 4. And will perform all operations on it.
        
        b.  I have created 2-d list and I have added a function which will search all the empty box and then put randomly on any of the index either 2 or 4 (randomly).

