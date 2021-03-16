# PA1 - SpamLord

## Getting the Assignment

You can get started using the same steps you followed for PA0. To recap,
you'll want to:

1. Open a terminal (terminal for macOS and Linux, 
   Ubuntu for Windows for Windows, or SSH into Rice/Myth) the same way you did for PA0. 

1. Clone the git repository for PA1 in a location of your choice:
      
        git clone https://github.com/cs124/pa1-spamlord.git
   
2. Enter the project root directory and activate your cs124 conda environment 
   (you should have already created this as part of PA0. If not, please go 
   back and follow the instructions there): 
   
        cd pa1-spamlord
        conda activate cs124
   
    You should now see `(cs124)` in front of your shell prompt. 
   You'll need to do this every time you open a new terminal or re-start your
   notebook server.
3. Start up your jupyter notebook server

        jupyter notebook

4. A window should open automatically in your default browser. If it didn't,
    the terminal output should contain a URL you can use to open the
    notebook in a browser of your choice.
5. From the Jupyter notebook file explorer window that opens, click on the
pa1.ipynb file to open it. All your implementation will be done directly in the notebook.

# Submitting your Solution

## macOS/Linux

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).

## Ubuntu for Windows

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. To access the file easily from Windows (which you'll need to do if you
   want to upload it to Gradescope), you'll probably want to move or copy
   it to an easily accessible location in your Windows filesystem. The C
   drive in Windows is accessible in Ubuntu at `/mnt/c`, so you should copy
   it to some path there, like `/mnt/c/Users/[your Windows username]/Desktop`,
   which is the path to your Windows desktop directory.
   You can do this from your Ubuntu terminal by doing:
   
        cp /path/to/submission.zip /mnt/c/Users/[your Windows username]/Desktop

3. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).

## Google Colaboratory

1. Once you've saved all your changes, go to File->Download .ipynb to download
your notebook file to your local machine.
2. If your solution required any extra files, make sure they were located in
pa1-spamlord/deps. Go to the file explorer on the left-hand side and download
those as well.
3. Once you have pa1.ipynb and any deps files you need saved locally,
create a zip file (either from your OS's file explorer or the terminal), making
sure that it has the following structure:
   
        deps/
        pa1.ipynb

3. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).

## Rice/Myth

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. You will then need to download/copy the zip file from Rice/Myth to your
local machine.
   
   - __[macOS/Linux/Ubuntu for Windows]__
    
        Open a terminal on your local machine and run the following command to
        copy the submission zip file from Rice/Myth to your local machine.

            scp [SUNet ID]@[myth/rice].stanford.edu:/path/to/submission.zip /local/path/to/copy/to
    
        If you're using Ubuntu for Windows, we recommend choosing as your local
        path something starting with `/mnt/c`, as this is the UNIX path
        that corresponds to your Windows filesystem. This allows you to download
        the zip file to a location where it can be easily accessed directly
        from windows. For example, if you chose `/mnt/c/Users/[your Windows username]/Desktop`
        as your destination, the file will be saved to your Windows Desktop folder.

   - __[Windows]__ PSCP is another utility that should have been installed
    automatically when you installed PuTTY earlier. Find and run it. In the
     terminal window, you can run the command:
     
            pscp [Your SUNet]@rice.stanford.edu:/path/to/submission.zip c:\temp\submission.zip
    
    to download the file from Rice/Myth to your local machine. You should now
   be able to access the file locally at c:\temp\submission.zip
   
3. Upload the zip file as your solution to the PA1 SpamLord assignment in 
   Gradescope (http://www.gradescope.com).
