import numpy as np
import pickle

experiment_name = "IQN/KungFuMaster"


metric = np.zeros((200, 5))



for idx_epoch in range(200):
    for idx_seed in range(5):
        with open(f"experiments/{experiment_name}/{idx_seed + 1}/metrics/pickle/pickle_{idx_epoch}.pkl", "rb") as f:
            data = pickle.load(f)
        
        metric[idx_epoch, idx_seed] = data[f"iteration_{idx_epoch}"]["Train/AverageReturns"][0]


np.save(f"experiments/{experiment_name}/metric.npy", metric)