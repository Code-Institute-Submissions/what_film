import os
from flask import Flask, render_template, flash, redirect, request, session, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["MONGO_DBNAME"] = 'whatFilmDB'
app.config["MONGO_URI"] = 'mongodb+srv://lewejuice:Leahlh1994@myfirstcluster.ztxrz.mongodb.net/whatFilmDB?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():   
    #checks if username is in session and renders the home page
    if 'username' in session:
        user = 'username' 
    return render_template("index.html")

@app.route('/login_button')
def login_button():  
    #Login button takes you to login.html
    return render_template("login.html")  

@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
    logged_user = users.find_one({"username": request.form["username"]})
    if logged_user:
        #checks if username matches one in database
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), logged_user['password']) == logged_user['password']:
            session["username"] = request.form["username"]
            flash("Welcome back " + session["username"])
            return redirect(url_for("home"))
    # if username is'nt recognised
    flash("Invalid Username/Password")
    return redirect(url_for("login_button"))

@app.route('/logout')
def logout():
    #clears cookies to logout user
    session.clear()
    flash("You are logged out")
    return redirect(url_for("home"))

@app.route('/account', methods=['POST', 'GET'])
def account():   
    if 'username' in session:
        #checks if username is in session and then renders the information for that user
        user = mongo.db.users
        active_user = user.find({"username": session['username']})
        return render_template("account.html", account = active_user)
    return render_template("login.html")

@app.route('/delete_account', methods=['POST', 'GET'])
def delete_account():
    users = mongo.db.users
    reviews = mongo.db.reviews
    logged_user = users.find_one({"username": session['username']})
    if bcrypt.hashpw(request.form['old_password'].encode('utf-8'), logged_user['password']) == logged_user['password']:
        #if the password matches the stored password it will delete the user and their reviews
        myquery = { "username": session['username'] }
        users.delete_one(myquery)
        reviews.delete_many(myquery)
        session.clear()
        flash("Account Deleted")
        return redirect(url_for("home"))
    #if password is incorrect it flashes message incorrect password    
    flash("Incorrect Password")
    return redirect(url_for("account"))


