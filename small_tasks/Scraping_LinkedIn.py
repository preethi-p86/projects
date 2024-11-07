from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import xlwt

# Set up Chrome options to keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Set up the WebDriver
driver = webdriver.Chrome(options=chrome_options)  # Ensure ChromeDriver is in your PATH

# Navigate to LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Log in to LinkedIn
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("Email***")  # Replace with your LinkedIn email
password.send_keys("Password***")           # Replace with your LinkedIn password
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for the login to complete
time.sleep(5)

# Navigate to the specific URL

# Initialize workbook
wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0,0,'S.NO')
sheet1.write(0,1,'Name')
sheet1.write(0,2,'Software')
sheet1.write(0,3,'Product')
sheet1.write(0,4,'E-mail')

row_count = 1


for i in range(1,101):

    url = f"https://www.linkedin.com/search/results/products/?keywords=%20&origin=FACETED_SEARCH&page={i}&productCategory=%5B%221114%22%2C%221263%22%2C%221157%22%5D&sid=dVH"
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)

    # Get the page source and parse with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Example: Find the specific main element
    main_divs = soup.find_all('main', class_='scaffold-layout__main')

    # Debug: Print number of main divs found
    print(f"Number of main divs found: {len(main_divs)}")

    # Index for writing rows in the Excel sheet

    # Loop through the found main_divs
    for main_div in main_divs:
        search_divs = main_div.find_all('div', class_='search-marvel-srp')
        
        # Debug: Print number of search divs found in each main div
        print(f"Number of search divs found: {len(search_divs)}")
        
        for search_div in search_divs:
            ul = search_div.find('ul')
            
            # Debug: Print if ul is found
            if ul:
                print("ul found")
                lis = ul.find_all('li')
                
                # Debug: Print number of li elements found in ul
                print(f"Number of li elements found: {len(lis)}")
            
                for li in lis:
                    name_tag = li.find('div', class_='t-roman t-sans')
                    software_tag = li.find('div', class_='entity-result__primary-subtitle t-14 t-black t-normal')
                    
                    if name_tag and software_tag:
                        name = name_tag.text.strip()
                        software_text = software_tag.text.strip()
                        software, product = software_text.rsplit(' by ', 1)
                        
                        print(row_count, '\n', name, '\n', software, '\n', product, '\n')
                        
                        sheet1.write(row_count, 0, row_count)
                        sheet1.write(row_count, 1, name)
                        sheet1.write(row_count, 2, software)
                        sheet1.write(row_count, 3, product)
                        row_count += 1

# Save the workbook
wb.save('Products.xls')

# Close the WebDriver (if you don't want to keep it open)
# driver.quit()
