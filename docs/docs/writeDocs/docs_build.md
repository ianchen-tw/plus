---
id: docs_build
title: Build your docs-site
---

## Dependencies for building docs

Follow the steps below to build our docsSite.

### Node.js
+ Install Node Version Manager via the [install script][nvm-install-link].

    ```sh
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
    ```

+ Verify your installation

    ```sh
    nvm version
    ```

+ Install `node.js` Erbium(v12) via `nvm`

    ```sh
    nvm install --lts=erbium
    ```

+ Set default node version

    ```sh
    nvm use --lts=erbium
    ```

### Yarn

+ Install [Yarn][yarn-install-link]

+ Install dependecies via `Yarn`

  ```sh
  cd docs && yarn install
  ```

+ Try to build and preview the document site

  ```sh
  yarn run start
  ```
  :::info
  Your shell needs to be in the /docs folder.
  :::

[nvm-install-link]: https://github.com/nvm-sh/nvm#install--update-script
[yarn-install-link]: https://classic.yarnpkg.com/en/docs/install/
[docu-link]: https://v2.docusaurus.io/
