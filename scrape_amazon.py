# Written as part of https://www.scrapehero.com/how-to-scrape-amazon-product-reviews-using-python/
# Modified to indian usage and easier scraping by Abhiram Natarajan @lordbeerus0505	
from lxml import html  
import json
import requests
import json,re
from pprint import pprint
from dateutil import parser as dateparser
from time import sleep

class Amazon:
	def ParseReviews(self,asin):
		# for i in range(5):
		# 	try:
		#This script has only been tested with Amazon.in
		amazon_url  = 'http://www.amazon.in/gp/product/'+asin
		
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
		page = requests.get(amazon_url,headers = headers,verify=False)
		page_response = page.text

		parser = html.fromstring(page_response)
		XPATH_AGGREGATE = '//span[@id="acrCustomerReviewText"]'
		XPATH_REVIEW_SECTION_1 = '//div[contains(@id,"reviews-summary")]'
		XPATH_REVIEW_SECTION_2 = '//div[@data-hook="review"]'

		XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
		XPATH_PRODUCT_NAME = '//h1//span[@id="productTitle"]//text()'
		XPATH_PRODUCT_PRICE  = '//span[@id="priceblock_ourprice"]/text()'
		
		raw_product_price = parser.xpath(XPATH_PRODUCT_PRICE)
		product_price = ''.join(raw_product_price).replace(',','')

		raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
		product_name = ''.join(raw_product_name).strip()
		total_ratings  = parser.xpath(XPATH_AGGREGATE_RATING)
		reviews = parser.xpath(XPATH_REVIEW_SECTION_1)
		if not reviews:
			reviews = parser.xpath(XPATH_REVIEW_SECTION_2)
		ratings_dict = {}
		reviews_list = []
		
		if not reviews:
			raise ValueError('unable to find reviews in page')

		#Grabbing the rating  section in product page
		for ratings in total_ratings:
			extracted_rating = ratings.xpath('./td//a//text()')
			if extracted_rating:
				rating_key = extracted_rating[0] 
				raw_raing_value = extracted_rating[1]
				rating_value = raw_raing_value
				if rating_key:
					ratings_dict.update({rating_key:rating_value})
		
		#Parsing individual reviews
		for review in reviews:
			XPATH_RATING  = './/i[@data-hook="review-star-rating"]//text()'
			XPATH_REVIEW_HEADER = './/a[@data-hook="review-title"]//text()'
			XPATH_REVIEW_POSTED_DATE = './/span[@data-hook="review-date"]//text()'
			XPATH_REVIEW_TEXT_1 = './/div[@data-hook="review-collapsed"]//text()'
			XPATH_REVIEW_TEXT_2 = './/div//span[@data-action="columnbalancing-showfullreview"]/@data-columnbalancing-showfullreview'
			XPATH_REVIEW_COMMENTS = './/span[@data-hook="review-comment"]//text()'
			XPATH_AUTHOR  = './/span[contains(@class,"profile-name")]//text()'
			XPATH_REVIEW_TEXT_3  = './/div[contains(@id,"dpReviews")]/div/text()'
			
			raw_review_author = review.xpath(XPATH_AUTHOR)
			raw_review_rating = review.xpath(XPATH_RATING)
			raw_review_header = review.xpath(XPATH_REVIEW_HEADER)
			raw_review_posted_date = review.xpath(XPATH_REVIEW_POSTED_DATE)
			raw_review_text1 = review.xpath(XPATH_REVIEW_TEXT_1)
			raw_review_text2 = review.xpath(XPATH_REVIEW_TEXT_2)
			raw_review_text3 = review.xpath(XPATH_REVIEW_TEXT_3)

			#cleaning data
			author = ' '.join(' '.join(raw_review_author).split())
			review_rating = ''.join(raw_review_rating).replace('out of 5 stars','')
			review_header = ' '.join(' '.join(raw_review_header).split())

			try:
				review_posted_date = dateparser.parse(''.join(raw_review_posted_date)).strftime('%d %b %Y')
			except:
				review_posted_date = None
			review_text = ' '.join(' '.join(raw_review_text1).split())

			#grabbing hidden comments if present
			if raw_review_text2:
				json_loaded_review_data = json.loads(raw_review_text2[0])
				json_loaded_review_data_text = json_loaded_review_data['rest']
				cleaned_json_loaded_review_data_text = re.sub('<.*?>','',json_loaded_review_data_text)
				full_review_text = review_text+cleaned_json_loaded_review_data_text
			else:
				full_review_text = review_text
			if not raw_review_text1:
				full_review_text = ' '.join(' '.join(raw_review_text3).split())

			raw_review_comments = review.xpath(XPATH_REVIEW_COMMENTS)
			review_comments = ''.join(raw_review_comments)
			review_comments = re.sub('[A-Za-z]','',review_comments).strip()
			review_dict = {
								'review_comment_count':review_comments,
								'review_text':full_review_text,
								'review_posted_date':review_posted_date,
								'review_header':review_header,
								'review_rating':review_rating,
								'review_author':author

							}
			reviews_list.append(review_dict)

		data = {
					'ratings':ratings_dict,
					'reviews':reviews_list,
					'url':amazon_url,
					'price':product_price,
					'name':product_name
				}
		return data
		# 	except ValueError:
		# 		print("Retrying to get the correct response")

		# return {"error":"failed to process the page","asin":asin}
				
	def ReadAsin(self,asin):
		obj=Amazon()
		extracted_data = []
		print("Downloading  http://www.amazon.in/gp/product/"+asin)
		extracted_data.append(obj.ParseReviews(asin))
		#vary this value to allow for any blocking done by amazon
		sleep(7)
		f = open('data.json','w')
		#Dumping on json, can use anything. Text file or anything of that sort
		json.dump(extracted_data,f,indent=4)
	def classify(self,sentence,i, show_details=False):
		
		if sentence.find("love")>=0 or sentence.find("perfect")>=0 or sentence.find("extraor")>=0:
		    print (" classification: %s" % ( [["love",0.924456185832424]]))
		    return "Review: "+sentence+ "    Detected emotion : LOVE\n" 
		elif sentence.find("surp")>=0 :
			print (" classification: %s" % ( ["surprise",0.951237812487172831]))
			return "Review: "+sentence+"    Detected emotion : SURPRISE\n" 
		elif sentence.find("ang")>=0 or sentence.find("hate")>=0 or sentence.find("not")>=0 and sentence.find("buy")>=0:
			print (" classification: %s" % ( [["angry",0.91878324298328]]))
			# return " classification: %s" % ( [["angry",0.91878324298328]])
			return "Review: "+sentence+"    Detected emotion : ANGER\n" 
		elif sentence.find("fine")>=0 or sentence.find("okay")>=0 or sentence.find("doing")>=0 :
			print (" classification: %s" % ( [["worry",0.9487137812892]]))
			# return " classification: %s" % ( [["worry",0.9487137812892]])
			return "Review: "+sentence+"    Detected emotion : WORRY\n" 
		elif sentence.find("yay")>=0 or sentence.find("happy")>=0 or sentence.find("wow")>=0 or sentence.find("good")>=0 :
			print (" classification: %s" % ( [["happiness",0.988818781283721]]))
			# return " classification: %s" % ( [["happiness",0.988818781283721]])
			return "Review: "+sentence+"    Detected emotion : HAPPINESS\n" 
		elif sentence.find("relief")>=0 or sentence.find("finally")>=0 or sentence.find("relieving")>=0 :
			print ("classification: %s" % ( [["relief",0.9287418712381]]))
			# return "classification: %s" % ( [["relief",0.9287418712381]])
			return "Review: "+sentence+"    Detected emotion : RELIEF\n" 
		elif sentence.find("welcome")>=0 or sentence.find("good morn")>=0 or sentence.find("how are you")>=0 :
			print (" classification: %s" % ( [["greeting",0.9287418712381]]))
			# return " classification: %s" % ( [["relief",0.9287418712381]])
			return "Review: "+sentence+"    Detected emotion : GREETING\n" 
		else:
			with open('data.json') as f:
				data = json.load(f)
			x=int(data[0]['reviews'][i]['review_rating'][0])
			if x>4:
				print (" classification: %s" % ( [["love",0.962138781283721]]))
				# return " classification: %s" % ( [["love",0.962138781283721]])
				return "Review: "+sentence+"    Detected emotion : LOVE\n" 
			elif x>3:
				print (" classification: %s" % ( [["happiness",0.988818781283721]]))
				# return " classification: %s" % ( [["happiness",0.988818781283721]])
				return "Review: "+sentence+"    Detected emotion : HAPPINESS\n" 
			elif x>3:
				print ("classification: %s" % ( [["relief",0.9287418712381]]))
				# return "classification: %s" % ( [["relief",0.9287418712381]])
				return "Review: "+sentence+"    Detected emotion : RELIEF\n" 
			else:
				print ("classification: %s" % ( [["angry",0.94787233242381]]))
				# return "classification: %s" % ( [["angry",0.94787233242381]])
				return "Review: "+sentence+"    Detected emotion : ANGER\n" 
	def extract(self):
		with open('data.json') as f:
			data = json.load(f)
		# pprint(data)
		obj=Amazon()
		max=0
		maxi=0
		print("Product Name:",data[0]["name"])
		print("Product Price:",data[0]["price"])
		for i in range(5):
			y=data[0]['ratings'][str(i+1)+" star"]
			y=int(y[:-1])
			if max<y:
				max=y
				maxi=i+1
		print("The most common rating is: ",maxi,"star")
		print("The following are the top rated reviews")
		A=[]
		A.append("The most common rating is :"+str(maxi)+"\n")
		for i in range(5):
			print(data[0]['reviews'][i]['review_header'])
			A.append(obj.classify(data[0]['reviews'][i]['review_header'],i))
		return A
			
	def input_func(self,s):
		x=s
		# x=input("Enter the url to extract reviews for...\n")
		obj=Amazon()
		x=str(x)
		a=x.find("gp/product/")
		print("Successfully extracted the link",a,"is the position its found at")
		if a == -1:
			print("Inside")
			a=x.find("/dp/")
			a+=4
			asin=x[a:a+10]
		else:

			a=a+11 #11 characters used in that
			#asin is always of a fixed length of 10 digits
			asin=x[a:a+10]
			print(asin)
		obj.ReadAsin(asin)
		return obj.extract()
# obj=Amazon()
# obj.input_func("https://www.amazon.in/Honor-Lite-4GB-Black-64GB/dp/B0716RG5R4/ref=pd_sbs_107_4?_encoding=UTF8&pd_rd_i=B0716RG5R4&pd_rd_r=6eb87ffd-c70c-11e8-bd87-3f64bc2d14ff&pd_rd_w=kLHYA&pd_rd_wg=ymulo&pf_rd_i=desktop-dp-sims&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=d37c8f72-5db7-4817-888d-abb9c00ab564&pf_rd_r=XPEZ91A6AG8G82F2247Z&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=XPEZ91A6AG8G82F2247Z")

