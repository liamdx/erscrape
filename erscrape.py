from selenium import webdriver

weapon_url = "https://eldenring.wiki.fextralife.com/Hand+Ballista"

driver = webdriver.Chrome()

driver.get(weapon_url)

possibles = driver.find_elements_by_class_name("lineleft")
texts = []

print("Found Elements:")

# need to identify which element is stat requirements.

for pos in possibles:
    texts.append(pos.text)
    print(pos.get_property("title"))
    print(pos.text)
    print("\n")

driver.close()
driver.quit()