---
id: install_deps
title: Install Dependecies
---

:::caution
`plus` only support development via Linux/OSX

If your're using Windows, this might but is not guaranteed to works. (use virtualmachines instead)
:::

For most of our work, you should develop your application in Docker Containers.


If you don't want to connect to database or other services, (only write code in editor and wanna get syntax support/intellisence) try [local development with syntax supports][1].

For gerenating docs, checkout [Dependencies for writing docs][2].

[1]: #local-development-with-syntax-support
[2]: #dependencies-for-building-docs

## Install dependecies via Docker

+ [Docker][docker-link].
+ [Docker Compose][dockercompose-link].

[docker-link]: https://www.docker.com/get-started
[dockercompose-link]: https://docs.docker.com/compose/install/

After installing `docker` and `docker-compose`, build your own docker image with:

```sh
docker-compose build
```

## Local development with syntax support


### Python

+ Install [pyenv][pyenv-page] via [pyenv-installer][pyenv-install-link] to have a virtual python version

    ```sh
    curl https://pyenv.run | bash
    ```
+ Install `Python 3.7.7` via pyenv
    ```sh
    pyenv install 3.7.7
    ``` 

[pyenv-page]: https://github.com/pyenv/pyenv
[pyenv-install-link]: https://github.com/pyenv/pyenv-installer

### Poetry

+ Intall [Poetry][poetry-page] for Package management tool for Python

    ```sh
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
    ```

+ Install dependecies by:

    ```sh
    poetry install
    ```
[poetry-page]: https://python-poetry.org/

### Using Poetry in VSCode

Select the correct interpreter in your VSCode: [vscode-python/issues/8372][vscode-poetry]

[vscode-poetry]: https://github.com/microsoft/vscode-python/issues/8372



## Dependencies for building docs

wip

[docu-link]: https://v2.docusaurus.io/
