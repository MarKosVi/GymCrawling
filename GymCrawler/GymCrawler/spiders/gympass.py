# -*- coding: utf-8 -*-
import scrapy


class GympassSpider(scrapy.Spider):
    name = 'gympass'
    start_urls = [
        'https://www.gympass.com/negocios',
        ]

    def parse(self, response):
        for gym in response.css('div.gym_list_s'):
            yield {
                'name': gym.css('div.gym_list_info_outer_container div.gym_list_info_container h3::text').get(),
                'link':'https://www.gympass.com/negocios'+gym.css('div.gym_list_s a::attr(href)').get(),
            }
        next_page = 'https://www.gympass.com/negocios'+gym.css('div.gym_list_s a::attr(href)').get()




#gym.css('div.details_revamp div.card-box div.body-row p::text').get()
