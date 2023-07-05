#!/bin/bash

docker run -it --rm --mount type=bind,src=/home/$USER/dopamine/,dst=/home/$USER/dopamine/ idqn bash -c cd /home/$USER/dopamine && $@