@app.route('/update_account', methods=['POST', 'GET'])
def update_account():
    users = mongo.db.users
    logged_user = users.find_one({"username": session['username']})
    #if the form password matches to stored database password
    if bcrypt.hashpw(request.form['old_password'].encode('utf-8'), logged_user['password']) == logged_user['password']:
        hashpass = bcrypt.hashpw(request.form["new_password"].encode("utf-8"), bcrypt.gensalt())
        oldhashpass = bcrypt.hashpw(request.form["old_password"].encode("utf-8"), bcrypt.gensalt())
        #if a new username, email and password has been given, it updates them all
        if len(request.form["new_username"]) >= 1 and len(request.form["new_email"]) >= 1 and len(request.form["new_password"]) >= 1:
            users.update({'username': session['username']},
            {
                'username': request.form.get('new_username'),
                'email': request.form.get('new_email'),
                'password': hashpass
            })
            session.clear()
            flash("Your account details have been updated")
            return redirect(url_for("logout"))
        #if a new username and email has been given, but password has not, it updates them all but the password   
        if len(request.form["new_username"]) >= 1 and len(request.form["new_email"]) >= 1 and len(request.form["new_password"]) < 1:
            users.update({'username': session['username']},
            {
                'username': request.form.get('new_username'),
                'email': request.form.get('new_email'),
                'password': oldhashpass
            })
            session.clear()
            flash("Your account details have been updated")
            return redirect(url_for("logout"))
        #if a new username and password has been given, but email has not, it updates them all but the email   
        if len(request.form["new_username"]) >= 1 and len(request.form["new_email"]) < 1 and len(request.form["new_password"]) >= 1:
            users.update({'username': session['username']},
            {
                'username': request.form.get('new_username'),
                'email': request.form.get('old_email'),
                'password': hashpass
            })
            session.clear()
            flash("Your account details have been updated")
            return redirect(url_for("login"))
        #if a new password and email has been given, but username has not, it updates them all but the username    
        if len(request.form["new_username"]) < 1 and len(request.form["new_email"]) >= 1 and len(request.form["new_password"]) >= 1:
            users.update({'username': session['username']},
            {
                'username': session['username'],
                'email': request.form.get('new_email'),
                'password': hashpass
            }) 
            flash("Your account details have been updated")
            return redirect(url_for("account"))
        #if only a new username is given, only that will be updated    
        if len(request.form["new_username"]) >= 1 and len(request.form["new_email"]) < 1 and len(request.form["new_password"]) < 1:
            users.update({'username': session['username']}, 
            {
                'username': request.form.get('new_username'),
                'email': request.form.get('old_email'),
                'password': oldhashpass
            })
            session.clear()
            flash("Your account details have been updated")
            return redirect(url_for("logout"))
        #if only a new email is given, only that will be updated    
        if len(request.form["new_username"]) < 1 and len(request.form["new_email"]) >= 1 and len(request.form["new_password"]) < 1:
            users.update({'username': session['username']}, 
            {
                'username': session['username'],
                'email': request.form.get('new_email'),
                'password': oldhashpass
            })  
            flash("Your account details have been updated")
            return redirect(url_for("account"))
        #if only a new password is given, only that will be updated    
        if len(request.form["new_username"]) < 1 and len(request.form["new_email"]) < 1 and len(request.form["new_password"]) >= 1:
            users.update({'username': session['username']}, 
            {
                'username': session['username'],
                'email': request.form.get('old_email'),
                'password': hashpass
            })
            flash("Your account details have been updated")
            return redirect(url_for("account"))
    #if password was not entered correctly, it will flash message incorrect password        
    flash("Incorrect Password")
    return redirect(url_for("account"))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({"username": request.form["username"]})
        #if no username is found that matches the username typed in
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form["password"].encode("utf-8"), bcrypt.gensalt())
            session["username"] = request.form["username"]
            existing_email = users.find_one({"email" : request.form["u_email"]})
            #if no email matches the one given
            if existing_email is None:
                users.insert({"username" : request.form["username"], "password" : hashpass, "email" : request.form["u_email"]})
                session["email"] = request.form["u_email"]
                flash("Welcome " + session["username"])
                return redirect(url_for("home"))
            #if email is already in use, flashes message "That email already exists!"
            flash("That email already exists!")
            return render_template("register.html")
        #if username is already in use, flashes message "That username already exists!"
        flash("That username already exists!")
        return render_template("register.html")

    return render_template("register.html")

@app.route('/movie/<id>')
def movie_page(id):
    review_db = mongo.db.reviews
    #takes the id from url which is given from Javascript
    review_id = review_db.find({"movie_id": id})
    total = 0
    #if there is a review stored in the database matching the same movie id, get all ratings and reviews 
    for reviews in review_id:
        ratings = reviews["rating"]
        one_review = reviews["review"]
        total += int(ratings)
    #if there are none matching that movie id, it will show no rating and no review    
    if total == 0:
        av_rating = "No Rating"
        one_review = ""
    #if there is one or more found it averages the ratings and rounds it to one decimal place
    else:
        average = total / review_id.count()
        av_rating = str(round(average, 2))
        one_review = one_review
    #passes the variable to jinja function in html to for loop the reviews    
    review_by_id = review_db.find({"movie_id": id})
    return render_template("test.html", id=id, review_by_id=review_by_id, one_review=one_review, av_rating=av_rating)

@app.route('/review', methods=['POST', 'GET'])
def review():
    reviews_db = mongo.db.reviews
    #checks if user is logged in
    if 'username' in session:
        user = session['username']
        #checks if the review is there and then inserts the review, rating, username and movie id to the database
        if len(request.form["review"]) and len(request.form["rating"]) >= 1:
            reviews_db.insert({
                "username": user,
                "movie_id": request.form["id"],
                "review": request.form["review"],
                "rating": request.form["rating"]
            })
            #tells the user their review has been posted
            flash("Your review has been posted!")
            return redirect(url_for("home"))
        #No text found in review so user is notified    
        flash("Form error! Please write the review and select a rating")
        return redirect(url_for('home'))
    #user is taken to login screen if not logged in    
    flash("Please login to write a review")
    return render_template("login.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)