# Triibu App
[Triibu](www.rionegrodatascience.com "Frontend") is a Data Science powered dashboard that will allow Rionegro Major's office to analyze and forecast their income from property and business taxes, and to take the best investment decisions for the municipality.

![image info](./assets/Home_ss.PNG)

## Folder Structure

```
project_root/
│
├── assets/               # Project assets and styles (css)
├── data/                 # Additional data needed
├── apps/                 # Python files for each one of the application tabs
├── app.py                # Dash App definition
├── db_connection.py      # Connection credentials for the database
├── index.py              # Main dash file, call of the tabs layouts
├── wsgi.py               # App Endpoint
├── rionegro.ini          # Configuration file for WSGI HTTP Server
├── rionegro.service      # Systemd Unit File
├── rionegro              # Configuration file Nginx to Proxy Requests
├── requirements.txt      # Requirements for running the Dash app
```

## Instructions to run locally.
1. Clone this repo
```
git clone {repository_url}
```

2. Change the working folder and install dependencies using requirements.txt
```
cd 'Triibu Frontend'
pip install -r requirements.txt
```

3.  Execute the app from the command line
```
python index.py
```

5. Open in browser
the app will be served at https://localhost:8050
