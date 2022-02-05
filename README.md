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

    ** The main problem is here with me that I want to call a function from frontend in my views.py. So for this purpose either I have to use ajax or fetch API to send a request to a URL, but to keep it simple I am using a framework of django which will "call" Python functions from the front-end HTML (it provides the infrastructure so I don't have to create AJAX endpoints or deal with serializing data).

        c. So, it was the first time, I was using unicorn.
            What changes I need to do , when using unicorn.
                a. A new unicorn specific app is created, I named it as "unicorn_folder".
                b. I added a component inside it named as "component1". 
                c. So, component one contain both template folder and components folder.
                d. My complete logic is in component folder -> component1.html. I have to do this because I need to update grid without refreshing.
                e. All the template related to grid is in templates -> component1.html.
                f. I have to pass the arr and score variable from views.py to index.html and from index.html I am using it in unicorn folder.

    5. Now, it's time to fix bugs.

    6.

    Basic structure and logic of my program.

    There are 6 operations which I am doing :

    1. Left_shift.
    2. Right_shift.
    3. Up_shift.
    4. Down_shift.
    5. After shifting or in the start of the game, use an empty index and put a random value either 2 or 4.
    6. Score updation.

    Now, all these operations are in working condition.
    If there is any bug, then I need to find that.



