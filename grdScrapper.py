import urllib.request
import subprocess
import os
from tqdm import tqdm  # Import tqdm library for progress bar

# Get valid number input or assign default value
while True:
    GRD_Version = input("Please enter a valid version number (e.g. 531.68) or leave it blank for the default version (531.68): ")
    if GRD_Version.strip() == "":
        GRD_Version = "531.68"
        break
    try:
        float(GRD_Version)
        break
    except ValueError:
        print("Invalid input. Please enter a valid version number.")

# Set the download URL and file name
url = f'https://us.download.nvidia.com/Windows/{GRD_Version}/{GRD_Version}-desktop-win10-win11-64bit-international-dch-whql.exe'
filename = f'GRD{GRD_Version}.exe'

# Download the file with progress bar
try:
    print(f"Downloading {url}...")
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        file_size = int(response.info().get('Content-Length', -1))
        if file_size == -1:
            print('Could not determine file size. Downloading without progress bar.')
            out_file.write(response.read())
        else:
            # Use tqdm for progress bar
            with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc=filename) as progress_bar:
                while True:
                    buffer = response.read(1024*1024)
                    if not buffer:
                        break
                    out_file.write(buffer)
                    progress_bar.update(len(buffer))

    print(f"Download complete. File saved as {filename}.")
except urllib.error.HTTPError as e:
    print(f"Error downloading {url}: {e}. Please check the version number and try again.")
    exit()
except urllib.error.URLError as e:
    print(f"Error downloading {url}: {e}.")
    exit()

# Install the driver
try:
    print(f"Installing {filename}...")
    cmd = filename
    driver_install_command = subprocess.call(cmd, shell=True)
    print(f"Installation complete.")
except subprocess.CalledProcessError as e:
    print(f"Error installing {filename}: {e}.")
    exit()

# Delete the downloaded file
try:
    os.remove(filename)
    print(f"{filename} deleted.")
except OSError as e:
    print(f"Error deleting {filename}: {e}")
