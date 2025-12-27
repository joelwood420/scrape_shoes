import json
import csv
import requests



def extract_shoes_from_html(html):
    start_marker = '"products":['
    start = html.find(start_marker)
    if start == -1:
        raise RuntimeError("Couldn't find products")

    start += len(start_marker)

    bracket_count = 1
    i = start
    while i < len(html) and bracket_count > 0:
        if html[i] == '[':
            bracket_count += 1
        elif html[i] == ']':
            bracket_count -= 1
        i += 1

    if bracket_count != 0:
        raise RuntimeError("Could not find matching closing bracket for products array")

    products_json_string = '{"products":[' + html[start:i] + '}'

    data = json.loads(products_json_string)
    products = data["products"]

    shoes = []
    for p in products:
        name = p.get("name")
        price = p.get("price", {}).get("formattedValue")
        original_price = p.get("originalPrice", {}).get("formattedValue")
        images = p.get("images", [])
        image_url = images[0]["url"] if images else None

        if name and " - " in name:
            product_name, category = name.split(" - ", 1)
        else:
            product_name = name
            category = "Unknown"

        shoes.append({
            "product_name": product_name,
            "category": category,
            "image_url": image_url,
            "price": price,
            "original_price": original_price
        })

    return shoes


def extract_shoes(use_local_file=True, max_pages=3):

    if use_local_file:
        with open('Foot_locker.html', 'r', encoding='utf-8') as f:
            html = f.read()
        return extract_shoes_from_html(html)
    else:
        base_url = "https://www.footlocker.co.nz/en/category/sale/boxingday?query=%3Arelevance%3Acollection_id%3Asale%3Abrand%3ANike"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        all_shoes = []
        
        for page in range(max_pages):
            if page == 0:
                url = base_url
            else:
                url = f"{base_url}&currentPage={page}"
            
            print(f"Fetching page {page + 1}...")
            
            try:
                resp = requests.get(url, headers=headers)
                resp.raise_for_status()
                html = resp.text
                
                shoes = extract_shoes_from_html(html)
                
                if not shoes:
                    print(f"No shoes found on page {page + 1}, stopping.")
                    break
                
                all_shoes.extend(shoes)
                print(f"Found {len(shoes)} shoes on page {page + 1}")
                    
            except Exception as e:
                print(f"Error fetching page {page + 1}: {e}")
                break
        
        return all_shoes


def save_shoes_to_csv(shoes, filename='shoes.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["product_name", "category", "image_url", "price", "original_price"])
        writer.writeheader()
        for shoe in shoes:
            writer.writerow(shoe)
