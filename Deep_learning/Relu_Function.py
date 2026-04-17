#-----------------------------------------------
# Program : Aritifical Neuron with Relu Activation
# Author  : Saurabh Ravindra Bhonsle
#-----------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#-----------------------------------------------
# Step 1 : Activation Function (Relu)
#-----------------------------------------------

# Relu = max(0, z)
# If z is positive -> output z
# If z is negative -> output 0

def relu(z):
    return max(0,z)

#-----------------------------------------------
# Step 2 : Neuron Forward Pass Function
#-----------------------------------------------

# This Function simulates a single artifical neuron
# It performs :
# 1. Input x Weight multiplication
# 2. Summation + bias
# 3. Activation (Relu)

def Marvellous_neuron_forward(inputs,weights,bias):

    print("\n------Neuron Calculation Start-----\n")

    # Display inputs and weights
    print("Inputs (X) :", inputs)
    print("Weights (W) :",weights)
    print("Bias (b) :",bias)

#-----------------------------------------------
# # Step 2.1 : Weighted Sum Calculation
# # Formula : Z =(x1*w1 + x2*w2 + ...+xn*wn)+bias
#-----------------------------------------------

    z = sum(w * x for w,x in zip(weights,inputs)) + bias    

    print("\nStep 1 : Weighted Sum Claculation ")
    print("z = w.x + b =",z)

#-----------------------------------------------
# Step 2.2 : Activation Function
#-----------------------------------------------

    y_hat = relu(z)

    print("\nStep 2 : Activation function Applied")
    print("Activation Function : Relu")
    print("Output(y) =", y_hat)

    print("\n------Neuron Calculation End-------\n")

    return z,y_hat

#-----------------------------------------------
# Step 3 : Plot Relu Function
#-----------------------------------------------
# This helps to visualize how Relu behaves

def plot_relu():

    # Generate range of values for z

    z_values = np.linspace(-10,10,200)


    # Apply Relu on all values
    relu_values = np.maximum(0, z_values)


    # Plot Graph
    plt.figure(figsize =(8,5))
    plt.plot(z_values, relu_values, label = "ReLU Function", linewidth =2, color="green")


    # Axex lines
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray",linestyle="--")

    # Lables and titles
    plt.title("ReLU Activation Function ", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    #Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Show graph
    plt.show()

#-----------------------------------------------
# Step 4 : Main Function
#-----------------------------------------------

def main():
    print("\n============Marvellous Neuron Demo==========\n")

    # Example  input (features)

    inputs = [1.0,2.0,3.0]

    # Corresponding weights

    weights = [0.6,0.4,-0.2]

    #Bias value
    bias = 0.5

    #Perform forward propagation
    z,y_hat = Marvellous_neuron_forward(inputs, weights,bias)

    #Plot ReLU graph
    plot_relu()


if __name__ == "__main__":
    main()        

    