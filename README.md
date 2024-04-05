# Web Scraping Members from Malaysia Institute of Accountants

This repository contains code for scraping member information from the Malaysia Institute of Accountants website using Selenium. The website does not render its contents with JavaScript, so Selenium was used for dynamic content loading.

## Process Overview

1. **Setup**: Install Selenium and a compatible web driver (e.g., ChromeDriver) for Selenium to interact with the web browser.

2. **Scraping Logic**: Develop scraping logic to navigate through the website, locate member information, and extract relevant data such as firm number, firm name, address, state, country contact, and website.

3. **Selenium Script**: Write a Selenium script in Python to automate the scraping process. This script should handle dynamic content loading and ensure that all necessary data is captured.

4. **Data Extraction**: Implement code to extract the desired information from the website elements using XPath or CSS selectors.

5. **Writing Data**: Write the scraped data into a structured format. In this case, the data will be written into a text file for easy access and manipulation.

6. **Execution**: Run the Selenium script to initiate the scraping process. Ensure that the script navigates through all relevant pages to capture comprehensive member information.

7. **Data Cleaning**: Perform any necessary data cleaning or formatting to ensure the extracted information is accurate and consistent.

8. **Validation**: Validate the scraped data to ensure completeness and accuracy. Manually review a sample of the extracted data to confirm its integrity.

9. **Documentation**: Document the scraping process, including any challenges encountered and the solutions implemented. Provide clear instructions for replicating the scraping process.

## Repository Contents

1. `malaysia.py`: Python script containing the Selenium code for scraping member information from the Malaysia Institute of Accountants website.

2. `requirements.txt`: Text file listing the dependencies required to run the scraping script.

3. `malaysia_membership.txt`: Text file containing the scraped member information, organized in a structured format.

## Usage

1. Clone the repository to your local machine.

2. Install the required dependencies using `pip install -r requirements.txt`.

3. Execute the `malaysia.py` script to initiate the scraping process.

4. Once the scraping is complete, the extracted member information will be written into the `malaysia_membership.txt` file.

5. Access the `malaysia_membership.txt` file to view the scraped member information.

## Notes
- Respect the website's terms of service and scraping policies to avoid any legal issues.
- Periodically review and update the scraping logic to accommodate any changes to the website structure or content.

## Disclaimer

This scraping project is intended for educational and research purposes only. The scraped data should be used responsibly and in accordance with applicable laws and regulations. The repository owner assumes no liability for any misuse of the scraped data.


### website view

![image](https://github.com/FaeyO/webscrapping-members-detail-from-mia.org-website/assets/118575325/7256d020-b6dc-432c-886c-49d91938ad2f)
