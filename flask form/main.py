from flask import Flask, render_template, redirect, session, flash, url_for
from forms.NameForm import NameForm
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="templates")
Bootstrap(app)


app.config["SECRET_KEY"] = "ey12929292"

@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        nameForm = form.name.data
        nameOld = session.get("name", "")

        if nameOld is not None and nameOld != nameForm:
            flash("haz cambiado el nombre del usuario")

        session["name"] = nameForm
        return redirect(url_for("index"))

    return render_template('index.html', form=form, name=session.get("name", ""))


