from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import zomatopy

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):

        count = 0
        global restaurants
        response = 'Showing you top rated restaurants:\n'
        config = {"user_key": "3d3f2eb6c22379ad24fe5aeec2cda1a3"}
        zomato = zomatopy.initialize_app(config)
        budget = tracker.get_slot('budget')
        print(budget)
        if (budget == 'Below 300') or (budget == '300') or (budget == ' 300'):
            budget_min = '0'
            budget_max = '300'
            print(budget_max, budget_min)
        elif(budget == '300 to 700') or (budget == 'medium'):
            budget_min = '300'
            budget_max = '700'
            print(budget_max, budget_min)
        elif (budget == 'Above 700') or (budget == 'above 700') or (budget == '700') or (budget == ' Above 700'):
            budget_min = '700'
            budget_max = '1000'
            print(budget_max, budget_min)
            
        loc = tracker.get_slot('location')
        print(loc)
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'chinese': 25, 'south indian': 85, 'american': 1, 'north indian': 50, 'italian': 55,
                         'mexican': 73}
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 80)
        response = "Showing you top rated restaurants:" + "\n"
        response1 = ''
        data = json.loads(results)
        # Sort the results according to the restaurant's rating
        d_budget_rating_sorted = sorted(data['restaurants'],
                                        key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True)
        if data['results_found'] == 0:
            response = "Sorry! There are no restaurants matching your preferences! " \
                       "Please search again!"
            
        else:
            for restaurant in d_budget_rating_sorted:
                # Getting Top 10 restaurants for chatbot response
                if ((restaurant['restaurant']['average_cost_for_two'] >= int(budget_min)) and (
                        restaurant['restaurant']['average_cost_for_two'] <= int(budget_max)) and (count < 10 )):
                    response = response + restaurant['restaurant']['name'] + " in " + \
                               restaurant['restaurant']['location']['address'] + " has been rated " + \
                               restaurant['restaurant']['user_rating']['aggregate_rating'] + "." + '\n' + '\n'
                    response1 = response1 + restaurant['restaurant']['name'] + " in " + \
                               restaurant['restaurant']['location']['address'] + " has been rated " + \
                               restaurant['restaurant']['user_rating']['aggregate_rating'] + ' and cost for two people is ' + str(restaurant['restaurant']['average_cost_for_two']) + "." + '\n \n'
                    print(response)
                    count = count + 1
                    print(count)
        if (count == 5):
            dispatcher.utter_message(response)
        elif (count < 5) or (count > 0):
            dispatcher.utter_message(response)
        elif (count == 0):
            response = "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"
            dispatcher.utter_message(response)

        restaurants = response1


class ActionCheckLocation(Action):

    def name(self):
        return 'action_chk_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')

        cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune',
                  'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly',
                  'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City',
                  'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur',
                  'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon',
                  'Guwahati', 'Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu',
                  'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam',
                  'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram',
                  'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik',
                  'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Prayagraj', 'Raipur', 'Rajkot',
                  'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar',
                  'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur',
                  'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada']

        cities_lower = [x.lower() for x in cities]
        if loc:
            if loc.lower() not in cities_lower:
                dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
                return [SlotSet('location', None)]
        else:
            dispatcher.utter_message("Sorry, we did not got the city you searched for. Please try again.")
        return [SlotSet('location', loc)]


class SendEmail(Action):
    
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email_id')
       
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('foodie.assistance@gmail.com', 'loowkacftxrhckqm')

        msg = MIMEMultipart()
        message = '''
Hi, This is a mail from FOODIE chatbot. Please find below the list of all the restaurants as per your choice:

''' + restaurants + '''

Happy fooding!!!!!

This mail is auto generated and you cannot reply to this mail. Thanks for your time.
'''

        msg['From'] = 'simrankaurbadan3009@gmail.com'
        msg['To'] = email
        msg['Subject'] = "Foodie - Restaurant search"

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg


class ActionVerifyCuisine(Action):

    def name(self):
        return 'action_verify_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot('cuisine')
        if cuisine.lower() not in ['chinese', 'south indian', 'american', 'north indian', 'italian', 'mexican']:
            dispatcher.utter_message("Sorry, we do not deliver " + cuisine + " food. Please select some other cuisine.")
            return [SlotSet('cuisine', None)]
        return [SlotSet('cuisine', cuisine)]
