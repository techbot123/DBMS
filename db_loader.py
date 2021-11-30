import time
from flask import Flask
# print('at start')
from mongo_connector import mongo_connector
# print('ok')
from reg_form import run_web, emp_db

employee_db = {}
# app = Flask(__name__)

# def load_new_post_to_db(post):

# print('Run Web App..')
# run_web()
# print('time to sleep')
# time.sleep(5)
# print('Done Sleeping')
# employee_db.update(emp_db)
# print(f'printing employee db {employee_db}')
if __name__ == '__main__':

	# print('Initialize MongoDB...')
	# mongo_connector()
	# print('Initialization Successuful!')
	run_web()
	while True:
		employee_db.update(emp_db)
		print(f'printing emp db at {time.time()} and emp info {employee_db}')
		time.sleep(5)






