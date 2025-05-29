# import json
# from flask import Flask, jsonify, request
# app = Flask(__name__)
#
# foods = [
#  { 'id': 1, 'name': 'BBQ' },
#  { 'id': 2, 'name': 'chicken' },
#  { 'id': 3, 'name': 'banana' }
# ]
#
#
# nextFoodId = 4
#
# @app.route('/foods', methods=['GET'])
# def get_foods():
#  return jsonify(foods)
#
# @app.route('/foods/<int:id>', methods=['GET'])
# def get_food_by_id(id: int):
#  food = get_food(id)
#  if food is None:
#    return jsonify({ 'error': 'food does not exist'}), 404
#  return jsonify(food)
#
# def get_food(id):
#  return next((f for f in foods if f['id'] == id), None)
#
# def food_is_valid(food):
#  for key in food.keys():
#    if key != 'name':
#     return False
#  return True
#
# @app.route('/foods', methods=['POST'])
# def create_food():
#     global nextFoodId
#     food = request.get_json()  # <-- fix here
#     if not food_is_valid(food):
#         return jsonify({ 'error': 'Invalid food properties.' }), 400
#
#     food['id'] = nextFoodId
#     nextFoodId += 1
#     foods.append(food)
#
#     return '', 201, { 'location': f'/foods/{food["id"]}' }
#
# @app.route('/foods/<int:id>', methods=['PUT'])
# def update_food(id: int):
#     food = get_food(id)
#     if food is None:
#         return jsonify({ 'error': 'food does not exist.' }), 404
#
#     updated_food = request.get_json()  # <-- fix here
#     if not food_is_valid(updated_food):
#         return jsonify({ 'error': 'Invalid food properties.' }), 400
#
#     food.update(updated_food)
#     return jsonify(food)
#
#
# @app.route('/foods/<int:id>', methods=['DELETE'])
# def delete_food(id: int):
#  global foods
#  food = get_food(id)
#  if food is None:
#    return jsonify({ 'error': 'food does not exist.' }), 404
#
# #  foods = [f for f in foods if f['id'] != id]
# #  return jsonify(foods), 200
# #
# # if __name__ == '__main__':
# #    app.run(port=5000)
#
#
# # import httplib
# from pydrive.drive import GoogleDrive
# from pydrive.auth import GoogleAuth
#
# import os
#
# guath = GoogleAuth()
# guath.LocalWebserverAuth()
# drive = GoogleDrive(guath)
#
# path = "/Users/kareenaarora/Desktop/testing123"
#
# for x in os.listdir(path):
#     f = drive.CreateFile({'title': x})
#     f.SetContentFile(os.path.join(path, x))
#     f.Upload()
#
#
# from cryptography.fernet import Fernet
# def write_key():
#     """
#     Generates a key and save it into a file
#     """
#     key = Fernet.generate_key()
#     with open('key.txt', 'wb') as f:
#         f.write(key)
#
# def load_key():
#     with open('key.txt', 'rb') as f:
#         key = f.read()
#         return key
#
# def encrypt(filename, key):
#     f = Fernet(key)
#     with open(filename, 'rb') as og_file:
#         data = og_file.read()
#         encrypted = f.encrypt(data)
#     with open(filename, 'wb') as encrypted_file:
#         encrypted_file.write(encrypted)
#
# def decrypt(filename, key):
#     f = Fernet(key)
#     with open(filename, 'rb') as encrypted_file:
#         encrypted = encrypted_file.read()
#         decrypted = f.decrypt(encrypted)
#     with open(filename, 'wb') as decrypted_file:
#         decrypted_file.write(decrypted)
#
# if __name__ == '__main__':
#     file = "/Users/kareenaarora/Desktop/test.pdf"
# #     decrypt(file, load_key())
#
# import PyPDF2, getpass
# from colorama import Fore, init
#
# init()
#
# def lock_file(input_file, password):
#     with open(input_file, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#         pdf_writer = PyPDF2.PdfWriter()
#         for page_num in range(len(pdf_reader.pages)):
#                 pdf_writer.add_page(pdf_reader.pages[page_num])
#         pdf_writer.encrypt(password)
#         with open(input_file, 'wb') as file:
#             pdf_writer.write(file)
#
# input_pdf = input("enter the path to the pdf file: ")
# password = getpass.getpass("enter the password to lock the file: ")
# lock_file(input_pdf, password)
# print("pdf has been locked")
#
# import concurrent.futures
# import requests
# import time
# import csv
#
# def fetch_url(url):
#     time.sleep(2)
#     answer_of_call = requests.get(url)
#     return answer_of_call.text
#
# urls = ['https://api.github.com/',
# 'https://api.ipify.org?format=json']
#
# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     futures = [executor.submit(fetch_url, url) for url in urls]
#     with open('api.csv', 'w', newline="") as f:
#             writer = csv.writer(f)
#             for future in concurrent.futures.as_completed(futures):
#                 writer.writerow(future.result())
#
# print(f"new file has been created!")
