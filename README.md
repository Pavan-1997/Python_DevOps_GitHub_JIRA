# Python DevOps GitHub - JIRA               
           
Automation done for the below scenario:  
```
There are lot of QE when they noticed a bug while testing an application they will create an issue on GitHub repository. Development team in the organization will go to the GitHub repo and triage the issue if they find the issue is not valid then they close the issue else work on it. They need to go to JIRA dashboard and create a ticket for the issue they are working this is a lot manual work for them 
```
- DevOps team will automate the JIRA and GitHub

---
##  JIRA API Token

JIRA ( Template - Scrum | Type - Team-managed )

Go to JIRA dashboard -> Profile -> Manage your account -> Security -> Create and Manage API Token -> Create API token

Use the python script `create-issue.py` to create an issue in jira dashboard

---
# Implementation

 - Use the python scripts `flask_hello.py` and `create_jira.py` to integrate GitHub and Jira
 - Create a Webhook as below for the Ubuntu machine where the `flask_hello.py` is running

![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/99e842ed-2f0e-4bc3-b730-313d082029b3)

 - Below is a test connection created by GitHub to Ubuntu server
  
![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/971a8f5e-9cf1-40bc-abe4-227c73caf499)
