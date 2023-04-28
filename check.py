import subprocess

output = subprocess.check_output(['nvidia-smi', '--query-gpu=driver_version', '--format=csv'])
driver_version = output.decode().split('\n')[1]

print(f"The current NVIDIA driver version is: {driver_version}")