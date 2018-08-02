# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/womenintech/']
    start_urls = ['https://www.reddit.com/r/womenintech/']

    # location of csv file
    custom_settings = {
        'FEED_URI': 'data/reddit-women-in-tech.csv'
    }

    def parse(self, response):
        # Extracting content using CSS selectors
        titles = response.css('.fiq55l-0::text').extract()
        votes = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()
        times = response.css('._3jOxDPIQ0KaOWpzvSQo-1s::text').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()

        # Give the extracted content wise
        for item in zip(titles, votes, times, comments):
            # create a dictionary to store the scraped information
            scraped_info = {
                'title': item[0],
                'votes': item[1],
                'created': item[2],
                'comments': item[3]
            }

            # Yield the scraped information to scrapy
            yield scraped_info
