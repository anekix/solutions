from werkzeug.serving import run_simple
from main import app
run_simple('localhost', 9070, app, use_reloader=True)
