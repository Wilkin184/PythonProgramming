# -*- coding: utf-8 -*-
"""Midterm_Practical_Eaint_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xFRMdgl9tbAC6HlR5-CfDBLd8ZlinKSW

Write a Python program to read the name from Q2.txt and create email using domain 'parami.edu.mm' and save the results as dictionary : {'name': 'name@parami.edu.mm'}. Please take note that your email should not include space or any special characters and all charcters should be in lowercase.
"""

# Step 1: Read names from Q2.txt into a list
with open('Q2.txt', 'r') as names:
    header = names.readline()
    namelist = names.readlines()

def list_emails(name_list, domain):
    email_dic = {}

    for name in name_list:
        clean_name = name.strip().lower()
        final_name = clean_name.replace(' ', '') + "@" + domain

        email_dic[name.strip()] = final_name

    return email_dic

domain = "parami.edu.mm"
email_name = list_emails(namelist, domain)

for name, email in email_name.items():
    print("This is your name - {} : This is your Parami Email {}".format(name, email))