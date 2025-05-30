from flask import jsonify
from datetime import datetime
from models import *
import time

def sendmsg(msg):
    return jsonify({'message': msg})

def user_to_content(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'description': user.description
    }

def group_to_content(group):
    return {
        'id': group.id,
        'groupname': group.groupname,
        'leaderid': group.leaderid,
        'createdtime': group.createdtime.strftime('%Y-%m-%d'),
        'description': group.description
    }

def document_to_content(document):
    return {
        'id': document.id,
        'title': document.title,
        'creator_id': document.creator_id,
        'created_time': document.created_time.strftime('%Y-%m-%d %H:%M'),
        'modified_time': document.modified_time,
        'recycled': document.recycled
    }

def get_newid():
    return int(time.time() * 1000)

def valid_login(username, password):
    user = User.query.filter_by(username=username).first()
    return user and user.password == password

def get_user_byusername(username):
    return User.query.filter_by(username=username).first()