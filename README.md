# plus

`plus` is an API server for students

## Installation

1. Install `docker` and `docker-compose` before starting to development

2. Propagate the environment file
	```bash
	cp env_template/dev.env plus/dev.env
	```

## Usage

### Run the development server

```
make up
```

The api server will be hosted on `localhost:10080` in the background.

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