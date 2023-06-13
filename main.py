# TODO: Check the errors
# TODO: More Website

from flask import Flask, render_template, request, redirect, send_file
from datetime import datetime
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

# Create a flask app
app = Flask("WebScrap")

# Cache
data = {}

# Initialize
@app.route("/")
def init():
    return render_template("main.html")

# Search page
@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    # Unusual access
    if keyword == None:
        return redirect("/")

    # Check the cache
    if keyword in data:
        jobs = data[keyword]
    else:
        wwr = extract_wwr_jobs(keyword)
        jobs = wwr  # + wwr + wwr
        data[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)

# Export page
@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    # Without keyword
    if keyword == None:
        return redirect("/")

    # Not exist keyword data
    if keyword not in data:
        return redirect(f"search?keyword={keyword}")

    # File export
    time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_to_file(keyword, data[keyword])

    return send_file(f"{keyword}_{time_str}.csv", as_attachment=True)

# Run flask app
app.run("localhost")
