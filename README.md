# Solution To CodeChallenge
Code Challenge For Mobile Automation And API Automation

## Steps To Run Mobile Automation and API Automation (Python Project) In PyCharm IDE

### **Prerequisites**
- Make sure, the Python 3 is intsalled along with PyCharm IDE
- Download Appium GUI Server OR Install Appium Using npm > `npm install -g appium`
- Download Android Studio and Create a Android Virtual Device(AVD) AKA Emulator
- Start Appium Server (Appium Server By Default Starts on Port 4723)
- Launch an Emulator 
- Drag And Drop The General Store APK on to the Emulator in order to Install it

### **Step 1: Take the pull from public GitHub Repository**

Public GitHub Repository : `https://github.com/ansaritaha144/CodeChallenge.git`
Here is a [Link](https://github.com/ansaritaha144/CodeChallenge.git "Optional link title").

### **Step 2: Import the Project** 

Open the Project into PyCharm IDE (Trust the Project, when Prompted)

### **Step 3: Add Virtual Environment**

On Mac, Go to ‘Preference’ / On Windows Go to ‘Settings’

Click on ‘Project: FolderName’ -> Project Settings -> Python Interpreter

Now, Click on Python Interpreter Dropdown -> Click on “Show All” -> Click on “+” Icon -> Click on “Virtual Environment” -> Click on “OK” -> Click on “OK” -> Click on “Apply”

### **Step 4: Add Python Packages**

Click on “+” Icon to Install Packages

- Appium-Python-Client
- pytest
- pytest-html
- requests

Click on “OK”

### **Step 5: Running the Mobile Automation Script**

To run the basic flow with Appium-Python-Client:

Go to “basicflow” folder -> Open “mainFlow.py” -> Right Click -> Run ‘mainFlow’

Now, to run the “pytest framework” script:

Go to “pytestframework” -> Open a terminal (in PyCharm itself) -> Run the command 

#### **`pytest test_mainFlow.py -s -v --html=testreports.html`**

- -s -> To print out console statements
- -v -> For the verbosity
- --html -> To generate HTML reports

##### testreports.html is generated inside “pytestframework” folder itself

### **Step 6: Running the API Automation Script**

To run the API Automation Script with **requests** library:

Go to “API_Solution” folder -> Open “API_test.py” -> Right Click -> Run ‘API_test’ 


***Please Connect With Me In Case Of Any Query***

***Thanks !!!!***
