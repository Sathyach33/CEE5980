import numpy as np

#constants
a = 7
b = 0.1

#profit function
def profit(x1, x2, x3):
    return np.sin(np.sin(x1)) + a * np.sin(x2) + b * (x3**4) * np.sin(x1)

#Initial values
x = np.array([1.0, 1.0, 1.0])
dx = 0.01

#Base output
y0 = profit(*x)

#sensitivity analysis
sensitivities = []
for i in range(3):
    x_perturbed = x.copy()
    x_perturbed[i] += dx
    y_new = profit(*x_perturbed)
    Si = (y_new - y0) / dx
    sensitivities.append(Si)

#results
for i, Si in enumerate(sensitivities, start=1):
    print(f"S_{i} = {Si:.4f}")

#most influential variable
most_influential = np.argmax(np.abs(sensitivities)) + 1
print(f"\nMost influential variable: x{most_influential}")