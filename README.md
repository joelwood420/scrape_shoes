# Foot Locker Shoe Scraper 👟

Scrapes shoe data from Foot Locker NZ and saves it to CSV.

## What You Get

A CSV file with: product name, category, image URL, price, and original price.

## Setup

```bash
pip install requests
```

## How to Use

### Test with local file:
```bash
python3 extract_shoes.py
```

### Scrape multiple pages from website:
```bash
python3 scrape_multiple_pages.py
```

That's it! Your data will be in `shoes.csv`

## Change Number of Pages

Edit `scrape_multiple_pages.py` and change this line:
```python
shoes = extract_shoes(use_local_file=False, max_pages=3)  # Change 3 to any number
```

## Output Example

```csv
product_name,category,image_url,price,original_price
Nike Tuned 1,Men Shoes,https://...,NZ$219.95,NZ$270.00
Nike Dunk Low,Women Shoes,https://...,NZ$119.95,NZ$190.00
```
