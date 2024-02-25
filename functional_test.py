from selenium import webdriver

browser = webdriver.Firefox()
browser.get("htttp://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")