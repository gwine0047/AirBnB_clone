"""creating and reloading a storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()