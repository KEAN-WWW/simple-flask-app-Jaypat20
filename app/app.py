from flask import Flask, render_template

app = Flask(__name__)

# 2. Default route
@app.route('/')
def home():
    return "Hello CPS3500!"

# 3. New route /new_page
@app.route('/new_page')
def new_page():
    return "This is a New Page!"

# 6. Dynamic route with render_template
@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

