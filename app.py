from flask import Flask, render_template, request

app = Flask(__name__)

class DrawingWebsite:
    def __init__(self):
        self.color = "black"
        self.brush_size = 5

    def set_color(self, color):
        self.color = color

    def set_brush_size(self, size):
        self.brush_size = int(size)

drawing_website = DrawingWebsite()

@app.route('/')
def index():
    return render_template('index.html', color=drawing_website.color, brush_size=drawing_website.brush_size)

@app.route('/set_color', methods=['POST'])
def set_color():
    color = request.form['color']
    drawing_website.set_color(color)
    return 'OK'

@app.route('/set_brush_size', methods=['POST'])
def set_brush_size():
    size = request.form['size']
    drawing_website.set_brush_size(size)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
