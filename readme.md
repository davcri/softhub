# Softhub

Softhub is a demonstrative web application written in modern __Python 3__ using
[Django Web Framework](https://www.djangoproject.com/). 

This is a project for my bachelor thesis in computer engineering:

> Django: design and development of an open source web application

- [Blog post about my University projects](https://davcri.github.io/posts/software-projects-university/)
- Thesis ([LaTeX source repository](https://gitlab.com/davcri91/thesis))
- Thesis ([PDF](https://gitlab.com/davcri91/thesis/uploads/b53e6988702a7bef746bde6cd351fd1c/Tesi_v7_bozza_finale.pdf), only available in Italian)
 


## Development requirements
- [python](https://www.python.org/): to install Django and its modules
- [npm](https://www.npmjs.com/): required by _bower_
- [bower](https://bower.io/): to handle dependencies found in bower.json

## Set up a local development environment
For detailed install instructions, see
[the wiki page](https://gitlab.com/davcri91/softhub-site/wikis/installation-guide),
otherwise read the following **installation Overview**.  

**Note**: this guide is tested on Arch Linux that use python3.x as default.  
Run these commands from the project folder:

``` bash
# create a directory for the virtualenv
virtualenv ENV
# activate the virtualenv
source ENV/bin/activate
# install python dependencies
pip install -r requirements.txt

# install bower if necessary
npm install -g bower

# install web dependencies with bower
bower install

# run migrations
python manage.py migrate

# [Optional] run a custom Softhub command to initialize the database
# https://gitlab.com/davcri91/softhub-site/blob/master/softhub/management/commands/initialize_db.py
python manage.py initialize_db

# [Optional] run a custom Softhub command to populate the database with faked data
python manage.py fake_data

# run the local development server
python manage.py runserver
```

The following files are used to store dependencies:  
`requirements.txt`: contains python dependencies  
`bower.json`: contains external JS and CSS libraries, used by bower  
`.bower.rc`: configuration file for bower, used to tell bower where to store
dependencies

### Administrator section
In order to access the admin section, run the app server then go to
`/softhub/admin/`.

If you executed *initialize_db* command, an admin account will be automatically
creted with

```
username: admin
password: admin12
```

If you dind't execute *initialize_db*, you'll need to create an admin account
using `python manage.py createsuperuser`.

## Standard and conventions
Code is written trying to follow PEP8 standard:
https://www.python.org/dev/peps/pep-0008/

## Management commands
Generate models diagrams (you'll need Graphviz installed):
``` bash
python manage.py graph_models -a -o models.png
```

## Thanks
I used and modified the following templates (all MIT-licensed) :
- https://github.com/BlackrockDigital/startbootstrap-creative
- https://github.com/BlackrockDigital/startbootstrap-shop-homepage
- https://github.com/BlackrockDigital/startbootstrap-shop-item
