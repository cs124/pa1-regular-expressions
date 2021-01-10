# Getting the Assignment Set Up

## Preface: A Note about Windows

For this class, we strongly encourage working
in a UNIX-like operating system, as part of the class
will require working with UNIX command line tools. 
Having a UNIX-like environment set up will also make it easier for us to 
help you set up other parts of the course (like running your Jupyter notebooks 
and setting up your Python environment and dependencies).

In addition, most of the future courses you'll take in the CS department, 
irrespective of specialization, will work in UNIX-like environments and expect 
that you're familiar with them, so it's a very useful skill set to learn.

With that said, if your personal computer runs Windows and you don't currently
have access to a Linux or macOS alternative, __don't worry__. There are good
options available for Windows, and instructions for how to get things set
up are provided below.

## [WINDOWS ONLY] - Setting up Ubuntu for Windows

1. To get a working Linux environment set up on your Windows machine, we
recommend using Ubuntu for Windows 10. It requires that you have an installation
of Windows 10 which includes [this update](https://support.microsoft.com/en-gb/help/4028685/windows-10-get-the-fall-creators-update). 
If you have an up-to-date Windows 10 installation, you are all set. 
If you do not have the update installed, you should go ahead and update from
Windows settings, or follow the specific instructions in the link above to 
install it. If you have an older version of Windows, like Windows 7 or 8, you 
will need to [upgrade to Windows 10 first](https://www.microsoft.com/en-us/software-download/windows10ISO) (it's free).
If for some reason you're not able to upgrade to Windows 10, please contact the
teaching staff on Piazza or via the staff email address as soon as possible!
   
2. Follow the instructions [here](https://ubuntu.com/tutorials/ubuntu-on-windows#1-overview)
to install Ubuntu for Windows.
3. Once the installation process is complete, try opening an Ubuntu terminal
   window to verify that everything works.
4. If so, you're all set and can continue to the next section, Running Locally!

## [RECOMMENDED] - Running Locally

1. Install Python 3.9.1:
   - __[macOS]__ Download the Python 3.9.1 installer from here: 
     https://www.python.org/downloads/. Once it's downloaded, run the installer
     through to completion.
   - __[Linux/Ubuntu for Windows]__ Run Ubuntu to start a terminal, then run
   
         sudo apt update
         sudo apt install wget software-properties-common
         sudo add-apt-repository ppa:deadsnakes/ppa
         sudo apt update
         sudo apt install python3.9
    
2. Open a terminal if you haven't already (terminal for macOS or Linux, or run
   Ubuntu for Windows).
3. First, run 
   
        python3.9 --version

    You should see 
   
        Python 3.9.1

    If so, your installation of Python was successful!

4. Install pipenv:
    - __[macOS]__:
        
            curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python3.9
   
    - __[Linux/Ubuntu for Windows]__
     
            sudo apt install python3.9-distutils
            curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | sudo python3.9
    
4. Clone the git repository for PA1 in a location of your choice:
      
        git clone https://github.com/cs124/pa1-spamlord.git
   
5. Enter the project root directory and create a Python virtual environment 
   with all dependencies: 
   
        cd pa1-spamlord
        pipenv install
   
8. Activate the newly created environment:
        
        pipenv shell
   
    You should now see `(pa1-spamlord)` in front of your shell prompt. 
   You'll need to do this every time you open a new terminal and re-start your
   notebook server.
9. Start up your jupyter notebook server

        jupyter notebook

10. A window should open automatically in your default browser. If it didn't,
    the terminal output should contain a URL you can use to open the
    notebook in a browser of your choice.
11. From the Jupyter notebook file explorer window that opens, click on the
SpamLord.ipynb file to open it.


## [ALTERNATIVE] - Google Colaboratory

1. Go to [colab.research.google.com](http://colab.research.google.com). 
   If prompted to open a notebook, hit cancel for now. You should double-check 
   that you are logged in to your Stanford Google account. If not, you can 
   switch accounts in the top right.
2. Now go to File->Open Notebook. You have two options:

    -  __[Option 1 - Recommended]__ If you have a GitHub account, you can go to the
   Github tab. It will ask you to log in. Once you've done that, copy and paste 
   the URL: 
   https://github.com/bryankim96/test-cs124-pa1-spamlord into the search box and hit enter. It should show:
   
            Repository: bryankim96/test-cs124-pa1-spamlord
            Branch:  Master

        Click on SpamLord.ipynb below to load the notebook.

    - __[Option 2 - No GitHub]__ Download the SpamLord.ipynb notebook file 
      from Canvas to your local machine, click the Upload tab to select and upload it.
      

## [NOT RECOMMENDED] - Running on Rice/Myth

Rice is the name of a group of machines made available for student use
by Stanford. Myth machines are similar, but specifically maintained by and
for the computer science department. For our purposes, they are interchangeable
so you should feel free to use whichever one you prefer.

0. __[WINDOWS ONLY]__ If you are using Windows, you have two options. If you
were able to install Ubuntu for Windows according to the instructions above,
you can use that for your terminal/shell to SSH into Rice/Myth (although, if 
you were able to get Ubuntu for Windows set up we would strongly recommend that
you try to get things working locally instead of using Rice/Myth). If you
weren't able to install Ubuntu for Windows, you can instead download and install
PuTTY [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
to use as an SSH client. Install and run it. 

1. SSH into Rice/Myth.
   - __[macOS/Linux/Ubuntu for Windows]__

            ssh [Your SUNet]@rice.stanford.edu
            # OR
            ssh [Your SUNet]@myth.stanford.edu

   - __[Windows]__ Run PuTTY and when prompted, enter `rice.stanford.edu` or
    `myth.stanford.edu` in the box labeled Host Name. Do not change any of the
     other settings. Click open to open a connection, which will cause a 
     terminal window to pop up. You will then be prompted to log in.

    You'll be prompted for your Stanford SUNet account password. 
   You will also likely be asked to authenticate using 
   2-factor authentication.
2. Once you've SSH'd into Rice or Myth, install pipenv by running the following 
   command:
   
        pip install --user pipenv 
   
3. Once it has finished, copy and run the following commands in your terminal 
   to allow you to use pipenv from the command line:
       
        echo 'export PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"' >> ~/.bashrc
        echo 'export PATH="$PATH:$PYTHON_BIN_PATH"' >> ~/.bashrc
        source ~/.bashrc

4. Clone the git repository for PA1 in a location of your choice:
      
        git clone https://github.com/cs124/pa1-spamlord.git
   
5. Enter the project root directory and create a Python virtual environment 
   with all dependencies: 
   
        cd pa1-spamlord
        pipenv install --python 3
   
8. Activate the newly created environment:
        
        pipenv shell
   
    You should now see (pa1-spamlord) in front of your shell prompt. You'll need
   to do this every time you open a new terminal and re-start your notebook 
   server.
9. Start up your jupyter notebook server without a browser.

        jupyter notebook --no-browser --port=[pick a number from 1025 to 65535]

10. You now need to set up port forwarding from Rice/Myth to your local machine:

   - __[macOS/Linux/Ubuntu for Windows]__ Open a new terminal window on your
    local machine (NOTE: don't close the one on Rice/Myth, that one needs to
     stay open) and enter the following command:

            ssh -NL [local port you'd like to use]:localhost:[port number you picked on rice/myth] [SUNet]@[rice/myth].stanford.edu

    If it worked correctly, nothing should happen and your terminal will appear 
    to hang. This is fine, you should keep it open to maintain the tunnel.

   - __[Windows]__ Go back to your PuTTY window. In the left-side navigation
    window and select Connection->SSH->Tunnels. In the right-hand side window,
     there will be a section labeled "Add new forwarded port". 
     
    Under Source port, type the local port you'd like to forward to. 
    Destination, type:

        [rice/myth].stanford.edu:[port your Jupyter notebook server is running on]
     
    Then, click "Add".

11. Finally, try opening a browser of your choice (i.e. Chrome, Firefox, Safari)
    and opening the URL:
    
        localhost:[local port number you chose]

    If everything worked correctly, you'll see the Jupyter file
    explorer. It may prompt you for an authentication token. If it does,
    go back to the terminal window that is running the Jupyter notebook server
    (on Rice/Myth). In the output, you should see some URLs with a portion that
    looks like "token=...". Copy the token from there and paste it into your
    browser where requested.






# Submitting your Solution

## Running Locally (macOS/Linux)

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).

## Running Locally (Ubuntu for Windows)

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. The 

## Google Colaboratory

1. Once you've saved all your changes, go to File->Download .ipynb to download
your notebook file to your local machine.
2. If your solution required any extra files, make sure they were located in
pa1-spamlord/deps. Go to the file explorer on the left-hand side and download
those as well.
3. Once you have SpamLord.ipynb and any deps files you need saved locally,
create a zip file (either from your OS's file explorer or the terminal), making
sure that it has the following structure:
   
        deps/
        SpamLord.ipynb

3. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).

## Running on Rice/Myth

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. You will then need to download/copy the zip file from Rice/Myth to your
local machine.
   
   - __[macOS/Linux/Ubuntu for Windows]__

            scp 
    
        If you're using Ubuntu for Windows, see the section above on
        "Running Locally (Ubuntu for Windows)" for how to access files on your
        Ubuntu filesystem from Windows.

   - __[Windows]__ PSCP is another utility that should have been installed
    automatically when you installed PuTTY earlier. Find and run it. In the
     terminal window, you can run the command:
     
            pscp [Your SUNet]@rice.stanford.edu:/path/to/submission.zip c:\temp\submission.zip
    
    to download the file from Rice/Myth to your local machine. You should now
   be able to access the file locally at c:\temp\submission.zip
   
3. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).