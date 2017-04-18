# Softhub

Web application to store applications.


## Requirements
- python (pip): to install Django and other apps like Django REST Framework
- npm: to install bower
- [bower](https://bower.io/): to handle dependencies found in bower.json

## Install and Run
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

python manage.py runserver
```

The following files are used to store dependencies:  
`requirements.txt`: contains python dependencies  
`bower.json`: contains external JS and CSS libraries, used by bower  
`.bower.rc`: configuration file for bower, used to tell bower where to store dependencies

## Standard and conventions

Code is written trying to follow PEP8 standard: https://www.python.org/dev/peps/pep-0008/

## Management commands
Generate models diagrams (you'll need Graphviz installed):
``` bash
python manage.py graph_models -a -o models.png
```
