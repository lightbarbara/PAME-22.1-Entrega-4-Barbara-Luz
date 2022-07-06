from app.local.controller import LocalCreate, LocalDetails
from flask import Blueprint

local_api = Blueprint('local_api', __name__)

local_api.add_url_rule('/registro_local', view_func = LocalCreate.as_view('registro_local'), methods = ['POST', 'GET'])
local_api.add_url_rule('/modifica_local', view_func = LocalDetails.as_view('modifica_local'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])