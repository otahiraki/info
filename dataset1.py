import numpy as np
import matplotlib.pyplot as plt

# 真の関数
def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

if __name__ == "__main__":
    print(true_function(np.array([0])))

if __name__ == "__main__":
    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    plt.plot(x, y, label="true function")
    plt.legend()
    plt.savefig("ex1.1.png")
    plt.show()