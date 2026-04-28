import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def create_dataset(n=20, seed=0):
    np.random.seed(seed)

    x = np.random.uniform(-1, 1, n)
    y = true_function(x)

    # ノイズ追加
    noise = np.random.normal(0, np.sqrt(2), n) / 2
    y_obs = y + noise

    df = pd.DataFrame({
        "観測点": x,
        "真値": y,
        "観測値": y_obs
    })

    return df

if __name__ == "__main__":
    x_line = np.linspace(-1, 1, 100)
    y_line = true_function(x_line)

    df = create_dataset()

    plt.plot(x_line, y_line, label="true function")
    plt.scatter(df["観測点"], df["真値"], color="red", label="true value")
    plt.scatter(df["観測点"], df["観測値"], color="green", label="observed")

    plt.legend()
    plt.savefig("ex1.3.png")
    plt.show()