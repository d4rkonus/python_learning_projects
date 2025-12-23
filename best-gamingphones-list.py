#!/usr/bin/python3

# Smartphones
smartphones = {
    "Black Shark 5 Pro": {"brand": "Xiaomi", "price": 699, "memory": "256GB"},
    "ROG Phone 9 Pro": {"brand": "Asus", "price": 799, "memory": "512GB"},
    "REDMAGIC 11 Pro": {"brand": "REDMAGIC", "price": 749, "memory": "256GB"},
    "Honor Play": {"brand": "Honor", "price": 499, "memory": "128GB"}
}

# Sells and position
global_sells = {
    "Black Shark 5 Pro": (30_000_000, "Asia", "Europa"),
    "ROG Phone 9 Pro": (50_000_000, "America", "Europa"),
    "REDMAGIC 11 Pro": (70_000_000, "America","Antartida"),
    "Honor Play": (40_000_000, "Africa", "Oceania"),  
}

# Mostrar todos los teléfonos
for i, model in enumerate(smartphones.keys()):
    brand = smartphones[model]["brand"]
    price = smartphones[model]["price"]
    memory = smartphones[model]["memory"]
    
    sells, region1, region2 = global_sells[model]

    print(f"\n[+] {i+1} Smartphone name: {model} by {brand}")
    print(f"  [-] Price: ${price}")
    print(f"  [-] Memory: {memory}")
    print(f"  [-] Sells: {sells:,}".replace(",", ".") + " copies sold")
    print(f"  [-] Best-selling regions: {region1}, {region2}\n")
