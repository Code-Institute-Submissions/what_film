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
    session.clear()
    flash("You are logged out")
    return redirect(url_for("home"))

@app.route('/account', methods=['POST', 'GET'])
def account():   
    if 'username' in session:
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
        myquery = { "username": session['username'] }
        users.delete_one(myquery)
        reviews.delete_many(myquery)
        session.clear()
        flash("Account Deleted")
        return redirect(url_for("home"))
    flash("Incorrect Password")
    return redirect(url_for("account"))


@app.route('/update_account', methods=['POST', 'GET'])
def update_account():
    users = mongo.db.users
    logged_user = users.find_one({"username": session['username']})
    if bcrypt.hashpw(request.form['old_password'].encode('utf-8'), logged_user['password']) == logged_user['password']:
        hashpass = bcrypt.hashpw(request.form["new_password"].encode("utf-8"), bcrypt.gensalt())
        oldhashpass = bcrypt.hashpw(request.form["old_password"].encode("utf-8"), bcrypt.gensalt())
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
        if len(request.form["new_username"]) < 1 and len(request.form["new_email"]) >= 1 and len(request.form["new_password"]) >= 1:
            users.update({'username': session['username']},
            {
                'username': session['username'],
                'email': request.form.get('new_email'),
                'password': hashpass
            }) 
            flash("Your account details have been updated")
            return redirect(url_for("account"))
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
        if len(request.form["new_username"]) < 1 and len(request.form["new_email"]) >= 1 and len(request.form["new_password"]) < 1:
            users.update({'username': session['username']}, 
            {
                'username': session['username'],
                'email': request.form.get('new_email'),
                'password': oldhashpass
            })  
            flash("Your account details have been updated")
            return redirect(url_for("account"))
        if len(request.form["new_username"]) < 1 and len(request.form["new_email"]) < 1 and len(request.form["new_password"]) >= 1:
            users.update({'username': session['username']}, 
            {
                'username': session['username'],
                'email': request.form.get('old_email'),
                'password': hashpass
            })
            flash("Your account details have been updated")
            return redirect(url_for("account"))
    flash("Incorrect Password")
    return redirect(url_for("account"))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({"username": request.form["username"]})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form["password"].encode("utf-8"), bcrypt.gensalt())
            session["username"] = request.form["username"]
            existing_email = users.find_one({"email" : request.form["u_email"]})

            if existing_email is None:
                users.insert({"username" : request.form["username"], "password" : hashpass, "email" : request.form["u_email"]})
                session["email"] = request.form["u_email"]
                flash("Welcome " + session["username"])
                return redirect(url_for("home"))
            flash("That email already exists!")
            return render_template("register.html")
        flash("That username already exists!")
        return render_template("register.html")

    return render_template("register.html")

@app.route('/movie/<id>')
def movie_page(id):
    review_db = mongo.db.reviews
    review_id = review_db.find({"movie_id": id})
    total = 0
    for reviews in review_id:
        ratings = reviews["rating"]
        one_review = reviews["review"]
        total += int(ratings)
    if total == 0:
        av_rating = "No Rating"
        one_review = ""
    else:
        average = total / review_id.count()
        av_rating = str(round(average, 2))
        one_review = one_review
    review_by_id = review_db.find({"movie_id": id})
    return render_template("test.html", id=id, review_by_id=review_by_id, one_review=one_review, av_rating=av_rating)

@app.route('/review', methods=['POST', 'GET'])
def review():
    reviews_db = mongo.db.reviews
    if 'username' in session:
        user = session['username']
        if len(request.form["review"]) and len(request.form["rating"]) >= 1:
            reviews_db.insert({
                "username": user,
                "movie_id": request.form["id"],
                "review": request.form["review"],
                "rating": request.form["rating"]
            })
            flash("Your review has been posted!")
            return redirect(url_for("home"))
        flash("Form error! Please write the review and select a rating")
        return redirect(url_for('home'))
    flash("Please login to write a review")
    return render_template("login.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)