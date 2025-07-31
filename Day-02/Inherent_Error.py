true_length = 10.12345
measured_length = 10.12

true_area = true_length**2
measured_area = measured_length**2

inherent_error_in_area = abs(true_area - measured_area)

print(f"True Area: {true_area:.8f} m^2")
print(f"Measured Area: {measured_area:.8f} m^2")
print(f"Error in Area due to Inherent Error: {inherent_error_in_area:.8f}")
