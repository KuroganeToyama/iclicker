# iClicker Data Collection Tool

## Description
This tool automatically performs login to iClicker Cloud, access each class section and download all data files. <br> <br>
This tool is developed for CS 135 ISAs at the University of Waterloo to easily collect iClicker data, due to the lack of official APIs.

## Setup
- Make sure you have Google Chrome installed (I'm too lazy to make it available for other browsers).
- Clone this repo to your local machine.
- At the root directory of the repo, run `python -m venv venv` to create a virtual environment (in this case, a folder named `venv`).
- Activate the virtual environment.
    - If you're on Windows, run `.\venv\Scripts\activate` at the root directory of the repo.
    - If you're on MacOS and Linux, run `source ./venv/bin/activate` at the root directory of the repo.
- Now, at the root directory of the repo, run `pip install -r requirements.txt` to install all dependencies.
- At the root directory of the repo, create a copy of `config_sample.py` and rename it as `config.py`. Fill in `config.py` all the required configurations.

## Usage
- Run `python iclicker.py` and view your downloaded files at the `DOWNLOAD_PATH` you specified.

## Note
- The tool assumes the polls are named "Class XX - Poll".
- I'D REALLY APPRECIATE IT IF YOU CAN ENSURE THE INSTRUCTORS DO NOT DO THINGS THEIR OWN WAY AND SIMPLY STICK TO THIS POLL NAMING FORMAT. WHY CAN WE NEVER HAVE CONSISTENCY? IT'S JUST SO NICE TO HAVE CONSISTENCY.
- This tool is more relevant in Fall, for it is the only term with multiple sections.