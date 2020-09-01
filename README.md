# Test Driven Development with Django

A deep dive into the discipline of Test Driven Development  by building a web app
from scratch using Django, Selenium, jQuery and Mocks.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python3
* Firefox and geckodriver

[Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)

[Installing Python3 on Windows](https://www.python.org/downloads/windows/)

[Geckodriver](https://github.com/mozilla/geckodriver/releases)

### Installing

Getting your development env up and running

Clone this repo

Create a virtual environment
```
python3 -m venv env
```

Activate virtual environment

windows
```
source venv/Scripts/activate
```

linux/Mac
```
source venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

Run database migrations
```
python manage.py makemigrations
```


## Running the tests

Run the functional and unit tests using built in Django test runnner
```
python manage.py test
```

## Deployment

TODO: Notes on deployment to a live system

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used

## Acknowledgments

* [Obey the Testing Goat](https://www.obeythetestinggoat.com/book/chapter_01.html)
