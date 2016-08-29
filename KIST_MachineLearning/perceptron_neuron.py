import numpy as np

def activation(weight, x):
    return np.dot(weight, x)

def output(weight, x):
    b = 1
    if (np.dot(weight, x) + b) > 0:
        return 1
    else:
        return 0

def main():
    weight = [1, 0.5, -0.7, 0.1]
    x = [0, 1, 1, 0]

    if output(weight, x) == 1:
        print("My neuron fired a signal")
    else:
        print("My neuron did not fire a signal")

if __name__ == "__main__":
    main()
