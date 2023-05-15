seconds = int(input("Enter number of seconds: \n"))
hour = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print(f"{hour}-{minutes}-{seconds}")
