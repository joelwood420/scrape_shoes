import json
import csv



def extract_shoes():
   url = "https://www.footlocker.co.nz/en/category/sale/boxingday?query=%3Arelevance%3Acollection_id%3Asale%3Abrand%3ANike"
   headers = {
    "User-Agent": "Mozilla/5.0" 
}

   with open('Foot_locker.html', 'r', encoding='utf-8') as f:
       html = f.read()


   start_marker = '"products":['
   start = html.find(start_marker)
   if start == -1:
       raise RuntimeError("Could not find products JSON in page")

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

   products_json_str = '{"products":[' + html[start:i] + '}'

   data = json.loads(products_json_str)
   products = data["products"]

   shoes = []
   for p in products:
       name = p.get("name")
       price = p.get("price", {}).get("formattedValue")
       original_price = p.get("originalPrice", {}).get("formattedValue")
       images = p.get("images", [])
       image_url = images[0]["url"] if images else None

       shoes.append({
           "name": name,
           "image_url": image_url,
           "price": price,
           "original_price": original_price
       })

   return shoes

def save_shoes_to_csv(shoes, filename='shoes.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "image_url", "price", "original_price"])
        writer.writeheader()
        for shoe in shoes:
            writer.writerow(shoe)

if __name__ == "__main__":
    shoes = extract_shoes()
    save_shoes_to_csv(shoes)
    for shoe in shoes:
         name = shoe["name"]
         image_url = shoe["image_url"]
         price = shoe["price"]
         original_price = shoe["original_price"]
         