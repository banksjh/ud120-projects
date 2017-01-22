#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "dataset size", len(enron_data)
print "features:", len(enron_data['TAYLOR MITCHELL S'])
iterator = enron_data.iterkeys()
Pois = 0
people_with_salary_data = 0
people_with_emails = 0

while True:
    try:
        person = iterator.next()
    except StopIteration as e:
        break
    if enron_data[person]["poi"] == 1:
        Pois = Pois + 1
    if enron_data[person]["salary"] != 'NaN':
        people_with_salary_data = people_with_salary_data + 1
    if enron_data[person]['email_address'] != 'NaN':
        people_with_emails = people_with_emails + 1

print "POIs:", Pois
print "People with salary data:", people_with_salary_data
print "People with emails:", people_with_emails
