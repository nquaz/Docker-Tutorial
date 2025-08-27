# Tutorial

Here, we will cover core Docker concepts and utilities so that you can be quickly up and running on your next big project!
At the end of this tutorial, you will know how to:

+ Read and write a `Dockerfile`
+ Build a Docker image
+ Run and develop code inside a container

First, some vocabulary:

## Vocabulary
+ `Dockerfile` - file specifying how to set up your environment
+ Image - result of building from a `Dockerfile`, usually via running `docker build -t <image_name> <path_to_Dockerfile>`
+ Container - result of running an “instance” of the image, usually via `docker run -it –name <container_name> <image_name>`

Briefly, their relationship goes:
Dockerfile --> Image --> Container

## Overview

It starts with the eponymous `Dockerfile`, which resides locally on your machine and usually at the root of your project. Docker reads in the `Dockerfile` and builds the specified environment in what can be likened to a "mini-Virtual Machine" (it's technically not a virtual machine and relies upon namespace technology, which allows you to run thousands of isolated environments at once on the same machine with very little overhead 🤓). First, it builds the image, which can be built locally *or* imported from the web! Tons of pre-built images exist in public libraries, such as [Docker Hub](https://hub.docker.com/). This tutorial will build off a `miniconda` image that installs and configures conda, a python (as well as non-python) package manager, for us to immediately use. We won't do so in this tutorial, but after you have built an image, you can also publish that for others to use! Note that if the image is too large, as will be the case here, it may be difficult to publish.

Finally, after an image is built, here comes the fun part: you can then create a container, which is a running instance of the image on your machine! You can access its files, make changes, etc., and so long as you don't destroy the container, then any changes you make will persist between stopping and restarting the container. However, you can imagine scenarios where it is more desirable to have direct access to files inside the container e.g. generated content such as figures and other files. In such cases, you can map local directories to directories on the container, so that any change in the container is reflected in the local directory. We will see this in action.

More will be elaborated on as we proceed through the tutorial. Next, let's set up your machine.

## Setup

+ Clone this repo and `cd` into its root
+ [Follow these instructions to download the Docker client](https://docs.docker.com/desktop/)
    + You can download the GUI or CLI version, depending on your OS
    + If on windows, I highly suggest also getting WSL2 for best performance
+ **You do not need to install Docker on both the host machine and virtual machine**

## Build image

Let's take a look inside the Dockerfile to understand its anatomy. The Dockerfile first specifies a base image, which may look like a light-weight linux OS that comes with python installed. We will use a custom image that configures miniconda for us on a debian machine, as well as other packages useful for ML and RL projects. The image itself contains a rich structure that I won’t bore you with the details of, but essentially each instruction is called a ‘layer’ that can be cached for reuse between different failed builds while you iterate on a Dockerfile that keeps failing to build and I am already tired of this conversation.

The rest of the Dockerfile consists of additional instructions that usually follow this structure: create a working directory inside the container > move your local files to the container (local filepaths should be relative to the directory the Dockerfile lives in) > build tools necessary for development ie. install packages, download repos, create conda environments, etc. You can read the Dockerfile comments for more details, especially if you plan to design your own Dockerfile at some point. These are quite versatile files capable of generating multiple types of images from the same file, and ChatGPT is your friend :).

To build the image, make sure you are in the same directory as the Dockerfile and run the following in terminal, replacing the placeholder with a name:

```
docker build -t <image_name> .
```

and see Docker at work! This may take a few minutes since the image is big...

## Run container

Once the image completes building, you can start running a container! The command to do this looks a little involved, but we'll break it apart.

```
docker run --name test --gpus all -p 8888:8888 -v .:/workspace -it <image_name>
```

The `--name` flag specifies the name of the container, `--gpus all` tells docker to give the container gpu access (handy for machine learning work), `-p 8888:8888` maps the local port to the container port, so we can interact with jupyter in a local browser, and `-v .:/workspace` maps the local directory (`.`) to the container directory where the project lives `/workspace`. Finally, the remaining flags connect the current terminal to the running container so that you may interact with it-- although,in our case, the container is programmed to run `jupyter lab` on start-up, so you may need to open another terminal and run `docker exec -it test`.

## Develop inside the container

As mentioned previously, you can do all your interaction with the container from a terminal connected to the container. For quality of life reasons, you may elect to connect your favorite IDE to the container instead-- provided that it has support for containers. Assuming you have vscode or something related, just download the `Dev Containers` extension, hit `ctrl + shift + p` to pull up the command palette, and run `Dev Containers: Attach to Running Container`. Since we only have the one container running, it should work perfectly. Allow it a few seconds to set up.

Finally, let's test the environment and `cd` into `notebooks`-- you will notice there is only a `.py` file in there instead of `.ipynb`. This is because the best practice is to share the "source code" of a jupyter notebook and build the notebook itself locally. You can work inside the plain python version of the notebook, if you like. You can also use a nifty utility called `jupytext` that we installed with the pacakge to convert the `.py` file into a notebook. Run `jupytext --sync my-notebook.py`. Now there should be a `my-notebook.ipynb`. 

Run the notebook! If everything is set up correctly, then all the cells should run without issue. Try changing the `moo` function defined inside the `a.py` module of `my_package` and rerun the first cell in the notebook. Does it change? When you open the repo on your local machine, did the code change there as well?




