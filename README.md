# The ToDo List
###### Simple Flask To Do List
###### Life Version [ToDo List](https://manifest-shade-274413.ew.r.appspot.com/)
_______________________________________________________________________

###### How to install repository and run locally:
1. Clone repo: git clone https://github.com/VladyslavHnatchenko/g-todo.git
2. Go to folder: cd g_todo
3. Run on terminal/bash: python3 -m pip install --user --upgrade pip
4. Run on terminal/bash: python3 -m pip install --user virtualenv
5. Install virtualenv: python3 -m venv env
6. Activate virtualenv: source env/bin/activate
7. Install all libraries: pip install -r requirements.txt
8. Export your Cognite API-KEY: export COGNITE_API_KEY='insert your api key here'
9. Run locally with uwsgi: python3 main.py
_______________________________________________________________________

###### How to Deploy On App Engine:
1. Go to [Google Cloud](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
2. Download and install Cloud SDK: click on Download the SDK and choose your OS 
(Debian/Ubuntu/MacOS/Windows/etc.)
3. Run on terminal/bash: gcloud projects create [YOUR_PROJECT_ID] --set-as-default
4. Run on terminal/bash: gcloud projects describe [YOUR_PROJECT_ID]
5. Run on terminal/bash: gcloud app create --project=[YOUR_PROJECT_ID]
6. Run on terminal/bash: gcloud init
7. Run on terminal/bash: gcloud app deploy
8. Run on terminal/bash: gcloud app browse
_______________________________________________________________________
