---
id: getting_started
title: Getting Started
---

## step1. clone the project

```bash
git clone https://github.com/ianre657/plus.git
```

## step2. Setup configuration files (`.env` file)

We use a `.env` file to store global variables for all of our dockerfiles.

Use `./onboarding.sh` to propagate those files.

## step3. Install dependencies

### Install docker and docker-compose

+ [Docker][docker-link].
+ [Docker Compose][dockercompose-link].

[docker-link]: https://www.docker.com/get-started
[dockercompose-link]: https://docs.docker.com/compose/install/

### Build docker image

After installing `docker` and `docker-compose` and setting up `.env` file, build your own docker image with:

```sh
docker-compose build
```


## step4. Start Developing

Use `docker-compose up` to start the project.

Open your browser with `localhost:10080` to see the result.

See [Develop Inside Container][dev_container], `Code of Conducts`(wip) for more information.

[dev_container]: ./dev_container.md
