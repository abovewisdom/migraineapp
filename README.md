# migraineapp

This app is used to enter and track migraines. The MVP of this project will include the ability to create an account, log a migraine, and view the details for each migraine entered. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install Docker

On Mac:
```
brew install docker
```

### Installing

Clone this repo. 

```
git clone https://github.com/abovewisdom/migraineapp.git
```

If changes have been made to the database model run this command in the web container, `mgappdocker_web_1`

```
python3 manage.py migrate
```

And to launch the web app:

```
docker-compose up
```

TODO: End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

TBD: Planning on using Docker and AWS tools to deploy. 

## Built With
This app is built with the Django Framework and Postgres as a database. It is built with the goal of using docker to ultimately deploy the app. 

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap 4](https://getbootstrap.com/) - The css framework used
* [pgAdmin 4](https://www.pgadmin.org/) - UI for Database Configuration
* [Postgres](https://www.postgresql.org/) - Database
* [Docker](https://www.docker.com/) - Used to make development/deployment easier.

## Contributing
For now this repo is a private project and I don't plan on others being interested in contributing. If you are interested or have questions please open an Issue on Github. 

## Versioning

TODO: I plan on using [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

Just me so far. 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

TBD

