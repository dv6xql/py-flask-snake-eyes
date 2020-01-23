from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template)

from snakeeyes.blueprints.feedback.forms import FeedbackForm

feedback = Blueprint('feedback', __name__, template_folder='templates')


@feedback.route('/feedback', methods=['GET', 'POST'])
def index():
    form = FeedbackForm()

    return render_template('feedback/index.html', form=form)
