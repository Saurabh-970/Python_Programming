#------------------------------------------------------------
# Network Structure :
# Input Layer : 2 inputs
# Hidden Layer : 2 neurons with relu activation
# Output Layer : 1 neuron with sigmoid activation
#------------------------------------------------------------

import math

#------------------------------------------------------------
# ReLU Activation
#------------------------------------------------------------
def Marvellous_ReLU(value):
    return max(0, value)

#------------------------------------------------------------
# Sigmoid Activation
#------------------------------------------------------------
def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))

#------------------------------------------------------------
# Weighted Sum
#------------------------------------------------------------
def Marvellous_Calculate_Weighted_Sum(inputs, weights, bias):
    return sum(weight * input_value for weight, input_value in zip(weights, inputs)) + bias

#------------------------------------------------------------
# Display Multiplication Details
#------------------------------------------------------------
def Marvellous_Display_Multiplication_Details(inputs, weights):
    print(" Step 1 : Multiply inputs by corresponding weights")
    for index in range(len(inputs)):
        print(
            f"  ({weights[index]} * {inputs[index]}) = {weights[index] * inputs[index]:.3f}"
        )

#------------------------------------------------------------
# Hidden Layer Processing
#------------------------------------------------------------
def Marvellous_Process_Hidden_Layer(inputs, hidden_weights, hidden_biases):
    hidden_output = []

    print("\n============== Hidden Layer ==============\n")

    for neuron_index in range(len(hidden_weights)):
        print(f"Hidden Neuron {neuron_index + 1}:")

        current_weight = hidden_weights[neuron_index]
        current_bias = hidden_biases[neuron_index]

        Marvellous_Display_Multiplication_Details(inputs, current_weight)

        z_value = Marvellous_Calculate_Weighted_Sum(inputs, current_weight, current_bias)
        print(f"  Step 2 : Add all results + bias ({current_bias})")
        print(f"  z = {z_value:.3f}")

        activated_output = Marvellous_ReLU(z_value)
        print(f"  Step 3 : Apply ReLU → {activated_output:.3f}\n")

        hidden_output.append(activated_output)

    return hidden_output

#------------------------------------------------------------
# Output Layer Processing
#------------------------------------------------------------
def Marvellous_Process_Output_Layer(hidden_outputs, output_weights, output_bias):
    print("\n================ Output Layer ================\n")
    print("Output Neuron:")

    print(" Step 1 : Multiply hidden outputs with weights")
    for index in range(len(hidden_outputs)):
        print(
            f"  ({output_weights[index]} * {hidden_outputs[index]:.3f}) = "
            f"{output_weights[index] * hidden_outputs[index]:.3f}"
        )

    # OUTSIDE loop (corrected)
    z_output = Marvellous_Calculate_Weighted_Sum(hidden_outputs, output_weights, output_bias)

    print(f" Step 2 : Add all results + bias ({output_bias})")
    print(f"  z = {z_output:.3f}")

    final_output = Marvellous_Sigmoid(z_output)
    print(" Step 3 : Apply Sigmoid")
    print(f"  Sigmoid({z_output:.3f}) = {final_output:.3f}")

    return z_output, final_output

#------------------------------------------------------------
# Final Summary
#------------------------------------------------------------
def Marvellous_Display_Network_Summary(hidden_outputs, final_output):
    print("\n================ FINAL SUMMARY ================\n")
    print(f"Hidden Layer Outputs : {hidden_outputs}")
    print(f"Final Output         : {final_output:.3f}")
    print(f"Confidence          : {final_output * 100:.2f}%")

    if final_output >= 0.5:
        print("Prediction          : Positive Class")
    else:
        print("Prediction          : Negative Class")

#------------------------------------------------------------
# Complete Forward Pass
#------------------------------------------------------------
def Marvellous_ANN_Forward_Pass(inputs):
    print("============ INPUT LAYER ============")
    print(f"x1 = {inputs[0]}")
    print(f"x2 = {inputs[1]}")

    # Hidden Layer (2 neurons)
    hidden_weights = [
        [0.5, -0.2],
        [0.8, 0.4]
    ]

    hidden_biases = [
        0.1,
        -0.1
    ]

    # Output Layer
    out_weights = [1.0, -1.5]
    out_bias = 0.2

    # Forward Pass
    hidden_outputs = Marvellous_Process_Hidden_Layer(
        inputs, hidden_weights, hidden_biases
    )

    z_output, final_output = Marvellous_Process_Output_Layer(
        hidden_outputs, out_weights, out_bias
    )

    Marvellous_Display_Network_Summary(hidden_outputs, final_output)

#------------------------------------------------------------
# Main Function
#------------------------------------------------------------
def main():
    inputs = [2.0, 3.0]
    Marvellous_ANN_Forward_Pass(inputs)

#------------------------------------------------------------
# Entry Point
#------------------------------------------------------------
if __name__ == "__main__":
    main()