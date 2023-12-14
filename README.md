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
# Implementation (GitHub - Jira)

 - Use the python scripts `flask_hello.py` and `create_jira.py` to integrate GitHub and Jira
 - Create a Webhook as below for the Ubuntu machine where the `flask_hello.py` is running

![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/99e842ed-2f0e-4bc3-b730-313d082029b3)

 - Below is a test connection created by GitHub to Ubuntu server
  
![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/971a8f5e-9cf1-40bc-abe4-227c73caf499)

- Below is the Ubuntu server running the `flask_hello.py` server

![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/508b2145-0df6-454e-bb64-4c6c4a05706b)

- Below is the Issue Comment given to automate the Jira ticket creation

![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/f5b65e07-2e68-4ad3-807d-d467af66ebde)

- Below is the Jira ticket created by the Issue Comment

![image](https://github.com/Pavan-1997/Python_DevOps_GitHub_JIRA/assets/32020205/1c4900cc-f688-4c08-9d98-d766a80c3b9c)
