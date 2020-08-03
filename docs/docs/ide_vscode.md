---
id: ide_vscode
title: Develop with VSCode
---

在開發時推薦使用 VSCode，一般來說會有二種可行作法: **Remote Container** 跟 **Local development**。

最高整合性跟方便性的方式是使用**Remote Container**，這樣做你不會需要煩惱環境設置，因為所有東西都已經打包在虛擬環境中了。

## Remote Container

安裝 VSCode 的 `Remote Containers`套件，打開 `plus` 專案後使用 `Command+Shift+P`, (`Ctrl-Shift-P` for windows)，呼叫命令列，再選擇 `Remote-Containers: Rebuild and Reopen in Container`

:::info
   開發時如果網路不穩定不建議使用此方法。

   因為微軟授權因素，每次打開 remote-container 時都會需要即時下載他們的 language-server，網路差的時候這樣會很花時間
:::

## Local Development

使用 VSCode 打開專案，直接編輯文字專案，並且在 Command Line 進入 Container 進行開發

:::warning
這種方式只能在 VSCode 的文字介面中提供基本語法支援，比較不推薦
:::

這邊會推薦你先安裝一些 VSCode 的套件。
+ Visual Studio IntelliCode (`visualstudioexptteam.vscodeintellicode`)
+ Python (`ms-python.python`)
+ Better TOML (`bungcip.better-toml`)

並且透過 `pyenv` 安裝 `python3.7` ，在 VSCode 中指明 `Python3.7`作為你的 interpreter。

### Install python3.7
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


