class MongoAtlas(object):
    """
    Classe MongodbAtlas. Conecta e faz chamadas ao banco
    """
    from pymongo import MongoClient


    def __init__(self, client, data_base, schema):
        """
        Inicializa um objeto MongoAtlas.

        :parâmetro client: URI de conexão
        :parâmetro data_base: nome do banco
        :parâmetro schema: nome da collection
        """
        self.cluster = self.MongoClient(client, connect=False)
        self.db  = self.cluster[data_base]
        self.collection = self.db[schema]


    def post(self, product, value, img_url):
        """
        Envia um documento contendo informações sobre um produto.
        """
        from time import strftime, localtime


        try:
            post = {"product": product, "value": value, "img": img_url, "date": strftime('%d-%m-%y %H:%M:%S', localtime())}
            self.collection.insert_one(post)
        except Exception as error:
            print(f'Exceção encontrada ao tentar postar o documentono no Mongodb:\nDocument: {post}\n{error}')
