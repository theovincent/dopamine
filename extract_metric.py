import os
import numpy as np
import pickle
from tqdm import tqdm


for game in tqdm(["Alien", "BankHeist", "ChopperCommand", "Enduro", "Frostbite", "Jamesbond", "KungFuMaster", "Seaquest", "Skiing", "StarGunner"]): 
    experiment_name = f"IQN/{game}"

    metric = np.zeros((200, 5)) * np.nan

    for idx_epoch in range(200):
        for idx_seed in range(5):
            if os.path.exists(f"experiments/{experiment_name}/{idx_seed + 1}/metrics/pickle/pickle_{idx_epoch}.pkl"):
                with open(f"experiments/{experiment_name}/{idx_seed + 1}/metrics/pickle/pickle_{idx_epoch}.pkl", "rb") as f:
                    data = pickle.load(f)
                
                    if data.get(f"iteration_{idx_epoch}", None) is not None:
                        metric[idx_epoch, idx_seed] = data[f"iteration_{idx_epoch}"]["Train/AverageReturns"][0]


    np.save(f"experiments/{experiment_name}/metric.npy", metric)