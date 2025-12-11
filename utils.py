import ZODB
import ZODB.FileStorage

def connect():
    storage = ZODB.FileStorage.FileStorage('data.fs')
    db = ZODB.DB(storage=storage)
    return db.open()

def get_root():
    return connect().root()