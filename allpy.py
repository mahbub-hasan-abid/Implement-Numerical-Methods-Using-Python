
# def f(x):
#     return x

# def bisection(a,b,tol):
#     steps =[];
#     while (b-a)/2 > tol:
#         mid= (b+a)/2;
#         steps.append((a,b,mid,f(mid)));
#         if f(mid)==0:
#             return mid;
#         elif f(a)* f(mid) <0:
#             b=mid;
#         else:
#             a=mid;
    
#     return (a+b)/2, steps; 


# def false_position(a, b, tol):
#     steps = []
#     if f(a) * f(b) >= 0:
#         print("No root in the interval.")
#         return None, steps

#     while True:
#         # Calculate the false position root
#         root = b - (f(b) * (b - a)) / (f(b) - f(a))
#         steps.append((a, b, root, f(root)))

#         # Stop if we meet tolerance
#         if abs(f(root)) < tol:
#             break

#         # Update interval based on root
#         if f(a) * f(root) < 0:
#             b = root
#         else:
#             a = root

#     return root, steps
        
# def simpson_3_8_no_loop(f, a, b):
#     h = (b - a) / 3  # Step size for 3 subintervals
#     result = (f(a) + 3 * f(a + h) + 3 * f(a + 2 * h) + f(a+3*h)) * ((b-a) / 8)  # Apply Simpson's 3/8 formula for 4 points
#     return result

# def trapezoidal_no_loop(f, a, b):
#     h = (b - a)  # Step size
#     result = (f(a) + f(b)) * (h / 2)  # Apply Trapezoidal formula for 2 points
#     return result

# for i in range(max_it):
#     x_next= f(x_current);
#     iterations.append(x_next);

#     if (abs(x_next-x_current)<tol): 
#         convergence=True;
#         print(f"Convergence Found at iteration {i+1}");
#         break;

#     x_current=x_next;
    
    
    
# def euler_method(dy_dt, h):
#     t_values = []
#     y_values = []
#     t = 0
#     y = 0
#     while t < 5:
#         y += h * dy_dt(t, y)
#         t += h
#         t_values.append(t)
#         y_values.append(y)
#     return t_values, y_values