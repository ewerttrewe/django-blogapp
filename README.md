![GitHub last commit](https://img.shields.io/github/last-commit/ewerttrewe/django-blogapp?style=plastic) ![Maintenance](https://img.shields.io/maintenance/no/2022)

# Django blog app
This app is a simple blog where you can create, update, read and delete posts.

> **This simple django blog app is created only with vanilla django and it assumes that you have python >= 3.6 version installed on your machine**

You need to follow few steps below in order to use this app on your local machine:<br><br>
1. Clone the repository using `git clone https://github.com/ewerttrewe/django-blogapp.git` command.<br>
2. Cd to the root directory of the project on your machine and fetch and merge all the latest changes using `git pull` command.<br>
3. After that create virtual environment in your root directory via `python -m venv env` command.<br>
4. Cd to previously created environment and activate environment:<br><br>
  Actiavte virtual environment by typing in<br><br>
  &nbsp; **Windows Users:**<br>
  `.\Scripts\Activate.ps1`<br><br>
  &nbsp; **Linux/macOS Users:**<br>
  `source venv/bin/activate`<br><br>
5. cd back via `cd ..` and `pip install -r requirements.txt`<br>
6. To start the server and be able to connect to certain endpoint type in `python manage.py runserver 8000`<br>
7. Open web browser and try to connect to `http://localhost:8000`<br>
8. Now you should be able to surf on the blog, try to create new user, log in and feel free to add post or check whatever you want, beneth there is a short video showing the page for brief visualization.<br><br>

> **Disclaimer:** You can open a Python shell within the project's directory and run the following command to generate a new secret key and add it to `settings.py`, at the top level there is `SECRET_KEY=''` empty variable:<br>
`python manage.py shell`<br>
`from django.core.management.utils import get_random_secret_key`<br>
`get_random_secret_key()`<br><br>











https://user-images.githubusercontent.com/93892998/209128750-14c1f304-133c-41b1-8a3e-24d23451f831.mp4
