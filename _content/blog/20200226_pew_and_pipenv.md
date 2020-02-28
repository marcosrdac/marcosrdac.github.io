---
title: Python virtual environments: from "virtualenvwrapper + pip" to "pew + pipenv"
date: 20200226
draft: true
---

Ever since I started using `Python` environments, I am using `virtualenvwrapper`. It is nice to to be able to isolate a version of the language interpreter and its libraries and access it so easly. Though the proccess of installing this wrapper is a mess. You must set your shell to load one of its codes, and then, when you perceive you've done something that is really freezing every terminal window when it starts... So that you look up in the docs for them to say that you could source another script instead of the first one, so that your terminal isn't that way anymore... You know, this is not very didatic when I am teaching Python.

I'm happy to show you here that you can easily manage your virtual environments with two modern tools: `pew` and `pipenv`.


## `pew`

Pew is a tool very similar to virtualenvwrapper, but it only requires the variable `$WORKON_HOME` to be defined in your environment. It is a useful tool for creating general Python virtual environments, and can easily be installed with pip:

```sh
sudo pip install pew
```

Though, if you are an Arch user, it is recomended that you use `pacman` to install this kind of general software, that is not a library for a specific project:

```sh
sudo pacman -S python-pew
```

I usually set "$WORKON_HOME" to to be at `$HOME/.local/lib/pipenvs` (`$HOME` means `/home/<YOUR_USERNAME>` --- it is pre-defined shell variable), but it is really arbitrary. If you use a common bash shell, to set `$WORKON_HOME` means to add this line to your `$HOME/.bashrc`:

```sh
export WORKON_HOME="$HOME/.local/lib/pipenvs"
```

Else, if you divide env and rc configuration and files, put this line ate one of the env ones. In that case, it's safe that you restart your session. If you are a common user, you can just close your terminal and open it again. type `echo $WORKON_HOME` and you should see the path you just set. Anyway, let's get back to pew!

You can create a virtual environments named `m` with:

```sh
pew new m
# or, to specify a python executble,
pew new m -p python3
```

After this you will be in the virtual environment `m`. You can use pip without sudo here, as it will only install packages for your environment (a folder at home).



 echo $VIRTUAL_ENV
 will be useful
