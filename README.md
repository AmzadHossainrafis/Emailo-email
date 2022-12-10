
# Emailo-App

![Alt text](website/static/gitlab_img/git_banner.png)

A brief description of what this project does and who it's for

### What is emplimented: 

1. Login page
* user can login with email and password 
* if user is not registered, it will flah a message to register 
* if user is registered, it will redirect to dashboard
2. Sign up page 

* user can sign up with email he wants to use fast_name and last_name and password 
* it will flash a message if user is already registered with the email 
* it will redirect to login page if user is not registered 
  
   
3. User dashboard 
    

    1. Send email page 
      * user can see all his sent emails 
      * while sending email, user can select eamil category 

    2. Inbox page 
      * user can see all his emails divided into 4 section 


## How to run in your local machine 
1. cd into your dir

1. create a virtual environment 
```bash
    python -m venv Romatoo_email
```

2. activate the virtual environment 
```bash
    $ source Romatoo_email/bin/activate
```
3. clone the repo
```bash
    git clone {repo link} 
```
4. install requirements 
```bash
    $ pip install -r requirements.txt
```
5. cd into the project
```bash
   $ cd Romatoo_email
  ```
6. run app.py 
```bash
    $ python app.py
```
## Deploy in heroku 

### Importeant warning : 
  * note that you need to have git installed in your machine 
  * must have a Procfile in the root of your project , it will tell heroku how to run your app (in my case it is web: gunicorn app:app)
  * requirements.txt file must be in the root of your project, it will tell heroku what packages to install 
  * runtime.txt file must be in the root of your project, it will tell heroku what version of python to use (in my case it is python 3.10.5) 
  
  
## Deployment setps 

1. [Create a heroku account](https://id.heroku.com/login)
2. [Download heroku cli and install it](https://devcenter.heroku.com/articles/heroku-cli)
3. Open any tarminal and login to heroku
```bash
   $ heroku login
```

1. clone the repo 
```bash
   $ git clone https://github.com/AmzadHossainrafis/romatoo_email.git
   $ cd romatoo_email
```

1. create a new app in heroku (heroku will give you a link to your app) 
```bash
   $ heroku create 
```
1. push the repo to heroku
```bash
    $ git push heroku main
```

1. open the app in the browser

```bash
    $ heroku open
```
## Authors

- [@AmzadHossainrafis](https://github.com/AmzadHossainrafis)

