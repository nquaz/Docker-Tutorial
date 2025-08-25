# Docker Essentials

The essentials of how Docker works for maintaining reproducible environments and what a workflow for scientific development could look like.

## Pre-reqs
+ Knowledge of python and jupyter
+ An open mind 😀
+ Around 20 GB of space 😁

## Overview
Under `docs`, you will find a tutorial that walks you through basic concepts in Docker and how to run a project containing a jupyter notebook and custom package whose source you can modify, mirroring the typical pipeline for scientific package development.
The notebook is under `notebooks` and the package is under `src\my_package`. Note the generated image takes 20 GB, but this is solely because I wanted the environment to reflect a mature ecosystem of packages ready for heavy workloads ie. training RL agents. You are free to modify the repo as you like.

## Setup
1. Clone this repo
2. Install docker