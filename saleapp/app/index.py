from flask import render_template
import dao
from saleapp.app import app


@app.route("/")
def index():
    cates = dao.load_catigories()
    prods = dao.load_products()
    return render_template("index.html", catigories = cates, products = prods)


if __name__ == '__main__':
    app.run(debug=True)
