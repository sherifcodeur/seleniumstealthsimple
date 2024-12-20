from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

# Path to your ChromeDriver executable
CHROME_DRIVER_PATH = "C:/Users/techo/Desktop/chromedriver.exe"

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: Remove for full browser
options.add_argument('--disable-gpu')  # Disable GPU for headless mode
options.add_argument('--no-sandbox')  # Recommended for headless mode

# Create a Service object
service = Service(CHROME_DRIVER_PATH)

# Create the driver with the Service object
driver = webdriver.Chrome(service=service, options=options)

# Apply stealth settings
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
)

# Navigate to the target URL
driver.get("https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=supermarches+hypermarches&ou=Paris+%2875000%29&univers=pagesjaunes&idOu=")

# Print the page source (HTML response)
print(driver.page_source)

# Quit the driver
driver.quit()
