from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template)

# from snakeeyes.blueprints.contact.forms import ContactForm

feedback = Blueprint('feedback', __name__, template_folder='templates')


@feedback.route('/feedback', methods=['GET', 'POST'])
def index():
    pass
