import uuid

import scrapy

import models
import database as _database
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=_database.engine)
session = Session()


class FlatSpider(scrapy.Spider):
    name = 'flats'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=' +
                  str(500) + '&page=' + str(1) + '']

    async def parse(self, response):
        strTable = "<html><meta charset=\"UTF-8\"><table><tr><th>Flats</th><th> </th></tr>"
        jsonresponse = response.json()
        for item in jsonresponse["_embedded"]['estates']:
            db_flat = models.Flat(id=uuid.uuid4(), title=str(item['name']))
            strRW = "<tr><td>" + item['name'] + "</td>"
            for image in item['_links']['images']:
                db_image = models.Images(id=uuid.uuid4(), image_url=str(image['href']), flat_id=db_flat.id)
                session.add(db_image)
                db_flat.images.append(db_image)
                strRW = strRW + "<td><img src=\"" + image['href'] + "\"></td>"
            session.add(db_flat)
            strRW = strRW + "</tr>"
            strTable = strTable + strRW
        session.commit()
        strTable = strTable + "</table></html>"
        hs = open("flats.html", 'w')
        hs.write(strTable)
        hs.close()

        yield None

