import requests
from sys import argv
from requests.exceptions import ConnectionError
from xml.etree import ElementTree
import re

class  GoodreadsAPIClient:
      def __init__(self,url):
            self.url=url
            
      def get_book_details(self):
            d={}
            print(self.url)
            response = requests.get(self.url, stream=True)
            print(response)
            response.raw.decode_content = True
            tree = ElementTree.parse(response.raw)

            root = tree.getroot()
            value=None
            for i in root.iter('book'):
              id=i.find('id').text
              if id==self.book_id:
                    
                    d[id]=id
                    d[id]={}

                    title=i.find('title').text
                    d[id]['title']=title

                    average_rating=i.find('average_rating').text
                    average_rating= float(average_rating) if average_rating else None
                    d[id]['average_rating']=average_rating

                    ratings_count=i.find('ratings_count').text
                    ratings_count=int(ratings_count)if ratings_count else None
                    d[id]['ratings_count']=ratings_count

                    num_pages=i.find('num_pages').text
                    num_pages=int(num_pages) if num_pages else None
                    d[id]['num_pages']=num_pages

                    image_url=i.find('image_url').text
                    d[id]['image_url']=image_url

                    publication_year=i.find('publication_year').text
                    d[id]['publication_year']=publication_year

                    for author in i.findall('authors'):
                        for name in author.findall('author'):
                            name=name.find('name').text
                            d[id]['author']=name

                
                    value=d.get(self.book_id,None)
                    break
              else:
                  continue
            print(value) if value else print("This Book id does not exists")

      def validate_url(self):
            
            try:
                  response = requests.get(self.url, stream=True)
                  self.book_id=re.findall('\d+', self.url)[0]
                  
                  print(self.book_id)
                  start_index=0
                  if self.book_id:
                        end_index=self.url.find(self.book_id)
                  else:
                        print("Invalid book id")
                        exit()
                        
                  key='.xml?key=gH0soNm1WW8KXaDBmg8KQw'
                  self.url= self.url[start_index:end_index]+self.book_id+key
                  print(self.url)
                  self.get_book_details()
            except Exception: # This is the correct syntax
                  print("raise an exception InvalidGoodreadsURL")
                  response = "No response"
                  exit()




if __name__ == "__main__": 


      try:
            url = argv[1]
            GoodreadsAPIClient(url).validate_url()        
      except IndexError:
            print("please  provide url input")
            exit()



   
   


     
