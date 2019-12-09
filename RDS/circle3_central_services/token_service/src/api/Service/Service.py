from flask import jsonify, request, Response
import Util, json

from lib.Service import Service, OAuth2Service
from lib.Exceptions.ServiceExceptions import ServiceExistsAlreadyError
from werkzeug.exceptions import abort


init_object = Util.try_function_on_dict([OAuth2Service.from_dict, Service.from_dict, Util.initialize_object_from_json])

def index():
    services = Util.storage.getServices()
    data = {
        "length": len(services),
        "list": services
    }
    return jsonify(data)


def get(servicename):
    svc = Util.storage.getService(servicename)
    if svc is not None:
        return jsonify(svc)

    abort(Response(f"{servicename} not found."))
    

def post():
    svc = init_object(request.json)

    try:
        Util.storage.addService(svc)

    except ServiceExistsAlreadyError:
        Util.storage.addService(svc, Force=True)
        return jsonify({"success": True}), 204
    except:
        raise

    return jsonify({"success": True})