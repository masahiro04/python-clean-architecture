import json
import os

from flask import Blueprint, request
from flask.wrappers import Response

from repository.memrepo import MemRepo
from repository.postgresrepo import PostgresRepo

from use_cases.room_list import room_list_use_case
from serializers.room import RoomJsonEncoder
from requests.room_list import build_room_list_request
from responses import ResponseTypes

blueprint = Blueprint("room", __name__)


STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

postgres_configuration = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
    "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
    "APPLICATION_DB": os.environ["APPLICATION_DB"],
}


@blueprint.route("/rooms", methods=["GET"])
def room_list():
    query_params = {
        "filters": {}
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            query_params["filters"][arg.replace("filter_", "")] = values

    request_object = build_room_list_request(
        filters=query_params["filters"]
    )

    repo = PostgresRepo(postgres_configuration)
    response = room_list_use_case(repo, request_object)

    return Response(
        json.dumps(response.value, cls=RoomJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type]
    )
