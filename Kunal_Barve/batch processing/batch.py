import subprocess

# Define the content of the batch file
batch_content = """
@echo off
cls

echo Local IP addresses:
ipconfig | findstr /R "IPv4 Address"

echo Available ports:
netstat -an | findstr /R /C:"^  TCP" /C:"^  UDP" /C:"LISTENING"
"""

# Write the batch file
batch_file_path = "network_info.bat"
with open(batch_file_path, "w") as batch_file:
    batch_file.write(batch_content)

# Define the output file path
output_file_path = "network_info_output.txt"

# Execute the batch file and save the output to a text file
with open(output_file_path, "w") as output_file:
    subprocess.run([batch_file_path], stdout=output_file, shell=True)
