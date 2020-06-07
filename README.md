<img src="./docs/nplus_logo.png" alt="plus-logo" align="right" height="300" width="300" />

## Description

`plus` is an API server for students to build a better college course experience.

It is intend to be minimal and well-documented.

This project borrow lots of ideas from [full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql), take a look at [fastapi](https://fastapi.tiangolo.com/) to gain more knowledge on the structure of this project and the intrinsic to building servers.

Happy coding!

<br>


## Installation

1. Install `docker` and `docker-compose` before starting to development

2. Propagate the environment file

	```bash
	./onboarding.sh
	```

## Usage

### Run the development server

```
make up
```

The serivices will be hosted on `localhost` in the background. see the ports defined below

|||
|:-:|:-:|
|service|port|
|api-server|8888|
|pgAdmin|5050|

Note: This would run our serer in the background, use `docker-compose up` to run it in the foreground.

### Shutdown the development server

```
make down
```

### Run tests

1. Start our service in docker and enter the shell using:

```
make shell
```
2. run test with: (or `./scripts/test.sh`)
```
test.sh
```

### Run Formatter

1. Start our service in docker and enter the shell using:
```
make shell
```

2. run test with: (or `./scripts/format.sh`)
```
format.sh
```