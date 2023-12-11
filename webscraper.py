def dynamic_webscraping_bioconductor_packages_r():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service

    # Path to your Chrome WebDriver executable
    # webdriver_service = Service('/path/to/chromedriver')

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Define the URL
    url = "https://www.bioconductor.org/packages/release/BiocViews.html#___Software"

    # Navigate to the URL
    driver.get(url)

    # Wait for the dynamic content to load (you may need to adjust the waiting time)
    driver.implicitly_wait(10)  # Wait for 10 seconds

    try:
        # Find all rows within the table body
        rows = driver.find_elements(
            By.CSS_SELECTOR, "#biocViews_package_table tbody tr"
        )

        bioc_packages = []
        # Loop through each row
        for row in rows:
            # Find the first td element in the current row
            first_td = row.find_element(By.TAG_NAME, "td")

            # Extract and print the content of the first td element
            bioc_packages.append(first_td.text.strip())
            # print(first_td.text.strip())
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Close the browser
    driver.quit()

    output = open("bioc_packages.csv", "a")
    for package in bioc_packages:
        output.write(str(package) + "\n")
