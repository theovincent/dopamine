#!/bin/bash

GAME=$1

[ -d experiments/IQN/$GAME/1/ ] || mkdir -p experiments/IQN/$GAME/1
[ -d experiments/IQN/$GAME/2/ ] || mkdir -p experiments/IQN/$GAME/2
[ -d experiments/IQN/$GAME/3/ ] || mkdir -p experiments/IQN/$GAME/3
[ -d experiments/IQN/$GAME/4/ ] || mkdir -p experiments/IQN/$GAME/4
[ -d experiments/IQN/$GAME/5/ ] || mkdir -p experiments/IQN/$GAME/5


echo "launch dopamine"
sbatch -J IQN_dopamine --array=2-2 --cpus-per-task=6 --mem-per-cpu=10G --time=3-00:00:00 --output=experiments/IQN/$GAME/%a/logs.out --gres=gpu:1 -p gpu launch_docker.sh source run_dopamine.sh $GAME
