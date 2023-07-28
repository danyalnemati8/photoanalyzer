from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key for security

# Dummy data for demonstration purposes
dummy_photos = [
    {
        'url': 'https://dummyurl.com/photo1.jpg',
        'analysis': {
            'objects': ['cat', 'tree'],
            'colors': ['blue', 'green'],
            'sentiment': 'positive',
        },
    },
    {
        'url': 'https://dummyurl.com/photo2.jpg',
        'analysis': {
            'objects': ['dog', 'car'],
            'colors': ['red', 'yellow'],
            'sentiment': 'negative',
        },
    },
    # Add more dummy photos here...
]

@app.route('/')
def index():
    if 'access_token' not in session:
        return redirect(url_for('login'))
    return render_template('homepage.html', photos=dummy_photos)

@app.route('/login')
def login():
    # In a real app, you would implement Facebook Login here
    # For this example, we'll just set a dummy access token
    session['access_token'] = 'dummy_access_token'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # Clear the access token and log out the user
    session.pop('access_token', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
