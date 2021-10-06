from flask import Flask, json, request, render_template
from Scripts import LogBPM, StartBPM
from http import HTTPStatus

test = {"TEST_KEY": "TEST_VALUE"}

api = Flask(__name__)


@api.route('/getlog', methods=['GET'])
def get_log():
    bpm_num = request.args.get('bpm')
    if bpm_num is not None:
        out, err = LogBPM.exe(bpm_num)
        json_res = {"out": out, "error": err}
        print(json_res)
        return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
    else:
        json_res = {"data": "please provide bpm number"}
        return json_res, HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}


@api.route('/startbpm', methods=['GET'])
def start_bpm():
    bpm_num = request.args.get('bpm')
    if bpm_num is not None:
        out, err = StartBPM.exe(bpm_num)
        json_res = {"out": out, "error": err}
        return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
    else:
        json_res = {"data": "please provide bpm number"}
        return json_res, HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}
