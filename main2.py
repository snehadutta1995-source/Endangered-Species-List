import requests
from bs4 import BeautifulSoup
import csv
import random

print("Scraping endangered mammals data...\n")

keywords = [
    "african", "afrosoricids", "antillean", "arvicolines", "asian",
    "bathyergids", "borneo", "bovids", "bowhead", "calomyscids",
    "canids", "capromyids", "caviids", "cercopithecoids", "cervids"
]

print("👉 You can try these keywords:")
print(",".join(keywords))
print()


user_key = input("Enter a keyword from above: ").lower()


url = "https://en.wikipedia.org/wiki/List_of_critically_endangered_mammals"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []


for li in soup.find_all("li"):
    text = li.get_text()

    if user_key in text.lower():
        common_name = text.split("(")[0].strip()
        scientific_name = "Unknown"
        region = "Worldwide"

        if "(" in text and ")" in text:
            scientific_name = text[text.find("(")+1:text.find(")")]

        result = f"{common_name} ({scientific_name}) - Endangered [{region}]"
        results.append(result)

# 💖 Heart-melting conclusions.....
conclusions = [
    "Every endangered animal is a silent cry of nature, waiting for humans to listen with kindness.",
    "Saving animals is not a choice, it is our responsibility toward the life we share this planet with.",
    "When an animal disappears, a part of nature’s soul fades away forever.",
    "Protecting wildlife today means gifting a beautiful tomorrow to future generations.",
    "These animals cannot speak for themselves, but our actions can speak for them."
]

final_message = random.choice(conclusions)

with open("endangered_species.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Animal-Info"])
    for item in results:
        writer.writerow([item])

    writer.writerow([])
    writer.writerow(["Conclusion"])
    writer.writerow([final_message])

print("\n✅ Results saved to endangered_species.txt")
print("✅ Data saved to endangered_species.csv\n")

print("Sample results:")
for item in results[:4]:
    print(item)


print("\n🌍 Conclusion:")
print("\033[1m" + final_message + "\033[0m")

print("\nCreated by Himali Parveen & Sneha Dutta.")
print("Copyrighted by NSTI(W), Kolkata in 2025.")
