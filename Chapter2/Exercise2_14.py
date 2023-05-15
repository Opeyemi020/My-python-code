age = int(input("Enter the user age\n"))
maximum_heart_rate = 220 - age

minimum_target_heart_rate = maximum_heart_rate * 0.5
print(f"your maximum heart rate low is {maximum_heart_rate} in beat per minutes.")
maximum_target_heart_rate_range = maximum_heart_rate * 0.85
print(f"your maximum target heart rate range is {minimum_target_heart_rate:.2f} to {maximum_target_heart_rate_range:.2f} beats per minutes. ")
