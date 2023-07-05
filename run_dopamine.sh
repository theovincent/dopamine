source env/bin/activate

export XLA_PYTHON_CLIENT_MEM_FRACTION=0.89

GAME=$1

python -um dopamine.discrete_domains.train --base_dir experiments/IQN/$GAME/$SLURM_ARRAY_TASK_ID --gin_files dopamine/jax/agents/implicit_quantile/configs/implicit_quantile_one_step_$GAME.gin