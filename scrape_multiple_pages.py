
from extract_shoes import extract_shoes, save_shoes_to_csv

if __name__ == "__main__":
    print("Scraping multiple pages from Foot Locker website")
   
    
    shoes = extract_shoes(use_local_file=False, max_pages=3)
    
    save_shoes_to_csv(shoes, filename='shoes.csv')
    
    print(f"\n Total shoes scraped: {len(shoes)}")
    print(f" Saved to: shoes.csv")
    
   
