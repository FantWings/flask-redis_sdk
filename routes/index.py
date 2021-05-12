from flask import Blueprint, request
from lib.redis import Redis

index = Blueprint('index', __name__)


@index.route('/', methods=['GET'])
def hello():
    return "HelloWorld"


@index.route('/read', methods=['GET'])
def redis_read():
    key = request.args.get('key')
    return str(Redis.read(key))


@index.route('/write', methods=['GET'])
def redis_write():
    key = request.args.get('key')
    value = request.args.get('value')
    expire = request.args.get('expire' or None)
    return str(Redis.write(key, value, expire))


@index.route('/delete', methods=['GET'])
def redis_delete():
    key = request.args.get('key')
    return str(Redis.delete(key))
