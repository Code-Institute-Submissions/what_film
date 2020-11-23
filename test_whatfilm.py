import os
import unittest
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

# Run Tests

if __name__ == '__main__':
    unittest.main()