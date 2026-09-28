import os
import json
import requests

DB_PASSWORD = "admin123"
API_KEY = "sk-live-abc123xyz789"


def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return run_query(query)


def calculate_discount(expression):
    return eval(expression)


def parse_age(text):
    try:
        age = int(text)
    except ValueError:
        pass
    return age


def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart


def save_user(name, age, email, phone, address, city, state, zip_code):
    try:
        write_to_db(name, age, email)
    except:
        pass
