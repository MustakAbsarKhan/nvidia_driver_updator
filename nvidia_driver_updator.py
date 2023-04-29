import urllib.request
import subprocess
import requests
import time
import os
import re
from tqdm import tqdm  # Import tqdm library for progress bar
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

#________________
# wait for Enter key to be pressed
print("\n Getting Started: Welcome to the NVIDIA Driver Updator! \n")
input("\n => Press Enter to Initiate The Program!! ==>> ")

try:
    #Detects GPU model
    def get_mdl():
        line_as_bytes = subprocess.check_output("nvidia-smi -L", shell=True)
        line = line_as_bytes.decode("ascii")
        _, line = line.split(":", 1)
        line, _ = line.split("(")
        return line.strip()

    product_name_func = get_mdl()
    print("\n Current Device: " + product_name_func)

    # execute the next code block
    print("\n Initiating Current Driver Version Check...")

    soup_url = "https://www.nvidia.com/download/index.aspx"

    # send a GET request to the URL and store the response object in a variable
    soup_response = requests.get(soup_url)

    # extract the HTML content from the response object
    html_content = soup_response.content

    # create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    #-----------

    # Define the select "Product Type" Instructions and Take User Preference
    product_type = ""
    product_typ_content = soup.find(id='selProductSeriesType').find_all('option')
    print("\nCHOOSE YOUR DESIRED PRODUCT TYPE:")
    product_typ_dict = {}

    ## using fo loop to fetch and gather all option tag values in a dictionary
    for product_typ in product_typ_content:
            value = product_typ['value']
            text = product_typ.text
            product_typ_dict.update({int(value):text})
            if value == "3" or value == "1":
                print(f" For {text}: Type => {value}")
        
    ## taking user input and validating
    product_typ_input = input("\n Type Desired Value and Press Enter =>>  ")
    product_typ_input = int(product_typ_input)

    if(product_typ_input in product_typ_dict):
        selected_product_typ = product_typ_dict[product_typ_input]
        product_type = selected_product_typ
        print(f"\n=>Selected Product Type: {selected_product_typ}")
    else:
        print("\n=>Invalid input. Please try again.")
        exit()

    #________________
    # wait for Enter key to be pressed
    input("\nPress Enter to continue...")

    # execute the next code block
    print("Executing next code block...")

    #________________
    # Define the select "Product Series" Instructions and Take User Preference
    product_series = ""

    print("\nCHOOSE YOUR DESIRED PRODUCT SERIES:")
    product_series_dict = {129: 'GeForce RTX 40 Series (Notebooks)',127: 'GeForce RTX 40 Series',125: 'GeForce MX500 Series (Notebooks)',124: 'NVIDIA RTX Series (Notebooks)',123: 'GeForce RTX 30 Series (Notebooks)',122: 'NVIDIA RTX Series',121: 'GeForce MX400 Series (Notebooks)',120: 'GeForce RTX 30 Series',117: 'GeForce MX300 Series (Notebooks)', 116: 'Quadro RTX Series (Notebooks)',115: 'GeForce GTX 16 Series (Notebooks)',113: 'GeForce MX200 Series (Notebooks)',112: 'GeForce 16 Series',111: 'GeForce RTX 20 Series (Notebooks)', 109: 'Quadro RTX Series',107: 'GeForce RTX 20 Series',104: 'GeForce MX100 Series (Notebook)',102: 'GeForce 10 Series (Notebooks)',101: 'GeForce 10 Series',99: 'GeForce 900M Series (Notebooks)',98: 'GeForce 900 Series',97: 'GeForce 800M Series (Notebooks)',95: 'GeForce 700 Series',92: 'GeForce 700M Series (Notebooks)',85: 'GeForce 600 Series',84: 'GeForce 600M Series (Notebooks)',78: 'GeForce 500M Series (Notebooks)',76: 'GeForce 500 Series', 74: 'Quadro Series (Notebooks)', 73: 'Quadro Series',72: 'GeForce 400M Series (Notebooks)',71: 'GeForce 400 Series',70: 'GeForce 300 Series',69: 'GeForce 300M Series (Notebooks)', 65: 'Quadro Blade/Embedded Series',62: 'GeForce 200M Series (Notebooks)',61: 'GeForce 100M Series (Notebooks)',59: 'GeForce 100 Series',55: 'GeForce Go 7 Series (Notebooks)',54: 'GeForce 8M Series (Notebooks)',53: 'GeForce 9M Series (Notebooks)',52: 'GeForce 200 Series',51: 'GeForce 9 Series', 47: 'Quadro SDI', 42: 'Quadro FX Series (Notebooks)', 39: 'Quadro NVS Series (Notebooks)', 32: 'Quadro Sync Series', 16: 'Quadro2 Go Series', 15: 'Quadro4 Go Series', 13: 'Quadro DCC Series', 12: 'Quadro4 XGL Series', 11: 'Quadro NVS Series', 10: 'Quadro FX Series', 9: 'Quadro Plex Series',4: 'GeForce 5 FX Series',3: 'GeForce 6 Series',2: 'GeForce 7 Series',1: 'GeForce 8 Series'
        }

    ## printing series based on product type
    for key, value in product_series_dict.items():
        if(product_type == "GeForce" and key in [129, 127, 125, 123, 122, 121, 120, 117, 115, 113, 112, 111, 107, 105, 104, 102, 101, 99, 98, 97, 95, 92, 85, 84, 78, 76, 73, 72, 71, 70, 69, 62, 61, 59, 55, 54, 53, 52, 51, 4, 3, 2, 1]):
            print(f"For Series {value}: Type => {key}")  
            
        elif(product_type == "NVIDIA RTX / Quadro" and key in [122, 124, 116, 109, 74, 73, 65, 47, 42, 39, 32, 16, 15, 13, 12, 11, 10, 9]):
            print(f"For Series {value}: Type => {key}")
        

    product_series_input = input("\nType Desired Value and Press Enter =>>")

    for key, value in product_series_dict.items():
        if int(key) == int(product_series_input):
            product_series = value
            print(f"\n=>Selected Product Series: {product_series}")
            break


    #________________
    # wait for Enter key to be pressed
    input("\nPress Enter to continue...")

    # execute the next code block
    print("\nExecuting next code block...")

    #_________________
    # Detecting the Product

    product_name_store = product_name_func
    if product_type == "GeForce":
        product_name = product_name_store.split("NVIDIA ")[1]
    else:
        product_name = product_name_store
        
    print(f"\n=> Detected Device: {product_name}")

    #________________
    # wait for Enter key to be pressed
    input("\nPress Enter to continue...")

    # execute the next code block
    print("\nExecuting next code block...")

    #_________________
    Operating_System = ""
    #Detecting the OS
    print("\nCHOOSE YOUR OPERATING SYSTEM:")
    op_sys_dict = {57:"Windows 10 64-bit",135:"Windows 11",19:"Windows 7 64-bit",41:"Windows 8.1 64-bit",28:"Windows 8 64-bit",44:"Windows Server 2012 R2 64",74:"Windows Server 2016",119:"Windows Server 2019",134:"Windows Server 2022",124:"Linux aarch64",12:"Linux 64-bit",13:"Solaris x86/x64",22:"FreeBSD x64"} 

    for key, value in op_sys_dict.items():
        print(f" For OS {value}: Type => {key}")

    ## taking user input and validating
    op_sys_input = input("\n Type Desired Value and Press Enter =>>")
    op_sys_input = int(op_sys_input)

    if(op_sys_input in op_sys_dict):
        selected_os = op_sys_dict[op_sys_input]
        Operating_System = selected_os
        print(f"\n=>Selected Operating System: {selected_os}")
    else:
        print("\n=>Invalid input. Please try again.")
        exit()
        
    #________________
    # wait for Enter key to be pressed
    input("\nPress Enter to continue...")

    # execute the next code block
    print("\nExecuting next code block...")
    
    #__________________'
    # Choosing the stable download type

    download_typ = 1 #Production Branch/Studio

    print("\n=> Game Ready Driver (GRD) is Selected (Default)")

    #________________
    # wait for Enter key to be pressed
    input("\nPress Enter to continue...")

    # execute the next code block
    print("\nExecuting next code block...")

    #_________________
    # select the language
    language = ""
    lang_op_content = soup.find(id='ddlLanguage').find_all('option')
    print(lang_op_content)

    print("\nCHOOSE YOUR DESIRED LANGUAGE:")
    lang_op_dict = {}

    ## using fo loop to fetch and gather all option tag values in a dictionary
    for lang_op in lang_op_content:
        value = lang_op['value']
        text = lang_op.text
        lang_op_dict.update({int(value):text})
        
        print(f" For {text} Language: Type => {value}")

    ## taking user input and validating
    lang_op_input = input("\n Type Desired Value and Press Enter =>> ")
    lang_op_input = int(lang_op_input)

    if(lang_op_input in lang_op_dict):
        selected_lang_typ = lang_op_dict[lang_op_input]
        language = selected_lang_typ
        print(f"\n=>Selected Language: {selected_lang_typ}")
    else:
        print("\n=>Invalid input. Please try again.")
        exit()

    #________________
    # wait for Enter key to be pressed
    input("\nPress Enter to Check The Summary...")

    # execute the next code block
    print("\n Printing The Summary...")
    #________________

    #Summary
    print(f"\nProduct Type: {product_type}")
    print(f"Product Series: {product_series}")
    print(f"Product Name: {product_name}")
    print(f"Operating System: {Operating_System}")
    print(f"Download Type: Production Branch/Studio")
    print(f"Language: {language}")

    #________________
    # wait for Enter key to be pressed
    input("\n => Press Enter to Check The Latest Official Version!! ==>> ")


    # check if Chrome is installed
    print("\n => Checking The Latest Official Version....\n")

    # create options object
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # create webdriver object
    driver = webdriver.Chrome(options=chrome_options)
    # navigate to the NVIDIA download page
    driver.get("https://www.nvidia.com/download/index.aspx")

    # find the product type dropdown element and select based on Input

    product_typ_dropdown = Select(driver.find_element("id","selProductSeriesType"))
    product_typ_dropdown.select_by_value(str(product_typ_input))

    # find the product series dropdown element and select based on Input

    product_series_dropdown = Select(driver.find_element("id","selProductSeries"))
    product_series_dropdown.select_by_value(product_series_input)

    #_________________________________
    # find the product name dropdown element and select based on Input
    product_dropdown = Select(driver.find_element('id','selProductFamily'))
    options = product_dropdown.options
    for option in options:
        if(option.text == product_name):
            product_dropdown.select_by_value(option.get_attribute("value"))


    # find the operating system dropdown element and select based on Input
    os_dropdown = Select(driver.find_element("id","selOperatingSystem"))
    os_dropdown.select_by_value(str(op_sys_input))

    # find the download type dropdown element and select based on Input

    dt_dropdown = Select(driver.find_element("id","ddlDownloadTypeCrdGrd"))
    dt_dropdown.select_by_value(str(download_typ))

    # find the language type dropdown element and select based on Input

    lang_dropdown = Select(driver.find_element("id","ddlLanguage"))
    lang_dropdown.select_by_value(str(lang_op_input))

    # find the search button element
    search_button = driver.find_element("xpath",'//a[btn_drvr_lnk_txt="Search"]')

    # click the search button
    search_button.click()

    # get the current URL after clicking the search button
    current_url = driver.current_url
    print(current_url)

    # close the browser window
    driver.quit()
    # exit()


    #______________________
    #Soo Deep! Working on the second page!

    # get the current URL after clicking the search button
    current_url = current_url

    # fetch the HTML content of the page
    new_response = requests.get(current_url)
    new_html = new_response.content

    # parse the HTML content with BeautifulSoup
    new_soup = BeautifulSoup(new_html, 'html.parser')

    # find the latest version file size
    parent = new_soup.find('div', {'id': 'rightContent'})
    table_tbody = parent.find('table').find('tbody')

    tr_version = table_tbody.find_all('tr')[0]
    td_version_data = tr_version.find('td', {'id': 'tdVersion'}).text.strip()

    match = re.search(r'\d+(\.\d+)?', td_version_data)

    if match:
        latest_version = match.group(0)
    else:
        print('\n => No version number found. Check Internet')

    tr_version_size = table_tbody.find_all('tr')[5]
    tr_version_size_content = tr_version_size.find_all('td')[1]
    latest_version_size = tr_version_size_content.get_text().strip()

    latest_version_data = " => Latest Version: " + latest_version + " & " + "Size: "+ latest_version_size

    print("\n" + latest_version_data)#print

    # checking the current installed Game Ready Driver Version
    output = subprocess.check_output(['nvidia-smi', '--query-gpu=driver_version', '--format=csv'])
    current_driver_version = output.decode().split('\n')[1]

    print(f"\n => Current NVIDIA GRD Version: {current_driver_version}")

    # evaluate which version is newer and download that when needed
    if current_driver_version < latest_version:
        GRD_Version = latest_version
    else:
        print(f"\n => NVIDIA GRD Version:{latest_version} or Higher is already Installed!!")
        
        print(f"\n => Share Your Feedback to ==>> mustak.absar.khan@gmail.com")
        print(f" => © 2023, Mohammad Mustak Absar Khan")
        
        #________________
        # wait for Enter key to be pressed
        input("\n Press Enter to Close The Program \n")
    
        # execute the next code block
        print("\n Closing The Program....\n")
        time.sleep(3)  # pause for 3 seconds
        exit()

    # Set the download URL and file name
    url = f'https://us.download.nvidia.com/Windows/{GRD_Version}/{GRD_Version}-desktop-win10-win11-64bit-international-dch-whql.exe'
    filename = f'GRD{GRD_Version}.exe'

    # Download the file with progress bar
    try:
        print(f"\n => Downloading {url}...")
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

        print(f"\n => Download complete. File saved as {filename}.")
    except urllib.error.HTTPError as e:
        print(f"\n => Error downloading {url}: {e}. Please check the version number and try again.")
        exit()
    except urllib.error.URLError as e:
        print(f"\n => Error downloading {url}: {e}.")
        exit()

    # Install the driver
    try:
        print(f"\n => Installing {filename}...")
        cmd = filename
        driver_install_command = subprocess.call(cmd, shell=True)
        print(f"\n => Installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"\n => Error installing {filename}: {e}.")
        exit()

    # Delete the downloaded file
    try:
        os.remove(filename)
        print(f"\n => {filename} deleted.")
    except OSError as e:
        print(f"\n => Error deleting {filename}: {e}")

    #________________
    # wait for Enter key to be pressed
    input("\n Press Enter to Close The Program \n")

    # execute the next code block
    print("Closing The Program....")
    time.sleep(3)  # pause for 3 seconds
    exit()

except Exception as e:
    print("\n This Program Has Ran Into A Problem. Please Contact Admin @ mustak.absar.khan@gmail.com \n")
    print("\n Error:\n",e)
    
