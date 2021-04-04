from flask import Flask, request, render_template, url_for, redirect
from forms import SpendingsForm
from models import spendings

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route('/spendings/', methods=["GET", "POST"])
def spendings_list():
    form = SpendingsForm()
    errors = []
    if request.method == "POST":
        if form.validate_on_submit():
            spendings.create(form.data)
            spendings.save_all()
        else:
            errors.append('Podaj "Wartość" jako liczbę, grosze oddziel kropką')
            redirect(url_for("spendings_list"))

    return render_template("spendings.html", form=form, spendings=spendings.all(), errors=errors)


@app.route('/spendings/<int:spending_id>/', methods=["GET", "POST"])
def update_spending(spending_id):
    spending = spendings.get(spending_id - 1)
    form = SpendingsForm(data=spending)
    errors = []

    if request.method == "POST":
        if form.validate_on_submit():
            spendings.update(spending_id - 1, form.data)
            spendings.save_all()
        return redirect(url_for("spendings_list"))
    return render_template("spending.html", form=form, spending_id=spending_id)


@app.route('/spendings/delete/<int:spending_id>/', methods=["GET"])
def delete_spending(spending_id):
    form = SpendingsForm()
    spendings.delete(spending_id - 1)
    spendings.save_all()

    return render_template("spendings.html", form=form, spendings=spendings.all())


if __name__ == "__main__":
    app.run(debug=True)
