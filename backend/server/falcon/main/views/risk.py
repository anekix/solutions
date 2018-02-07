import falcon
from ..models import S
from ..models import Form, FormFieldMap, Field, Risk, FieldType
from ..helpers import generate_formdata
import json
from collections import defaultdict


@falcon.before(generate_formdata)
class riskSingle:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests for a single risk, by id"""
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

        res['res'] = result
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(res)


@falcon.before(generate_formdata)
class riskAll:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests , returns all risks with related fields"""

        result = S.query(
            Risk.risk_type,
            Form.risk_id,
            Form.form_id,
            FormFieldMap.field_id,
            Field.field_name,
            Field.field_id,
            FieldType.type_name,
        ).select_from(Risk)\
            .join(
                Form,
                Risk.risk_id == Form.risk_id
        ).join(
                FormFieldMap,
                Form.form_id == FormFieldMap.form_id
        ).join(
                Field,
                FormFieldMap.field_id == Field.field_id
        ).join(
                FieldType,
                Field.type_id == FieldType.type_id
        )

        data = defaultdict(lambda: defaultdict(dict))

        for i in result.all():
            risk_name = i[0]
            risk_id = i[1]
            form_id = i[2]
            field_id = i[3]
            field_name = i[4]
            field_id = i[5]
            field_type = i[6]

            if not data.has_key(risk_name):
                data[risk_name] = defaultdict(dict)
            if not data[risk_name]['fields'].has_key(field_name):
                data[risk_name]['fields'][field_name] = {}
            data[risk_name]['risk_id'] = risk_id
            data[risk_name]['fields'][field_name]['field_id'] = field_id
            data[risk_name]['fields'][field_name]['field_type'] = field_type
        resp.body = json.dumps(data)

