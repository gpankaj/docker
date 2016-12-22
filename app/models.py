__author__ = 'pankajg'
from sqlalchemy import Table,Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from . import db

class AllDockerfiles(db.Model):
    __tablename__= 'all_dockerfile_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32),nullable=False)
    description = db.Column(db.String(256), nullable=True)
    content = db.Column(db.String(5026), nullable=False)
    private = db.Column(db.Boolean)
    owner = db.Column(db.String(32),nullable=False)
    date_of_creation = db.Column(DateTime, default=func.now())
    valid = db.Column(db.Boolean)

class AllDockerComposeFiles(db.Model):
    __tablename__ = 'all_dockercompose_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    content = db.Column(db.String(5026), nullable=False)
    private = db.Column(db.Boolean)
    owner = db.Column(db.String(32), nullable=False)
    date_of_creation = db.Column(DateTime, default=func.now())
    valid = db.Column(db.Boolean)
    docker_file_id = db.Column(db.Integer, ForeignKey('all_dockerfile_table.id'))

class Upvote(db.Model):
    __tablename__='upvotes'
    id = db.Column(db.Integer, primary_key=True)
    all_dockerfile_id = db.Column(db.Integer, db.ForeignKey('all_dockerfile_table.id'))
    all_dockercompose_id = db.Column(db.Integer,ForeignKey('all_dockercompose_table.id'))
    date = db.Column(DateTime, default=func.now())
    user_name = db.Column(db.String(100))