from flask import Flask, render_template, request
from color_analysis import analyze_colors

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        colors = analyze_colors(image)
        return render_template('index.html', colors=colors)
    return render_template('index.html', colors=None)


if __name__ == '__main__':
    app.run(debug=True)
