# Foot Locker Shoe Scraper

A Python script to scrape shoe data from Foot Locker New Zealand's website.

## Features

- Extract shoe information (name, category, image URL, price, original price)
- Support for pagination to scrape multiple pages
- Export data to CSV format
- Option to use local HTML file for testing or fetch live data

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Use Local HTML File (Default)

By default, the script reads from the local `Foot_locker.html` file:

```python
python3 extract_shoes.py
```

### Option 2: Scrape Multiple Pages from Live Website

To scrape from the live website with pagination, edit `extract_shoes.py` and change:

```python
if __name__ == "__main__":
    # Comment out the local file option:
    # shoes = extract_shoes(use_local_file=True)
    
    # Uncomment this line to fetch from live site:
    shoes = extract_shoes(use_local_file=False, max_pages=3)
```

**Parameters:**
- `use_local_file`: `True` to read from local HTML file, `False` to fetch from website
- `max_pages`: Number of pages to scrape (e.g., `max_pages=3` for 3 pages)

### How Pagination Works

The script automatically:
1. Fetches page 1 (base URL)
2. Fetches page 2 with `&currentPage=1` parameter
3. Fetches page 3 with `&currentPage=2` parameter
4. And so on...

It includes:
- A 2-second delay between requests (to be respectful to the server)
- Error handling for network issues
- Stops if no products are found on a page

## Output

The script generates a `shoes.csv` file with the following columns:

- `product_name` - The shoe/product name (e.g., "Nike Tuned 1")
- `category` - The category (e.g., "Men Shoes", "Women Shoes", "Grade School Shoes")
- `image_url` - Product image URL
- `price` - Sale price
- `original_price` - Original price before discount

## Example

```python
# Scrape 5 pages from the live website
shoes = extract_shoes(use_local_file=False, max_pages=5)
save_shoes_to_csv(shoes, filename='all_shoes.csv')
print(f"Total shoes scraped: {len(shoes)}")
```

## Notes

- The `Foot_locker.html` file is not tracked by git (see `.gitignore`)
- Be respectful when scraping - the script includes delays between requests
- The script may need updates if the website structure changes
