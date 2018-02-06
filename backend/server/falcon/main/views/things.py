import falcon
from ..models import S
from ..models import Form, FormFieldMap, Field
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
        res = {'res': ''}
        result = S.query(Field.field_name).select_from(Form).join(
            FormFieldMap,
            Form.form_id == FormFieldMap.form_id
            ).join(
                Field, 
                FormFieldMap.field_id == Field.field_id
            ).filter(
                Form.risk_id == 1
            ).all()
        # result = select([
        #     Form.c.risk_id,
        #     FormFieldMap.c.field_id
        #     ]).select_from(
        #         Form.join(
        #             FormFieldMap,
        #             Form.c.form_id == FormFieldMap.c.form_id
        #         )
        #     )

        print result,"==="
        for i in result:
            print i
        # result = S.query(Risk).filter(Risk.risk_id == int(risk_id)).one()
        # risk_id = result.risk_id

        # # find fields associated with this risk
        # if risk_id:
        #     fields = []
        #     risk_fields = S.query(RiskData).filter(RiskData.riskId == risk_id)
        #     for i in risk_fields:
        #         print i.fields
        #         fields.append(i.fields)

        # res = dict(
        #         risk=result.as_dict(),
        #         fields=fields
        #     )
        res['res']=result
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)


@falcon.before(generate_formdata)
class riskAll:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests"""

        # result = S.query(Risk).all()
        res = {
            "Car":{
                    "risk_id": 1,
                    "fields": [
                        {
                            'field_id': 1,
                            'field_type': "NUMBER",
                            "field_name": "Age"
                        },
                        {
                            'field_id': 2,
                            'field_type': "TEXT",
                            "field_name": "Name"
                        },
                        {
                            'field_id': 1,
                            'field_type': "TEXT",
                            "field_name": "Address"
                        }
                    ]
                },
            "House": {
                "risk_id": 2,
                "fields": [
                    {
                        'field_id': 1,
                        'field_type': "NUMBER",
                        "field_name": "Country"
                    },
                    {
                        'field_id': 2,
                        'field_type': "TEXT",
                        "field_name": "Name"
                    },
                    {
                        'field_id': 1,
                        'field_type': "TEXT",
                        "field_name": "Contact"
                    }
                ]
            }
        }

        
        # for i in result:
        #     fields = []
        #     risk_fields = S.query(RiskData).filter(RiskData.riskId == i.risk_id)
        #     for j in risk_fields:
        #         fields.append(j.fields)
        #     print fields
        #     res.append(
        #         dict(
        #             risk=i.as_dict(),
        #             fields=fields
        #         )
        #     )
        # resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)

