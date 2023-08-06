from flask import Blueprint
from flask_restful import Api


from pyfw.api_1_0.respful import CommonUserInfoListApi, CommonUserInfoApi

api = Blueprint('api', __name__)
rest_api = Api(api, catch_all_404s=True)


rest_api.add_resource(CommonUserInfoListApi, '/commonuserinfos',endpoint = 'commonuserinfos')
rest_api.add_resource(CommonUserInfoApi, '/commonuserinfo/<int:id>',endpoint = 'commonuserinfo')


