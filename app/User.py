""" User Model """
from ..orm.models import Model


class User(Model):
    """User Model"""
    __table__ = 'users'
    __primary_key__ = 'id'
    __fillable__ = ['name', 'email', 'password', 'role']
    __timestamps__ = True
    __hidden__ = ['password', 'role', 'created_at', 'updated_at', 'remember_token']
