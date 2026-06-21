import csv
import json

print("Data cleaning and formatting automation initializing...\n")
print("-" * 40)

clean_data = []

with open('products.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:
        product_id = row[0]
        category = row[1]
        price = row[2]

        if category == "" or price == "":
            print(f"[ERROR] Missing data detected for Product ID {product_id}. Skipping.")
        else:
            print(f"[CLEAN] {category} (ID: {product_id}) processed successfully.")

            clean_data.append({
                "Product_ID": product_id,
                "Category": category,
                "Price": int(price)
            })

print("-" * 40)
print(f"Total clean records ready for export: {len(clean_data)}\n")

with open('clean_products.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["Product_ID", "Category", "Price"])
    writer.writeheader()
    writer.writerows(clean_data)
print("[SUCCESS] Clean data successfully saved to 'clean_products.csv'")


with open('clean_products.json', mode='w', encoding='utf-8') as json_file:

    json.dump(clean_data, json_file, indent=4)
print("[SUCCESS] Clean data successfully converted and saved to 'clean_products.json'")