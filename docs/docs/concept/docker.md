---
id: docker_concept
title: Docker
---

## Docker 是什麼

為了確保開發系統時不會遇到電腦環境問題干擾，最簡單的方式就是開出一個虛擬化後的 (virtualized)環境，讓大家在相同的平台上開發。
舉個例子，我們較常聽到的虛擬化產品是從網卡、處理器、顯示卡等等硬體層級開始模擬的 VirtualBox。不過在追求效率最大化以及部署便捷性的趨勢下，容器(Container)成為近年來發展最為迅速的虛擬化技術。與 VirtualBox 類別產品最大的不同是，容器技術是從作業系統層級開始進行虛擬化，不需要再用各種奇技淫巧來加速模擬硬體的過程，讓虛擬機的邊際成本下降了許多。

我們在這個專案下使用到的 Docker 就是基於 Container 技術家族的產品。

在這裏我們會介紹理解 Docker 需要知道的基礎知識跟名詞，為了降低新手們的認知負擔，專案已經把大部分的指令打包起來，只要理解如何使用我們給的流程背後所代表的意義，不需要親手操作 Docker 。但如果有興趣也可以自己去鑽研。而接下來的基礎介紹只是讓你知道一些基本概念。遇到問題時比較有方向解決。

### 名詞解釋

* docker image :

    一個 image 代表的是整個封裝完成的檔案系統（包含函式庫）。是我們拿來發布環境使用的檔案

* docker container:

    拿到 image 之後，系統可以根據 image 內容產生出一個當初指定的環境，每一個執行中的系統單位叫做一個 container

### Docker適用的環境

追根究底，Container 技術中你的虛擬化環境還是會與原本主機共享 Kernel，根本上還是依賴著你電腦上 OS 的調配能力。一般來說，如果要在 Windows 等非 Linux kernel 上支援 Container 技術都會需要另外一層的努力。(比如說安裝某些額外產品)

## Docker-compose

介紹完 Docker，我們就能開始談一下什麼是 Docker-Compose。這個對我們的系統很重要，是連結到整個服務如何運作的重要元件。

在 `plus` 的網站服務架構中，我們通常會需要有一個處理業務邏輯的後端伺服器、一個可以幫忙提供使用者資料的資料庫系統，還一個對外部網路公開，用來做加密連線的 Gateway Server(目前仍在開發階段，尚未放入)。三個獨立的系統相依運作，才能形成我們所看到的整個 `plus` 服務。

一般來說，這些系統都可以同時裝在同一台主機之上，但為了不讓彼此的服務的系統環境相互影響，也為了提高系統的可靠度，我們會把三個子系統各自拆分成一個獨立的 Docker Container。

對於 `plus` 系統的開發者來說，多個相依系統元件的起落雖然重要，但也不會想要手動管理他們各自的服務狀況。所以 `Docker-Compose` 就這樣出現了， `Docker Compose` 是一個獨立於 `Docker` 的工具，用途就是透過閱讀目前專案下的 `docker-compose.yml` 所指定 Container 間的相依關係來操作 `Docker` ，讓開發者不必去手動操作這些問題。

### `docker-compose.yml`

你可以看一下專案的根目錄有一個 `docker-compose.yml` 檔案。裡面的大致內容是這樣的：

``` yml
# docker-compose.yml
version: '3.x'
services:
    api-server:
        image: 'ianre657/plus-api-server:latest'
        build:
            context: ./plus
            dockerfile: plus.dockerfile
        # ...
    db:
        image:
        # ...

    pgadmin:
        image:
        # ...
volumes:
    app-db-data:
```

你可以簡單看出來這裡應該會有三個服務 `api-server` , `db` 跟 `pgadmin` 。我們主要撰寫的服務就是 `api-server` ，而這個系統由於是我們自己的程式碼真正用到的，所以也是由我們自己指定 container 中的環境該長什麼樣子，那麼我們的環境是寫在哪裡呢？你可以看看 `api-server` 中的區塊：

``` yml
# docker-compose.yml
api-server:
        image: 'ianre657/plus-api-server:latest'
        build:
            context: ./plus
            dockerfile: plus.dockerfile
```

綜合 `build` 區段下的 `context` 與 `dockerfile` 區段，我們是指定了專案下的 `/plus/plus.dockerfile` 做為我們服務所需要的 image。

## `plus` 的建置到啟動解析

```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

# RUN poetry install --no-root --no-dev
RUN poetry install --no-root

COPY . /app

ENV PATH="/app/scripts/:${PATH}"

```