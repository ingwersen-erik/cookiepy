# Website

Website built using [Docusaurus 2](https://docusaurus.io/),
a modern static website generator.

Below are the instructions on how to build the project documentation locally
at your machine.

## Requirements

To build the documentation website locally, you'll have to install either
`yarn`, or `npm`. Here's how to install each of them:

### How to Install `Yarn`

**For MacOS Users:**

First install Homebrew if you don't already have it installed:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then execute the following command:

```
$ brew install yarn
```


**For Linux Users:**

There are multiple ways to install `yarn` on Linux machines. One of these methods
is via `apt-get install` (requires root permissions):

```
$ sudo apt install yarn
```

Other methods can be found here: [How to install yarn](https://itslinuxfoss.com/yarn-command-not-found/#:~:text=The%20%E2%80%9Cyarn%20command%20not%20found%E2%80%9D%20error%20is%20invoked%20when%20the,sudo%20apt%20install%20cmdtest%E2%80%9D%20commands.)

**For Windows Users:** follow the instructions outlined [here](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable)

----

### Installation

The following command installs the necessary dependencies to build the project
documentation:

```
$ yarn
```

Example command output:
```
❯ yarn
yarn install v1.22.19
[1/5] 🔍  Validating package.json...
[2/5] 🔍  Resolving packages...
[3/5] 🚚  Fetching packages...
[4/5] 🔗  Linking dependencies...
warning "@docusaurus/core > react-loadable-ssr-addon-v5-slorber@1.0.1" has unmet peer dependency "react-loadable@*".
warning "@docusaurus/core > react-dev-utils > fork-ts-checker-webpack-plugin@6.5.2" has unmet peer dependency "typescript@>= 2.7".
warning "@docusaurus/preset-classic > @docusaurus/theme-search-algolia > @docsearch/react@3.1.1" has unmet peer dependency "@types/react@>= 16.8.0 < 19.0.0".
warning "@docusaurus/preset-classic > @docusaurus/theme-search-algolia > @docsearch/react > @algolia/autocomplete-preset-algolia@1.7.1" has unmet peer dependency "@algolia/client-search@^4.9.1".
[5/5] 🔨  Building fresh packages...
✨  Done in 60.82s.

```


### Local Development

Execute the following command to start the web server locally:

```
$ yarn start
```

**Default local URL:** [http://localhost:3000/](http://localhost:3000/)

When you execute the command, it opens a browser window with the landing page
for the documentation website. Most changes you make to the
markdown files that define the website contents are updated live
without having to restart the server. There are some exceptions for those
live updates though.

### Build

```
$ yarn build
```

This generates a static content into the `build` directory.
You can serve using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
