import falcon
from ..models import Form, FormField, Risk, User
from ..helpers import generate_formdata
import json
from collections import defaultdict
from ..models import session


@falcon.before(generate_formdata)
class riskSingle:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests for a single risk, by id"""

        response = {'data': '', 'success': True, 'error': None}

        try:
            risk_id = form["risk_id"]
        except Exception as e:
            raise falcon.HTTPMissingParam('risk_id')
        data = {}
        try:
            S = session()
            result = S.query(
                Risk.risk_type,
                Form.risk_id,
                FormField.field_id,
                FormField.field_label,
                FormField.field_type,
                FormField.mandatory
            ).join(
                Form,
                Risk.risk_id == Form.risk_id,
            ).join(
                FormField,
                Form.form_id == FormField.form_id
            ).filter(
                Form.risk_id == risk_id
            )

            data = defaultdict(lambda: defaultdict(dict))
            for i in result.all():
                risk_type = i[0]
                risk_id = i[1]
                field_id = i[2]
                field_label = i[3]
                field_type = i[4]
                mandatory = i[5]
                if not data.has_key(risk_type):
                    data[risk_type] = defaultdict(dict)
                if not data[risk_type]['fields'].has_key(field_label):
                    data[risk_type]['fields'][field_label] = {}
                data[risk_type]['risk_id'] = risk_id
                data[risk_type]['fields'][field_label]['field_id'] = field_id
                data[risk_type]['fields'][field_label]['field_type'] = field_type

        except Exception as e:
            response['error'] = str(e)
            response['success'] = False

        response['data'] = data
        S.close()
        resp.status = falcon.HTTP_200
        resp.content_type = "Application/json"
        resp.body = json.dumps(response)


@falcon.before(generate_formdata)
class riskAll:
    def on_get(self, req, resp, form={}, files={}):
        """Handles GET requests , returns all risks with related fields"""

        response = {'data': '', 'success': True, 'error': None}

        try:
            S = session()
            result = S.query(
                Risk.risk_type,
                Form.risk_id,
                FormField.field_id,
                FormField.field_label,
                FormField.field_type,
                FormField.mandatory
            ).join(
                Form,
                Risk.risk_id == Form.risk_id
            ).join(
                FormField,
                Form.form_id == FormField.form_id
            )
            print result.all()
            print 'here'

            data = defaultdict(lambda: defaultdict(dict))
            for i in result.all():
                risk_type = i[0]
                risk_id = i[1]
                field_id = i[2]
                field_label = i[3]
                field_type = i[4]
                mandatory = i[5]
                if not data.has_key(risk_type):
                    data[risk_type] = defaultdict(dict)
                if not data[risk_type]['fields'].has_key(field_label):
                    data[risk_type]['fields'][field_label] = {}
                data[risk_type]['risk_id'] = risk_id
                data[risk_type]['fields'][field_label]['field_id'] = field_id
                data[risk_type]['fields'][field_label]['field_type'] = field_type
            final_result = []
            for k, v in data.iteritems():
                final_result.append({'fields': v['fields'], 'risk': k})
        except Exception as e:
            response['error'] = str(e)
            response['success'] = False

        # serialize result to json
        response['data'] = final_result
        S.close()
        resp.content_type = "Application/json"
        resp.body = json.dumps(response)
