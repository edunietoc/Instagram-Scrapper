#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class Instagram_Scraper:

    def getData(self, hashtag, url):

        html = urllib.request.urlopen(url+hashtag, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        script = soup.find('script', text=lambda t: \
                           t.startswith('window._sharedData'))
        #print(soup.prettify())
        page_json = script.text.split(' = ', 1)[1].rstrip(';')
        data = json.loads(page_json)
      
        #print(data)
      
        
        print ('Scraping links with #' + hashtag+"...........")
        image_counter=0
        people_image_counter=0
        nonPeople_image_counter=0

        for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
          image_counter += 1

          print("")
          print("")
          try:
            accesibility_caption=post['node']['accessibility_caption']
            
            if "people" in accesibility_caption:
              #print("this image has a person in it")
              people_image_counter +=1
            else:
              #print("there is no one in this picture")
              nonPeople_image_counter +=1

          except:
            pass
            
          """
            image_src = post['node']['thumbnail_resources'][1]['src']
            hs = open(hashtag + '.txt', 'a')
            hs.write(image_src + '\n')
            hs.close()
           """ 
        print("Pics with people: ",people_image_counter)
        print("Pics with no people: ",nonPeople_image_counter)
        print("Total of Pics:", image_counter)
        print("Percentage of Pics with people: ",(people_image_counter/image_counter)*100)
          
    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        hashtag="diy"
        url = "https://www.instagram.com/explore/tags/"
        #with open('hashtag_list.txt') as f:
         #   self.content = f.readlines()
        #self.content = [x.strip() for x in self.content]
        #for hashtag in self.content:
        self.getData(hashtag,url)


if __name__ == '__main__':
    obj = Instagram_Scraper()
    obj.main()