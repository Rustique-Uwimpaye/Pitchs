# Pitch App
This is a Python application using Flask framework and PostgreSQL

By **[Rustique Uwimpaye](https://github.com/Rustique-Uwimpaye)**

## Description
This is a Python web application where users write and post ideas to change the world. Once a user has posted an idea it becomes visible to all members or users of the application where they can comment up-vote or down-vote the idea.
## Setup/Installation Requirements

* Python3.8 
* PostgreSQL  installed
* clone the directory into your local machine
* navigate to the cloned folder by `cd Pitchs`
* run `source virtual/bin/activate`
* pip install `requirements.txt`
* run `python3.8 manage.py server`
* The application should work
## Known Bugs
NO known bugs as at the moment.
## Behavior Driven Development

| __Behavior__  | __Input example__ | __Output example__ |
| ------------- | ----------------- | ------------------ |
| The user should be able to view all Pitched Ideas  | "https://www.com"   | Pitched ideas |
| The application should give the user an option to view a single category | pickup lines | pickup line pitches |
| The User should see different Pitch categories | interview pitch, product pitch, and promotion pitch | All pitched ideas |
| The user should be able to sign up to the application | /sign up | successfully |
| The application should save user credentials | username,password,email | saved |
| The application should authenticate the users on login request  | login | true/false |
| The user should be able to comment on any Pitched Idea | comment | saved |
| The user should be able to up-vote or down-vote any idea | up-vote or down-vote | votes |
| The application should logout the user when prompted | logout | True |


## Technologies Used

* Python
* Material design
* Flask
* JavaScript
* CSS
* PostgreSQL Database

## Support and contact details

get me at rustique644@gmail.com

## License
* MIT LICENSE <br>
Copyright © 2020 | **Rustique Uwimpaye**

