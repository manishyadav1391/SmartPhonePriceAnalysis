{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cfcef9f0-2ed1-443a-a726-0f065bdaa901",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "import time\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4196918f-2e57-4f47-93f9-8bfa8a60b9cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Page Title: Amazon.in : smartphones\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import time\n",
    "\n",
    "# Set up Chrome options\n",
    "chrome_options = Options()\n",
    "\n",
    "# Spoof User-Agent to look like a real browser\n",
    "chrome_options.add_argument(\"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36\")\n",
    "chrome_options.add_argument(\"--headless\")  # Run without opening browser (Optional)\n",
    "chrome_options.add_argument(\"--disable-blink-features=AutomationControlled\")  # Prevent detection\n",
    "\n",
    "# Use webdriver-manager to automatically download the correct ChromeDriver\n",
    "service = Service(ChromeDriverManager().install())\n",
    "\n",
    "# Start the Chrome browser\n",
    "driver = webdriver.Chrome(service=service, options=chrome_options)\n",
    "\n",
    "# Open Amazon's smartphone page\n",
    "url = \"https://www.amazon.in/s?k=smartphones\"\n",
    "driver.get(url)\n",
    "\n",
    "# Wait for page to load\n",
    "time.sleep(5)\n",
    "\n",
    "# Print page title to confirm successful scraping\n",
    "print(\"Page Title:\", driver.title)\n",
    "\n",
    "# Close the browser\n",
    "driver.quit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a8152fb-208e-42b2-830f-a7a44bc0462d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
