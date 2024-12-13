from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from database import db_init, db, User, Property
from ai_recommendation import recommend_properties

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/real_estate_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db_init(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('properties'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/properties')
def properties():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    properties = Property.query.all()
    return render_template('property_listings.html', properties=properties)

@app.route('/api/properties', methods=['GET'])
def api_properties():
    properties = Property.query.all()
    return jsonify([prop.to_dict() for prop in properties])

@app.route('/recommendations', methods=['POST'])
def recommendations():
    if 'user_id' not in session:
        return "Unauthorized", 401
    user_data = request.json
    recommendations = recommend_properties(user_data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
