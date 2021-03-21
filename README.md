# Gmail Spam +
![Gmail_Spam_+_banner](/assets/banner.png)

Vivan Madan, Nick McGonigle, Brandon Kim
MoCoHacks 2021, submitting to Most Technically Impressive Hack

# Inspiration
Millions of scams and misinformation are emailed out every day, siphoning billions every year. Even though nearly every modern email client has a native spam filter, a handful still slip through the cracks. To those familiar with the online landscape, these emails are obvious, but older populations don't recognize these as easily. Scammers prey on these older, vulnerable populations, and we need a better, stronger defense for our inboxes.

# What it does
Gmail Spam + runs incoming emails through a -- machine learning model, generating a -- and accuracy score for each email. Emails above a certain threshhold (taking both scores into account) are moved into Gmail's temporary Trash section.
On the GUI, after signing in, the emails are listed with a Restore and Delete button. For falsely marked emails, Restore moves them back into the inbox. For properly marked emails, Delete permanently deletes the emails. The model takes into account which emails were Restored or Deleted for the future.

# How we built it
Gmail Spam + is built on Python. The GUI is built on tkinter, a Python module.
Interaction with Gmail was handled through imaplib.
The ML is a Naive Bayes model that comes with SciKit-Learn. Naive Bayes helps with Natural Language Processing (NLP) through a Bag of Words technique. It has been hyperparametered tuned to give the most optimal performance and to avoid overfitting. The dataset utilized to train the model was found on Kaggle and provided by UCI Machine Learning, all credit to the dataset goes to them.

# Challenges we ran into
One goal of our app was to update emails in the GUI in real time. However, Python doesn't work well with multiple threads, making it nearly impossible to run our GUI and algorithms simultaneously. In its current state, emails only update on application startup.
As Python is not optimal for OOP, we ran into many issues in importing different classes and files. Dependency injection was a lifesaver, as it helped us connect different classes more seamlessly.
imaplib's documentation on ID assignment was also ambiguous. Instead, we sorted and identified emails based on time sent, which would nearly never overlap.

# Accomplishments we're proud of
- We're especially proud of how Gmail, our ML, and the GUI interact together.
- We went from having no familiarity with tkinter, to building a clean GUI.
- This is our first hackathon for everybody on the team, so we're proud to come together and tackle this challenge.


# What we learned
- We learned how NLP models and Bag of Words techniques work.
- We had to learn a lot about of Python modules and imports interact.
- We learned how to use tkinter to design a functional GUI.
- We learned how to pull an effective all-nighter.

# What's next for Gmail Spam +
It's now apparent that choosing Python as our language was suboptimal, and in the future we would restructure our app in Java or JavaScript. With a more potent GUI toolkit, we hope to make our GUI more user-friendly and polished. We also hope to refine our ML model to identify emails more precisely.
