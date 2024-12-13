import pandas as pd
import os

gain = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]
delay = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

episodes = 5

with open("results_log.txt", "w") as log_file:
    for g in gain:
        for d in delay:
            log_file.write(f"Gain: {g}, Delay: {d}\n")

            df = pd.read_csv(f"output/error_{g}_{d}.csv")
            df.columns = ['x_error', 'y_error', 'z_error']

            x_error_2 = sum(df['x_error']) / episodes
            y_error_2 = sum(df['y_error']) / episodes
            z_error_2 = sum(df['z_error']) / episodes
            norm_error = (x_error_2**2 + y_error_2**2 + z_error_2**2)**0.5

            log_file.write(f"mean x_error: {x_error_2}\n")
            log_file.write(f"mean y_error: {y_error_2}\n")
            log_file.write(f"mean z_error: {z_error_2}\n")
            log_file.write(f"mean norm_error: {norm_error}\n")

            rows = len(df)
            part = int(rows / episodes)

            x_error = []
            y_error = []
            z_error = []

            for i in range(episodes):
                x_error.append(sum(df['x_error'][i*part:(i+1)*part]))
                y_error.append(sum(df['y_error'][i*part:(i+1)*part]))
                z_error.append(sum(df['z_error'][i*part:(i+1)*part]))

            mean_x = sum(x_error) / episodes
            mean_y = sum(y_error) / episodes
            mean_z = sum(z_error) / episodes

            x_error_std = 0
            y_error_std = 0
            z_error_std = 0

            for i in range(episodes):
                x_error_std += (x_error[i] - mean_x)**2
                y_error_std += (y_error[i] - mean_y)**2
                z_error_std += (z_error[i] - mean_z)**2

            x_error_std = (x_error_std / (episodes - 1))**0.5
            y_error_std = (y_error_std / (episodes - 1))**0.5
            z_error_std = (z_error_std / (episodes - 1))**0.5

            log_file.write(f"std of x: {x_error_std}\n")
            log_file.write(f"std of y: {y_error_std}\n")
            log_file.write(f"std of z: {z_error_std}\n")
            log_file.write(f"std of norm: {(x_error_std**2 + y_error_std**2 + z_error_std**2)**0.5}\n")
            log_file.write("------------------------------------\n")

        
        
        

        
