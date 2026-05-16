from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Sahana"

    tasks = [
        "Learn Flask",
        "Understand Jinja2",
        "Build Templates"
    ]

    return render_template(
        'index.html',
        username=name,
        task_list=tasks
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)