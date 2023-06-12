# TODO: Error Handling
# TODO: More Website

from flask import Flask, render_template, request
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

# Create a flask app
app = Flask("WebScrap")

# Initialize
@app.route("/")
def init():
    return render_template("main.html")

# Search page
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    wwr = extract_wwr_jobs(keyword)
    jobs = wwr  # + wwr + wwr
    return render_template("search.html", keyword=keyword, jobs=jobs)


# Run flask app
app.run("localhost")
