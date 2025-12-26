def compare_ingredients(prod_a: dict, prod_b: dict) -> str:
    if "Vitamin C" in prod_a["ingredients"] and "Vitamin C" not in prod_b["ingredients"]:
        return "Product A focuses on Vitamin C based brightening."
    return "Both products offer basic skincare benefits."

def price_comparison(price_a: int, price_b: int) -> str:
    diff = price_b - price_a
    percent = int((diff / price_b) * 100)
    return f"Product A is approximately {percent}% more affordable."
