from main import app
from .risk import *

risk_single = riskSingle()
risk_all = riskAll()

app.add_route('/api/v1/risk', risk_single)
app.add_route('/api/v1/risk-all', risk_all)
