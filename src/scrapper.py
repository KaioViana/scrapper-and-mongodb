def scrapper_xiaomiProducts():
    import requests
    import ast 
    from urllib.request import urljoin
    from bs4 import BeautifulSoup


    dictionary_items = {}
    item_index = 1

    url = 'https://busca.magazineluiza.com.br/busca?q=xiaomi&p=&ranking=3&typeclick=4&ac_pos=header'
    req = requests.get(url)
    html = req.text

    html_bs = BeautifulSoup(html)
    lista_items = html_bs.find_all('', {'class': 'nm-product-item'})

    for item in lista_items:
        if 'Smartphone' not in item.find('', {'class': 'nm-product-name'}).text:
            continue
        else:
            data_product = item.find('a')
            data_product = data_product.attrs['data-product']
            dict_data_product = ast.literal_eval(data_product)
            
            item_img = item.find('img')
            item_img = item_img.attrs
            
            product = str(item.find('', {'class': 'nm-product-name'}).text).strip()
            value = dict_data_product['price']
            image_src = item_img['src']

            dictionary_items['item ' + str(item_index)] = [product, value, image_src]
            item_index += 1

    return dictionary_items


def main():
    from mongoAtlas import MongoAtlas


    items = scrapper_xiaomiProducts()

    # try connection MongoAtlas
    try:
        client = 'mongodb+srv://FirstMongo:91796337@scrappers-qhxp9.mongodb.net'
        mongo = MongoAtlas(client, 'Scrappers', 'xiaomi')
    except Exception as error:
        print(f'Exceção encontrada durante a tentativa de conexão com MongodbAtlas: {error}')
        exit()

    # post documents
    for value in items.values():
        mongo.post(value[0], value[1], value[2])    

if __name__ == '__main__':
    main()
