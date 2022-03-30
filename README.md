# Setting up QA Automation 

### Creating working directory and pulling the framewrok from GitHub
```
mkidir ~/qa
```
Navigate to working directory
```
cd qa
```
Cloning the repo
```
git clone git@github.com:privatepracticesaas/qa.git
```
### Install the required framework and libraries
Install python and virtual enviroment
```
sudo pip install virtualenv
brew install python
virtualenv -p python3 <env_name>
source <env_name>/bin/activate
```

Install the required libraries
```
pip install -r requirements.txt
```
### List of Browsers
Tests can be executed on 2 versions of Chrome (chrome74 and chrome79), safari and firefox.

#### Safari

To execute tests on Safari, you need to download [Safari Technology Preview](https://developer.apple.com/safari/download/). 
To prepare Safari Technology Preview for remote automation:
1.	Enable Develop menu in the Safari browser, `click Safari Technology Preview > Preferences > Advanced Tab`  
Select the `Show Develop Menu` check box. The Develop menu appears in the menu bar.
2.	Enable Remote Automation click `Develop > Allow Remote Automation` in the menu bar

#### Chrome
We can execute tests on two versions of Chrome. To run tests on chrome, specify browser version: chrome79 or chrome74. We need to download binaries for the two versions from here: :[Download older versions of Chrome for Mac](https://www.slimjet.com/chrome/google-chrome-old-version.php)
Download Chrome version 79 and version 74 for mac and place them in binaries folder.

#### Firefox
If not already there, download the [latest version of firefox]  (https://www.mozilla.org/en-CA/firefox/mac/ ) and install it.

### Running the tests
There are different ways that tests can be executed.\
To run all the tests on all the browsers:
```
python run.py
```

To run all the tests on specific browser(s)
```
python run.py -b chrome79,safari
```

To run specific feature:
```
python run.py -p notes -b chrome79
```

To further drill down to running desktop or mobile only within a feature:
```
python run.py -p notes/desktop -b chrome79
```

To run a specific testcase:
```
python run.py -p notes/desktop/TC_201_001_create_session_note_test.py -b chrome
```

