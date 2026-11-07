"""
Product Steps for loading BDD background data
"""
import requests
from behave import given
from compare import expect


@given('the following products')
def step_impl(context):
    """Delete all Products and load new ones"""
    # List all of the products and delete them one by one
    response = requests.get(f"{context.base_url}/products")
    expect(response.status_code).to_equal(200)
    for product in response.json():
        res = requests.delete(f"{context.base_url}/products/{product['id']}")
        expect(res.status_code).to_equal(204)

    # load the database with new products
    for row in context.table:
        payload = {
            "name": row['name'],
            "description": row['description'],
            "price": row['price'],
            "available": row['available'] in ['True', 'true', '1'],
            "category": row['category']
        }
        response = requests.post(f"{context.base_url}/products", json=payload)
        expect(response.status_code).to_equal(201)
