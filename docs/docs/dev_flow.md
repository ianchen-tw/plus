---
id: dev_flow
title: Development Flow
---

## Choose a Good Editor
wip

### VSCode

+ Plugins to Install
     + Docker
     + Remote-Containers
     + Visual Studio IntelliCode
     + Python
     + Magic Python

### PyCharm

+ Install PyCharm:
     + install dependency by `cd plus && poetry install`
     + install [poetry plugin][poetry-plugin-link] from marketplace
          + select virtual environment from settings

[poetry-plugin-link]: https://github.com/koxudaxi/poetry-pycharm-plugin

:::info
If you want to develop with docker-compose inside PyCharm, a [Pro](https://www.jetbrains.com/community/education/#students) version is required.
:::

## Develop in docker-container

### Run the development server


```sh
$ docker-compose up
```
(or use `make up` as shorthand)

+ additional options for running `docker-compose`:
     + `--build`: rebuild conatiner
     + `-d`: run in the background as daemon.

The serivices will be hosted on `localhost` in the background. see the ports defined below:

|Name|URL|
|-:|:-|
|api-server|[http://localhost:8888](http://localhost:8888)|
|api-server openAPI spec|[http://localhost:8888/docs](http://localhost:8888/docs)|
|traefik dashboard|[http://localhost:8090](http://localhost:8090)|
|pgAdmin|[http://localhost:5050](http://localhost:5050)|

Note: This would run our serer in the background, use `docker-compose up` to run it in the foreground.

### Shutdown the development server

```sh
$ docker-compose down
```
(or use `make down` as a shorthand)


### Attach to running container

```sh
$ docker-compose exe api-server bash
```
(or use `make shell` as a shorthand)


### Run predefined scripts

:::info
you need to attach to running container to run these scripts.

See [Attach to running container](#attach-to-running-container)
:::

+ Run tests
     ```sh
     .test.sh
     ```

+ Format code
     ```sh
     .format.sh
     ```


> Here we use a dot(`.`) as a prefix for naming our scripts to prevent from name collision and utilize tab-completion feature
