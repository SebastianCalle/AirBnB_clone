#!/usr/bin/python3
"""
init module of models
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
