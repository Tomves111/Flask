from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User


@app.route('/', methods=['GET'])
def entry():
    """Endpoint to create a user."""
    new_user = User(username='myuser',
                    email='myuser@example.com',
                    created=dt.now(),
                    bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                    admin=False
                    )
    db.session.add(new_user)
    db.session.commit()
    return make_response("User created!")