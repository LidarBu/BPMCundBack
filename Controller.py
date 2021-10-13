from flask import Flask, json, request, render_template
from flask_cors import cross_origin, CORS

from Scripts import LogBPM, StartBPM, StopBPM, PortBPM, StatusAll
from http import HTTPStatus

test = {"TEST_KEY": "TEST_VALUE"}

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'


@api.route('/gettest', methods=['GET'])
@cross_origin()
def get_test():
    json_res = {"data": [{"name": "BPM103", "port": 9009, "description": "from 1 to 3", "state": "WORKING"},
                         {"name": "BPM204", "port": 9009, "description": "from 2 to 4", "state": "NOT-WORKING"}],
                "error": None}
    return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}


@api.route('/getlogtest', methods=['GET'])
@cross_origin()
def get_log_test():
    bpm_num = request.args.get('bpm')
    json_res = {"data": [{"query": bpm_num + " loglog match more log 1", "level": "WARN"},
                         {"query": bpm_num + " loglog match more log 2", "level": "WARN"},
                         {"query": bpm_num + " loglog match more log 3", "level": "DEBUG"},
                         {"query": bpm_num + " loglog match more log 4", "level": "INFO"},
                         {"query": bpm_num + " loglog match more log 5", "level": "ERROR"}], "error": None}
    return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}


# ###################################end of thes###################################################################
@cross_origin()
@api.route('/getlog', methods=['GET'])
def get_log():
    bpm_num = request.args.get('bpm')
    if bpm_num is not None:
        try:
            out, err = LogBPM.exe(bpm_num)
            json_res = {"out": out, "error": err}
            print(json_res)
            return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
        except:
            json_res = {"out": "ERROR", "error": "Error occurred while executing script"}
            return json_res, HTTPStatus.INTERNAL_SERVER_ERROR, {'Content-Type': 'application/json'}
    else:
        json_res = {"data": "please provide bpm number"}
        return json_res, HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}


@cross_origin()
@api.route('/startbpm', methods=['PUT'])
def start_bpm():
    bpm_num = request.args.get('bpm')
    if bpm_num is not None:
        try:
            out, err = StartBPM.exe(bpm_num)
            json_res = {"out": out, "error": err}
            return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
        except:
            json_res = {"out": "ERROR", "error": "Error occurred while executing script"}
            return json_res, HTTPStatus.INTERNAL_SERVER_ERROR, {'Content-Type': 'application/json'}
    else:
        json_res = {"data": "please provide bpm number"}
        return json_res, HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}


@cross_origin()
@api.route('/stopbpm', methods=['PUT'])
def stop_bpm():
    bpm_num = request.args.get('bpm')
    if bpm_num is not None:
        try:
            out, err = StopBPM.exe(bpm_num)
            json_res = {"out": out, "error": err}
            return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
        except:
            json_res = {"out": "ERROR", "error": "Error occurred while executing script"}
            return json_res, HTTPStatus.INTERNAL_SERVER_ERROR, {'Content-Type': 'application/json'}
    else:
        json_res = {"data": "please provide bpm number"}
        return json_res, HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}


@cross_origin()
@api.route('/portbpm', methods=['GET'])
def port_bpm():
    bpm_num = request.args.get('bpm')
    if bpm_num is not None:
        try:
            out, err = PortBPM.exe(bpm_num)
            json_res = {"out": out, "error": err}
            return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
        except:
            json_res = {"out": "ERROR", "error": "Error occurred while executing script"}
            return json_res, HTTPStatus.INTERNAL_SERVER_ERROR, {'Content-Type': 'application/json'}
    else:
        json_res = {"out": "please provide bpm number", "error": "please provide bpm number"}
        return json_res, HTTPStatus.BAD_REQUEST, {'Content-Type': 'application/json'}


@cross_origin()
@api.route('/statusall', methods=['GET'])
def status_all_bpm():
    out, err = StatusAll.exe()
    json_res = {"out": out, "error": err}
    return json_res, HTTPStatus.OK, {'Content-Type': 'application/json'}
