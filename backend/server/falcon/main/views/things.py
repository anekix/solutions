import falcon
from ..models import S
from ..models import Risk, RiskData
from ..helpers import generate_formdata
import json


@falcon.before(generate_formdata)
class riskSingle:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests"""
        try:
            risk_id = form["risk_id"]
        except Exception as e:
            raise falcon.HTTPMissingParam(
                'risk_id'
            )
        result = S.query(Risk).filter(Risk.risk_id == int(risk_id)).one()
        risk_id = result.risk_id

        # find fields associated with this risk
        if risk_id:
            fields = []
            risk_fields = S.query(RiskData).filter(RiskData.riskId == risk_id)
            for i in risk_fields:
                print i.fields
                fields.append(i.fields)

        res = dict(
                risk=result.as_dict(),
                fields=fields
            )
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)


@falcon.before(generate_formdata)
class riskAll:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests"""

        result = S.query(Risk).all()
        res = []
        for i in result:
            fields = []
            risk_fields = S.query(RiskData).filter(RiskData.riskId == i.risk_id)
            for j in risk_fields:
                fields.append(j.fields)
            print fields
            res.append(
                dict(
                    risk=i.as_dict(),
                    fields=fields
                )
            )
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)

