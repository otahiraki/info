import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 真の関数
def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

# データセット作成
def create_dataset(n=20, seed=0):
    np.random.seed(seed)

    x = np.random.uniform(-1, 1, n)
    y = true_function(x)

    df = pd.DataFrame({
        "観測点": x,
        "真値": y
    })

    return df

# 実行
if __name__ == "__main__":
    x_line = np.linspace(-1, 1, 100)
    y_line = true_function(x_line)

    df = create_dataset()

    plt.plot(x_line, y_line, label="true function")
    plt.scatter(df["観測点"], df["真値"], color="red", label="samples")

    plt.legend()
    plt.savefig("ex1.2.png")
    plt.show()