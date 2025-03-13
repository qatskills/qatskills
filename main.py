from flask import Flask, render_template, send_file
import nbformat
import nbconvert

app = Flask(__name__)

# Route: Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route: Blog Posts
@app.route("/post/<post_name>")
def blog_post(post_name):
    return render_template(f"posts/{post_name}.html")

# Route: Render Jupyter Notebooks as HTML
@app.route("/notebook/<notebook_name>")
def show_notebook(notebook_name):
    notebook_path = f"notebooks/{notebook_name}.ipynb"
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)

    html_exporter = nbconvert.HTMLExporter()
    html_body, _ = html_exporter.from_notebook_node(notebook)

    return f"<html><body>{html_body}</body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


#from flask import Flask

#app = Flask(__name__)


#@app.route('/')
#def index():
#    return 'Hello from Flask!'

#if __name__ == '__main__':
#  app.run(host='0.0.0.0', port=5000)
