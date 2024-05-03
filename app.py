from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver (you need to download the appropriate webdriver for your browser)
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
time.sleep(10)  # Allowing time for scanning the QR code manually

# Locate the chat you want to analyze (you may need to inspect the HTML to find the right selector)
chat = driver.find_element_by_xpath("//span[@title='Somalian Pirates']")
chat.click()

# Function to count occurrences of a word in messages
def count_word_occurrences(messages, word):
    count = 0
    for message in messages:
        if word in message.text:
            count += 1
    return count

# Extract messages
messages = driver.find_elements_by_class_name("message-in")  # Assuming 'message-in' is the class for incoming messages
word_to_count = "some"  # Change this to your specific word

# Count occurrences of the word
occurrences = count_word_occurrences(messages, word_to_count)
print(f"The word '{word_to_count}' appeared {occurrences} times.")

# Close the browser
driver.quit()
