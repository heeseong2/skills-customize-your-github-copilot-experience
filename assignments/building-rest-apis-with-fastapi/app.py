# Starter Code for Building REST APIs with FastAPI

from fastapi import FastAPI

app = FastAPI(title="Item API")

# TODO: Create a sample list of items
# items = [
#     {"id": 1, "name": "Keyboard", "price": 49.99},
#     {"id": 2, "name": "Mouse", "price": 29.99},
# ]

# TODO: Create a GET endpoint that returns a welcome message or a list of items
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the API"}

# TODO: Create a POST endpoint to add an item
# @app.post("/items")
# def create_item(item: dict):
#     return {"message": "Item created", "item": item}

# TODO: Create a GET endpoint for a specific item by id
# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}

# TODO: Create a PUT endpoint to update an item
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: dict):
#     return {"message": "Item updated", "item_id": item_id, "item": item}

# TODO: Create a DELETE endpoint to remove an item
# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     return {"message": "Item deleted", "item_id": item_id}
