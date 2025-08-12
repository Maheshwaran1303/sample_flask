from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here' 

@app.route('/')
def home():
    return render_template('home.html')

# for fruit in fruits_list:
#     print(fruit)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return """
            <h1>Contact Page of Myapp</h1>
            <p>For more details, please visit <a href="https://www.google.com">Google</a></p>
            <p>For more details, please visit <a href="https://www.google.com">Google</a></p>
    """

@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Welcome {name}</h1>"

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Form Submitted!"
    return "Please Submit the Form"

@app.route('/search')
def search():
    name = request.args.get('name', '')
    return f"Searching for {name}"

from flask import render_template

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        print(name)
    return render_template('form.html')

from flask import redirect, url_for, flash

from forms import LoginForm
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        flash(f'Login successful for {email}', 'success')
        return redirect(url_for('home'))
    
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    
    