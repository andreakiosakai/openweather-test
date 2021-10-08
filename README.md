# OpenWeather Test Project

 This is a simple project using Python 3, pytest and requests for API testing.
## Pre-requisites

 - [python3](https://www.python.org/downloads/)

 - [pipenv](https://pipenv.pypa.io/en/latest/)

 - Sign up and get your API KEY from Open Weather API:
[site](https://home.openweathermap.org/users/sign_in)
## How to install

First of all, please, clone this repo:

`git clone git@github.com:andreakiosakai/openweather-test.git`

In the root folder, you need to duplicate and rename the env.cfg file:

`cd path/to/project/openweather-test`
`cp src/config/env-template.cfg src/config/env.cfg`

Open the file:

`vim src/config/env.cfg`

Edit this line with your OpenWeather API KEY:
>API_KEY = <YOUR_API_KEY>

Example:
>API_KEY = abc123abc123

#### Running Local with pipenv

Run this command to install dependencies:

`pipenv install`

Open your pipenv environment with the following command:

`pipenv shell`

Run the tests:

`pytest tests/ --html report/report.html`

#### Running with Docker

Build a Docker image with the following:

`docker build -t api_test .`

To run the tests from Docker, run the following command:

``docker run -it --rm -v `pwd`:/openweather-test api_test pytest tests/ --html report/report.html``

#### Reports

After the test run, you can see a report file, just open the following file in your browser:
>report/report.html
