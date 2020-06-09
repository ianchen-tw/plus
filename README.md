<img src="./res/nplus_logo.png" alt="plus-logo" align="right" height="300" width="300" />

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

The serivices will be hosted on `localhost` in the background. see the ports defined below:

|Name|URL|
|-:|:-|
|api-server|[http://localhost:8888](http://localhost:8888)|
|api-server openAPI spec|[http://localhost:8888/docs](http://localhost:8888/docs)|
|traefik dashboard|[http://localhost:8090](http://localhost:8090)|
|pgAdmin|[http://localhost:5050](http://localhost:5050)|

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
2. run test with: (or `./scripts/.test.sh`)

```
.test.sh
```

> Here we use a dot(`.`) as a prefix for naming our scripts to prevent from name collision and utilize tab-completion feature

### Run Formatter

1. Start our service in docker and enter the shell using:
```
make shell
```

2. run test with: (or `./scripts/.format.sh`)
```
.format.sh
```

> Here we use a dot(`.`) as a prefix for naming our scripts to prevent from name collision and utilize tab-completion feature

## MISC

config files:
+ ~`.devcontainer/`: used in VSCode~