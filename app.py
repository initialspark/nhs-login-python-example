from util import get_env_variable

from flask import *
from flask_session import Session

from oidc_client import OIDCClient

NHS_LOGIN_AUTHORITY_URL = get_env_variable('NHS_LOGIN_AUTHORITY_URL')
NHS_LOGIN_CLIENT_ID = get_env_variable('NHS_LOGIN_CLIENT_ID')
NHS_LOGIN_CALLBACK_URL = get_env_variable('NHS_LOGIN_CALLBACK_URL')
NHS_LOGIN_SCOPES = get_env_variable('NHS_LOGIN_SCOPES')

oidc_client = OIDCClient(NHS_LOGIN_CLIENT_ID,
                         NHS_LOGIN_AUTHORITY_URL,
                         NHS_LOGIN_SCOPES,
                         NHS_LOGIN_CALLBACK_URL)

app = Flask(__name__)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def index():
    auth_url = oidc_client.get_authorization_url()
    return render_template('index.jinja', authorize_url=auth_url)


@app.route('/oidc-callback')
def auth_callback():
    auth_resp = oidc_client.get_authorization_response(request.args)
    session['token_request'] = oidc_client.get_access_token(auth_resp)
    return redirect(url_for('user_details'))


@app.route('/user-details')
def user_details():
    access_token = session['token_request']['access_token']
    user_info = oidc_client.get_userinfo(access_token)
    return render_template('user_details.jinja', user_info=user_info)
