# Finance Tracker

Finance Tracker is a web app implemented using Flask and bootstrap that works like a mini stock exchange system. The following functionalities have been added to the app-

- Register: Any person can register to make a new account.
- Quote: A registered user can quote a price for a stock.
- Buy: Users can buy shares for a price.
- Index: To show the stocks in the user's account.
- Sell: Users can sell shares of a stock.
- History: User can see the past transaction history.

### Project Demo

<hr/>

![1](https://user-images.githubusercontent.com/43414928/79959356-acaf6b80-84a1-11ea-88b1-721e18ebdcef.png)
<br/>
![2](https://user-images.githubusercontent.com/43414928/79959291-95707e00-84a1-11ea-8cf1-0bb32cc4b496.png)
<br/>
![3](https://user-images.githubusercontent.com/43414928/79959295-973a4180-84a1-11ea-8ede-eeb86f41f739.png)
<br/>
![4](https://user-images.githubusercontent.com/43414928/79959314-9acdc880-84a1-11ea-9cbc-cf7685ef91f7.png)
<br/>
![5](https://user-images.githubusercontent.com/43414928/79959301-99040500-84a1-11ea-8f6b-50b7ff866c83.png)
<br/>
![6](https://user-images.githubusercontent.com/43414928/79959312-9acdc880-84a1-11ea-8a37-3a69d21e374f.png)


## Tech Stack-

* Python
* Flask
* SQLAlchemy
(Other dependencies can be found out in te requirements.txt file)

## Installation-

1] Create a folder in your device. Open the folder and right click on the empty space of the folder and click on Git bash here comand. In the git CLI write the command git clone and paste the link of the repository that you have copied.

2] Download SQLite3 Link: https://www.sqlite.org/download.html sqlite-tools-win-x64-3450100.zip (4.77 MiB) from A bundle of command-line tools for managing SQLite database files, including the command-line shell program, the sqldiff.exe program, and the sqlite3_analyzer.exe program. 64-bit. for windows.

3] To create a virtual environment you have to run these commands on Windows: python -m venv venv
Linux: python3 -m venv venv

4] After creating a virtual environment, activate it by running this command: 
Windows: venv\Scripts\activate (venv is the name of your virtual environment)
Linux : source myenv/bin/activate
To deactivate the venv you just write the `deactivate` comand on terminal

5] Now install all the packages which are mentioned in the requirements.txt file using `pip install -r requirements.txt`

6] Once all the dependancies have been installed, run the commands:
    1. `python database.py`, 
    2.`python create_db.py`,
    3.`python populate_db.py`, 
    4.`python Main.py`

7] This should start a local server and you can access it on your browser at localhost:5000.
