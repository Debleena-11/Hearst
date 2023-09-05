# Hearst QA Interview Exercise

## About
This readme files would provide necessary instructions to run the completed backend and frontend tests.
The tests are developed using Cucumber BDD, so that there is no additonal requirement of maintaining a seperate test plan.
The test directories contain test_app.feature file which has the details of test cases and test steps.
The implementations of the test steps are done in the steps.py file in the individual directory.
Each directory also has a output.txt file that captures the output from the tests last ran.


## Pre-requisites
Apart from the pre-requsites required to run the client and server
Use the following commands to install the necesary components for testing
The API tests were developed using Windows susbsystem for linux(WSL)
information regarding installing WSL on windows can be found here: https://learn.microsoft.com/en-us/windows/wsl/install
under WSL in power shell
-pip install fastapi[all] pytest
-pip install behave fastapi[all] httpx

in normal powershell windows
-pip install selenium 
-pip install behave
-place the \webdriver folder directly under "C:\" such that "C:\webdriver\chromedriver.exe" exists
After installation of behave have it included in the enviorment variable so as to not to specify the full path of the executable.
### After Running the client and server as specified in the original exercise.

### Run server -backend api tests
- Run 'wsl' to start the wsl
- Run `cd Hearst assignment\test\APITests\features\steps` to navigate into the api test folder
- Run 'behave' to run the API tests
Example:
nandajana@DESKTOP-UI4A4M3:/mnt/c/Users/Public/Documents/Hearst/qa-interview-main/qa-interview-main/test/APITests/features/steps$ behave


### Run client front end UI -selenium tests
- `cd Hearst assignment\test\SeleniumTests\features\steps` to navigate into the selenium front end test folder
- Run 'behave' to run the Selenium tests
Example:
PS C:\Users\Public\Documents\Hearst\qa-interview-main\qa-interview-main\test\SeleniumTests\features\steps> behave.exe
