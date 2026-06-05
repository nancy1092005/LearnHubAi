from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/courses/python')
def python_course():
    return render_template('python_course.html')

@app.route('/courses/web')
def web_course():
    return render_template('web_course.html')

@app.route('/courses/ai')
def ai_course():
    return render_template('ai_course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        return render_template(
            'success.html',
            name=name,
            email=email,
            message=message
        )

    return render_template('contact.html')

@app.route('/recommend')
def recommend():

    interest = request.args.get('interest')

    if interest == "Programming":
        course = "Python Programming"
        book = "Python Crash Course"
        link = "https://www.youtube.com/@programmingwithmosh"

    elif interest == "Web Development":
        course = "Full Stack Web Development"
        book = "HTML &CSS by Jon Duckett"
        link = "https://www.youtube.com/@CodeWithHarry"

    else:
        course = "Artificial Intelligence"
        book = "Artificial Intelligence Basics"
        link = "https://www.youtube.com/@freecodecamp"

    return render_template(
        'recommendation.html',
        course=course,
        book=book,
        link=link
    )

if __name__ == '__main__':
    app.run(debug=True)