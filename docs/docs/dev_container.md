---
id: dev_container
title: Develop Inside Container
---

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


### Migrations

As during local development your app directory is mounted as a volume inside the container, you can also run the migrations with `alembic` commands inside the container and the migration code will be in your app directory (instead of being only inside the container). So you can add it to your git repository.

Make sure you create a "revision" of your models and that you "upgrade" your database with that revision every time you change them. As this is what will update the tables in your database. Otherwise, your application will have errors.

* Start an interactive session in the backend container:

```console
$ docker-compose exec backend bash
```

* If you created a new model in `plus/app/models`, make sure to import it in `plus/app/models/base.py`, that Python module (`base.py`) that imports all the models will be used by Alembic.

* After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

* Commit to the git repository the files generated in the alembic directory.

* After creating the revision, run the migration in the database (this is what will actually change the database):

```console
$ alembic upgrade head
```