from algorithm import *

#Task 1: points in a 2d-plane
I = 1000 #Number of pictures (in this case: points)
d = 2 #dimension

Y_0, c = get_data_spiral_2d(I) #Til oppgave 1: 
c = c[:,0]  #for å få en Ix1 vektor 
Y_Kk, J, omega, my, iterations = algorithm(Y_0, c, I, d)

print(J[0],J[-1])  #god overenstemmelse

plot_cost_function_convergence(iterations, J)

plot_progression(Y_Kk, c) 

r = 1000 #resolution of plot
plot_separation(last_function, Y_Kk[-1,:,:], c, r, omega, my)