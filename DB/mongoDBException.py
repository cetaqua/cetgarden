class MongoDBException(Exception):

    def __init__(self, msg="Mongo Exception"):
        super(ArraySetExeption, self).__init__(msg)