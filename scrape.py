def scrape_webpage(url):
    import chromedriver_autoinstaller
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions
    from selenium.webdriver.support.ui import WebDriverWait
    
    # Checks if the current version of chromedriver exists and
    # if not, downloads it and adds chromedriver to path.
    chromedriver_autoinstaller.install()
    
    # Setting up Chrome browser options.
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  
    chrome_options.add_argument("--incognito")             # Chrome starts as a daemon
    
    # Starting webdriver with set options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Get-Requests given Website and renders it
    driver.get(url)
    print("here")
    _timeout = 10
    print("after")
    WebDriverWait(driver, _timeout).until(
        expected_conditions.presence_of_all_elements_located(
            (By.CLASS_NAME, "fa-check")
        ))
    html = driver.page_source
    driver.close()
    
    return html