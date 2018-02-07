from main import app
from .things import *

rs = riskSingle()
rsAll = riskAll()

app.add_route('/api/v1/risk', rs)
app.add_route('/api/v1/risk-all', rsAll)
