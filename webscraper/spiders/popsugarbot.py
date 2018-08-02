# -*- coding: utf-8 -*-
import scrapy


class PopsugarbotSpider(scrapy.Spider):
    name = 'popsugarbot'

    protocol = 'file:///'
    filepath = 'C:/Users/Solange/Documents/Projects/Summer_Of_Code/webscraper/local/'
    filename = 'popsugar_images_jennifer_garner.html'
    start_urls = [protocol + filepath + filename]

    # location of csv file
    custom_settings = {
        'FEED_URI': 'data/popsugar-jennifer-garner.csv',
    }

    def parse(self, response):
        # Extracting image URLs using CSS selectors
        titles = response.css(".img::attr(data-link-title)").extract()
        images = response.css(".img::attr(data-largesrc)").extract()

        for item in zip(titles, images):
            scraped_info = {
                'title': item[0],
                # Sets the url for scrapy to download images
                'image_urls': [item[1]]
            }
            # Yield the scraped information to scrapy
            yield scraped_info
