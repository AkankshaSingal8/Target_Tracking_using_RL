import os
#gain = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.4]
#delay = [0, 10, 20, 30, 40, 50]

gain = [0.6]
delay = [0.05]
for g in gain:
    for d in delay:
        os.system("python train.py --gain {} --delay {}".format(g, d))
