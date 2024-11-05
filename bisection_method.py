import numpy as np
import matplotlib.pyplot as plot
import pandas as pd


def f(x):
    return np.exp(-x)* (3.2*np.sin(x)- 0.5*np.cos(x));

def bisection(a,b,tol):
    steps =[];
    while (b-a)/2 > tol:
        mid= (b+a)/2;
        steps.append((a,b,mid,f(mid)));
        if f(mid)==0:
            return mid;
        elif f(a)* f(mid) <0:
            b=mid;
        else:
            a=mid;
    
    return (a+b)/2, steps; 
        





a,b,tol=3,4,0.001;

root, steps = bisection(a,b,tol);

df = pd.DataFrame(steps, columns=["a", "b", "mid", "f(mid)"]);
print(df);


x_val = np.linspace(3,4,1000);
y_val= f(x_val)

plot.plot(x_val, y_val, label="f(x)= e^(-x) sinx - cosx");
plot.axhline(0, color="black", lw=.5,);
plot.axvline(root, color="red", linestyle=":", label=f"Root: {root:.5f}");
plot.xlabel("x")
plot.ylabel("f(x)")
plot.title("Bisection Method Root Finding")
plot.legend();
plot.show();