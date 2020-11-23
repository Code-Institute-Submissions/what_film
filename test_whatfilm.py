import os
import unittest
import bcrypt
from app import app
from decouple import config
from flask_pymongo import PyMongo
from flask import Flask, render_template, flash, redirect, session, url_for, request

# Connect to external MongoDB database through URI variable hosted on app server

app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = config('SECRET_KEY')

mongo = PyMongo(app)

# Variables
users = mongo.db.users

# Testing App Routes
class testingApp(unittest.TestCase):
    
    def setUp(self):
        self.mongo = app.test_client()

    def test_routes(self):
        #Test Homepage
        page = self.mongo.get('/home')
        self.assertEqual(page.status_code, 200)
        
        #Test Login Page
        page = self.mongo.get('/login_button')
        self.assertEqual(page.status_code, 200)

        #Test Account Page
        page = self.mongo.get('/account')
        self.assertEqual(page.status_code, 200)

        #Test Register Page
        page = self.mongo.get('/register')
        self.assertEqual(page.status_code, 200)

        #Test Movie Page
        page = self.mongo.get('/movie/278')
        self.assertEqual(page.status_code, 200)

        print('All the tests passed')

# Testing Registering a User and Removing

    def test_successful_registration(self):
        response = self.mongo.post('/register', data=dict(username='testuser', password='password', email='test@email.com'), follow_redirects=True)
        data = response.data.decode('utf-8')
        print(data)
        find_user = users.find_one({'username': 'testuser'})
        self.assertIsNotNone(find_user)
        print('User Found. Preparing for Deletion')
        delete_user = users.remove({'username': 'testuser'})
        self.assertEqual(delete_user.status_code, 200)
        print('User Deleted.')

# Testing Deleting a User

    def test_deleting_user(self):
        response = self.mongo.post('/delete_account/test')
        user = users.find_one({'username': 'test'})
        self.assertIsNone(user)
        
        print('User Deleted')

# Tidy Up after test
    
    def tearDown(self):
        sign_out = self.mongo.get('/logout')

# Run Tests

if __name__ == '__main__':
    unittest.main()