from time import sleep
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

WITS_TARRIFS_BY_COUNTRY_URL = "https://wits.worldbank.org/tariff/trains/country-byhs6product.aspx?lang=en"

def extract_links(link:str):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

country_links = extract_links(WITS_TARRIFS_BY_COUNTRY_URL)
country_links = list(filter(lambda x: x.startswith('https://wits.worldbank.org/tariff/trains/en/country/'), country_links))
country_links = list(filter(lambda x: not 'covid' in x, country_links))

def extract_localdata_json(link: str):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and 'localdata:' in script.string:
            # Find the localdata array using regex
            match = re.search(r'localdata:\s*(\[[^\]]*\])', script.string, re.DOTALL)


            if match:
                localdata_str = match.group(1) 

                localdata_str = '\n'.join([line for line in localdata_str.splitlines() if not line.strip().startswith('//')])

                # Add double quotes to every property name using regex
                localdata_str = re.sub(r'(\s*)(\w+)\s*:', r'\1"\2":', localdata_str)

                try:
                    # Convert JS array to JSON array if necessary
                    localdata_str = localdata_str.replace("'", '"')
                    localdata = json.loads(localdata_str)

                    if localdata:
                        applied_tariffs = []
                        for item in localdata:
                            try:
                                value = float(item['AppliedTariff'].strip())
                                applied_tariffs.append(value)
                            except (ValueError, TypeError):
                                continue
                        
                        if applied_tariffs:
                            avg_applied_tariff = sum(applied_tariffs) / len(applied_tariffs)
                        else:
                            avg_applied_tariff = None
                        
                        result = {
                            "Reporter": localdata[0].get("Reporter"),
                            "Partner": localdata[0].get("Partner"),
                            "AverageAppliedTariff": avg_applied_tariff
                        }
                        
                        return result

                    return localdata
                except Exception as e:
                    print(f"Error parsing localdata JSON: {e}")
    return []

total = []

DATA_FILE = 'wits_tarrifs.json'
COLLECTED_LINKS_FILE = 'collected_links.json'

# Load already collected links and data if available
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        total = json.load(f)
else:
    total = []

if os.path.exists(COLLECTED_LINKS_FILE):
    with open(COLLECTED_LINKS_FILE, 'r') as f:
        collected_links = set(json.load(f))
else:
    collected_links = set()

def save_progress():
    with open(DATA_FILE, 'w') as f:
        json.dump(total, f, indent=4)
    with open(COLLECTED_LINKS_FILE, 'w') as f:
        json.dump(list(collected_links), f, indent=4)


country_links.reverse()

try:
    for country_link in tqdm(country_links, desc="Processing countries"):
        tarrif_links = extract_links(country_link)
        tarrif_links = list(filter(lambda x: x.startswith(country_link), tarrif_links))
        tarrif_links = [link for link in tarrif_links if link not in collected_links]

        def process_tarrif_link(tarrif_link):
            return extract_localdata_json(tarrif_link)

        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(process_tarrif_link, tarrif_link): tarrif_link for tarrif_link in tarrif_links}
            for future in tqdm(as_completed(futures), total=len(futures), desc=f"Processing {country_link}"):
                tarrif_link = futures[future]
                try:
                    data = future.result()
                    total.append(data)
                    collected_links.add(tarrif_link)
                except Exception as e:
                    print(f"Error processing {tarrif_link}: {e}")
                finally:
                    save_progress()
except Exception as e:
    print(f"Script interrupted: {e}")
    save_progress()

# Final save
save_progress()