"""
Application Tier
Handles business logic for the shopping application
"""

from db.database import get_products

def show_products():
    return get_products()

if __name__ == "__main__":
    products = show_products()
    print("Available Products:")
    for product in products:
        print("-", product)
