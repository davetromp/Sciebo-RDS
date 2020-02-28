import Singleton
from flask import jsonify


def get(user_id, project_id):
    return jsonify(Singleton.ProjectService.getProject(user_id, int(project_id)))


def delete(user_id, project_id):
    resp = Singleton.ProjectService.removeProject(user_id, int(project_id))

    if resp:
        return None, 204

    raise Exception("given project not removed")


def patch(user_id, project_id):
    # TODO Implement me
    pass
