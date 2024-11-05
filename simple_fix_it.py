import numpy as np;
import matplotlib.pyplot as plot;
import pandas as pd;

def f(x):
    return np.cos(x)

x_current=0.5;
tol=1e-5;
max_it=50;
iterations = [x_current];
convergence= False;


for i in range(max_it):
    x_next= f(x_current);
    iterations.append(x_next);

    if (abs(x_next-x_current)<tol): 
        convergence=True;
        print(f"Convergence Found at iteration {i+1}");
        break;

    x_current=x_next;

if convergence!=True:
    print("No Result");
else:
    print(f"Result is {x_next}")

df = pd.DataFrame(iterations, columns=["Values"]);

print(df);

plot.plot(iterations, marker='o');
plot.show();

