## story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chk_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "pankajpandey@gmail.com"}
    - slot{"email_id": "pankajpandey@gmail.com"}
    - action_send_email
    - utter_email_sent
* thankyou
    - utter_goodbye


## story 2
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "kota"}
    - slot{"location": "Prayagraj"}
    - action_chk_location
    - slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Above 700"}
    - slot{"budget": "Above 700"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "pankajpandey@gmail.com"}
    - slot{"email_id": "pankajpandey@gmail.com"}
    - action_send_email
    - utter_email_sent

##story 3
* greet
    - utter_greet
* restaurant_search{"location": "kolkota"}
    - slot{"location": "kolkota"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "simrankaurbadan3009@gmail.com"}
    - slot{"email_id": "simrankaurbadan3009@gmail.com"}
    - action_send_email
    - utter_email_sent

## story 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_chk_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget":"0"}
    - slot{"budget": "0"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "pkp@gmail.com"}
    - slot{"email_id": "pkp@gmail.com"}
    - action_send_email
    - utter_email_sent

## story 5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"budget": "Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye

## story 6
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - action_chk_location
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"budget":"300"}
    - slot{"budget": "300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "chebroluharika@gmail.com"}
    - slot{"email_id": "chebroluharika@gmail.com"}
    - action_send_email
    - utter_email_sent

## story 7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"budget": "Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "chebroluharika@gmail.com"}
    - slot{"email_id": "chebroluharika@gmail.com"}
    - action_send_email
    - utter_email_sent

## story 8
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "ghazipur"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "ghazipur"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_chk_location
    - slot{"location": "Hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget":"Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "avinash@gmail.com"}
    - slot{"email_id": "avinash@gmail.com"}
    - action_send_email
    - utter_email_sent

## story 9
* greet
    - utter_greet
* restaurant_search{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - action_chk_location
    - slot{"location": "aligarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget":"Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "simran@gmail.com"}
    - slot{"email_id": "simran@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## story 10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_chk_location
    - slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "pankaj@gmail.com"}
    - slot{"email_id": "pankaj@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## story 11
* greet
    - utter_greet
* restaurant_search{"location": "mizoram"}
    - slot{"location": "mizoram"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_chk_location
    - slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## story 12
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"budget":"Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## story 13
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_chk_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "pankaj@gmail.com"}
    - slot{"email_id": "pankaj@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## story 14
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - action_chk_location
    - slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Above 700"}
    - slot{"budget": "Above 700"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "sim@gmail.com"}
    - slot{"email_id": "sim@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## story 15
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "Below 300"}
    - slot{"budget": "Below 300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
* deny
    - utter_goodbye
    - action_restart

## story 16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_chk_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "Above 700"}
    - slot{"budget": "Above 700"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

## story 17
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_chk_location
    - slot{"location": "Bangalore"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_email_conf
* send_mail{"email_id": "simrankaurbadan3009@gmail.com"}
    - slot{"email_id": "simrankaurbadan3009@gmail.com"}
    - action_send_email
    - utter_email_sent
* thankyou
    - utter_goodbye


## story 18
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_chk_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": " 300"}
    - slot{"budget": " 300"}
    - action_search_restaurants
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_chk_location
    - slot{"location": "Delhi"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart


## story 19
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Kota"}
    - slot{"location": "Kota"}
    - action_chk_location
    - slot{"location": "Kota"}
    - utter_ask_budget
* restaurant_search{"budget": " 300"}
    - slot{"budget": " 300"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart


## story 20
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Kota"}
    - slot{"location": "Kota"}
    - action_chk_location
    - utter_ask_budget
* restaurant_search{"budget": " 300"}
    - slot{"budget": " 300"}
    - action_search_restaurants
    - utter_email_conf
* send_mail{"email_id": "simrankaurbadan3009@gmail.com"}
    - slot{"email_id": "simrankaurbadan3009@gmail.com"}
    - action_send_email
    - utter_email_sent
* thankyou
    - utter_goodbye
    - action_restart

* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_chk_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinese", "budget": "above 700"}
    - slot{"budget": "above 700"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "jamnagar"}
    - slot{"location": "jamnagar"}
    - action_chk_location
    - slot{"location": "jamnagar"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_chk_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "simrankaurbadan3009@gmail.com"}
    - slot{"email_id": "simrankaurbadan3009@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

* restaurant_search{"budget": " Above 700"}
    - slot{"budget": " Above 700"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_chk_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart

* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - utter_ask_location
* restaurant_search{"location": "Kota"}
    - slot{"location": "Kota"}
    - action_chk_location
    - slot{"location": "Kota"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "simrankaurbadan3009@gmail.com"}
    - slot{"email_id": "simrankaurbadan3009@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_chk_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye
    - action_restart
