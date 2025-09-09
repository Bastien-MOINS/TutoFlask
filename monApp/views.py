from .app import app

@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()

@app.route('/about')
def about():
    return app.config['ABOUT']

@app.route('/contact')
def contact():
    return app.config['CONTACT']