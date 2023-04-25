"""
1. Visit https://www.nvidia.com/download/index.aspx
    - set dropdown
        - Product Type based on Multiple Choice show based user Input (Geforce,NVIDIA RTX etc)
        - Product Series based on Multiple Choice show based user Input
        - Product based on Multiple Choice show based user Input
        - Operating System Windows 10 64 bit Default
        - Download Type Game Ready Driver (GRD) Defult
        - Language English (US) Default
"""
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import subprocess

#________________
# wait for Enter key to be pressed
input("Press Enter to Initiate The Program...")

# execute the next code block
print("Initiating...")


#Detects GPU model
def get_mdl():
    line_as_bytes = subprocess.check_output("nvidia-smi -L", shell=True)
    line = line_as_bytes.decode("ascii")
    _, line = line.split(":", 1)
    line, _ = line.split("(")
    return line.strip()

product_name_func = get_mdl()
print(product_name_func)


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
product_typ_input = input("\n Type Desired Value and Press Enter =>> ")
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

    else:
        print(product_series_input, key)


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

print("\n=> Stable Type of the Driver is Selected")

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

# # create a new Chrome browser instance
# driver = webdriver.Chrome()

# # navigate to the NVIDIA download page
# driver.get("https://www.nvidia.com/download/index.aspx")

# # find the product type dropdown element and select based on Input

# product_series_typ_dropdown = Select(driver.find_element("id","selProductSeriesType"))
# product_series_typ_dropdown.select_by_value(product_typ_input)

# # find the product series dropdown element and select based on Input

# product_series_typ_dropdown = Select(driver.find_element("id","selProductSeries"))
# product_series_typ_dropdown.select_by_value()

# # # get the HTML source code of the page after the selection change
# # html = driver.page_source
# # print(html)

# # # close the browser window
# # driver.quit()
# # exit()