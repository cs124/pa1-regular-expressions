# PA1 - Regular Expressions and BPE Tokenization

## Recommended before Starting

We recommend checking out the following before getting started on PA1:

* The Week 2 videos and slides.
* Lab 1 slides.
* Chapter 2 of Jurafsky and Martin (3rd ed.), particularly section 2.1
and sections 2.4.1, 2.4.2, 2.4.5.


## Getting the Assignment

### Jupyter Notebook

You can get started using the same steps you followed for PA0. To recap,
you'll want to:

1. Open a terminal (terminal for macOS and Linux, 
   Ubuntu for Windows for Windows, or SSH into Rice/Myth) the same way you did 
   for PA0. 

2. Clone the git repository for PA1 (this repository) into a folder of your 
   choice by typing this in your terminal:
      
        git clone https://github.com/cs124/pa1-regular-expressions.git

3. Enter the project root directory and activate your cs124 conda environment by
   doing:
   
        cd pa1-regular-expressions
        conda activate cs124
   
    You should now see `(cs124)` in front of your shell prompt. 

   You'll need to do this every time you open a new terminal and re-start your
   notebook server. You should have already created this conda enviornment 
   as part of PA0. If not, and you encounter an error, please go back and 
   follow the instructions there.

4. Follow the steps outlined in your setup guide for PA0 to open `pa1.ipynb`.

# Submitting your Solution

## macOS/Linux

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. Upload the zip file as your solution to the PA1 Regular Expressions assignment in 
   Gradescope (http://www.gradescope.com).

## Ubuntu for Windows

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. Run the following command to transfer that zip file over from WSL to your local computer:

      cp ~/cs124/pa1-regular-expressions/submission.zip /mnt/c/Users/YOUR_USER_NAME/OneDrive/Desktop/

   Note that you may want to replace OneDrive/Desktop/ with another destination folder based on your preferences.

   You can then upload submission.zip to Gradescope. And you are all done!

## Rice/Myth

1. You can run the cell at the bottom of the Jupyter notebook to zip up your
solution for you. It should generate a zip file `submission.zip`.
   
2. You will then need to download/copy the zip file from Rice/Myth to your
local machine.
   
   - __[macOS/Linux/Ubuntu for Windows]__
    
      After you have created the submission zip, first, run this command to find where the submission zip is:

            pwd

      This should return something like

            /afs/.ir/users/YOUR/SUNET/ID/cs124/pa1-regular-expressions

      Copy that command and append submission.zip to it:

            /afs/.ir/users/YOUR/SUNET/ID/cs124/pa1-regular-expressions/submission.zip

      Then, cd into a local folder where you'd like to save the submission zip, and use the following command to copy the zip from Myth to your local machine:

         scp -r [SUNet]@[rice/myth][rice/myth machine number].stanford.edu:/afs/.ir/users/YOUR/SUNET/ID/cs124/pa1-regular-expressions/submission.zip .
      
      You can replace . with a relative path to a local directory you'd like to copy the zip file to.

   - __[Windows]__ PSCP is another utility that should have been installed
    automatically when you installed PuTTY earlier. Find and run it. In the
     terminal window, you can run the command:
     
            pscp [Your SUNet]@rice.stanford.edu:/path/to/submission.zip c:\temp\submission.zip
    
    to download the file from Rice/Myth to your local machine. You should now
   be able to access the file locally at c:\temp\submission.zip
   
3. Upload the zip file as your solution to the PA1 Regular Expressions assignment in 
   Gradescope (http://www.gradescope.com).
