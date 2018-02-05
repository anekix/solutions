from main import app
from .things import *

rs = riskSingle()
rsAll = riskAll()

app.add_route('/risk', rs)
app.add_route('/risk-all', rsAll)
