import os
import smtplib
from flask import *
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
import secrets

my_email = "your_email"
my_password = "your_password"
client_id = "the_client_id"
client_secret = "the_client_secret"
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pages.db"
app.config["TRACK_MODIFICATIONS"] = False
ckeditor = CKEditor(app)
db = SQLAlchemy(app)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    vid_path = db.Column(db.String(100))
    git_link = db.Column(db.String(500))
    modules = db.Column(db.String(500))
    other_link = db.Column(db.String(500))
    desc = db.Column(db.String(2000))


# with app.app_context():
#     db.create_all()

class CreateMail(FlaskForm):
    name = StringField("Name")
    email = StringField("Email", validators=[DataRequired()])
    body = CKEditorField('Message', validators=[DataRequired()])
    submit = SubmitField("Send")


@app.route('/', methods=['GET', 'POST'])
def home():
    sent = ""
    form = CreateMail()
    if form.validate_on_submit():
        print(form.name.data, form.email.data, form.body.data)
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Website visitor\n\nFrom {form.name.data}\n{form.email.data}\n{form.body.data}")
        connection.close()
        sent = "Message sent"
    return render_template('index.html', form=form, sent=sent)

@app.route('/code')
def page():
    id = request.args.get('id')
    page = db.session.query(Page).get(id)
    return render_template('code.html', page=page)




if __name__ == '__main__':
    app.run(debug=True)