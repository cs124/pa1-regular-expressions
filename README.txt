Instructions for running the notebook:

[RECOMMENDED] - Google Colaboratory

1.

[ALTERNATE] - Running locally (Windows)

1. Install Ubuntu for Windows (https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6)
2.

[ALTERNATE] - Running locally (Linux/Mac OS)

1. Download and install Python 3.5.2 from here:

[LAST RESORT] - Running on Rice/Myth

1. Login to Rice at [SUNet]@rice.stanford.edu or Myth at
 [SUNet]@myth.stanford.edu. Your password will be your Stanford SUNet account
 password. You will also likely be asked for 2-factor authentication.
2. Install pipenv: "pip install --user pipenv"
3. Copy and run the following commands to allow you to use pipenv from the
command line:
    echo 'export PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"' >> ~/.bashrc
    echo 'export PATH="$PATH:$PYTHON_BIN_PATH"' >> ~/.bashrc
    source ~/.bashrc
4. Upload the assignment zip file:
5. Unzip it: ""
6. Go to project root directory: "cd ___"
7. Create an environment and install all dependencies: "pipenv install"
8. Activate your environment: "pipenv shell". You should now see () in
front of your shell prompt.
9. Start up your jupyter notebook server: "jupyter notebook --no-browser --port=8887"
10.

