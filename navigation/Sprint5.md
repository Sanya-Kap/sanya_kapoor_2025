
---
# ✨ My Work Showcase ✨

## 🖼️ Featured Projects
A collection of my work:

### Purpose of group project: 
*The website is a global platform where users can share and discover food reviews from around the world. Whether it's a hidden gem in Italy, street food in Thailand, or fine dining in France, the site allows travelers and food enthusiasts to post detailed reviews, including photos and ratings, about their culinary experiences.
The platform aims to connect people through the universal love of food, helping users explore authentic cuisines, make informed dining choices, and celebrate the cultural diversity of food in different countries. It fosters a global community of food lovers who inspire each other to try new dishes and discover unique flavors worldwide.*

---

### 🛠️ Checklist Item: *Asia Code*  
*This code helped allow the posts data to save in the backend*

<center/>
<img src="{{site.baseurl}}/images/channel.py.png" alt="Review"
    width="1200"
    height="500" />

<img src="{{site.baseurl}}/images/group.py.png" alt="Review"
    width="1200"
    height="500" />    

Initially, I only understood APIs as a way for systems to communicate, but I hadn't implemented one myself. Now, I've developed a feature where users can create a review on the frontend, which sends data to the backend with the API, and stores it in a database. I had to add an aditional code request to the group.py and channels.py folder. One challenge was handling the failed to fetch errors, but I learned how to fix it by configuring the backend properly and making sure the API paths were correct.

---

### 🛠️ Checklist Item: *Japan posting*  

<center/>
<img src="{{site.baseurl}}/images/asiaposting.png" alt="Review"
    width="500"
    height="350" />

<img src="{{site.baseurl}}/images/asiadatabse.png" alt="Review"
    width="1050"
    height="70" />    

<img src="{{site.baseurl}}/images/1st.png" alt="Review"
    width="700"
    height="1000" />    

This code above defines a SQLAlchemy model called Japan, which represents a database table named japans.

<img src="{{site.baseurl}}/images/2nd.png" alt="Review"
    width="700"
    height="1000" />    

This is the create function. Inserts a new Japan post into the database. If it is successful, it commits the transaction. If an error like a duplicate entry occurs, it rolls back and logs a warning.

I also have the read function which retrieves the post's details as a dictionary. It fetches the user name and channel name based on their IDs.Then it returns the data in a structured format.

<img src="{{site.baseurl}}/images/3rd.png" alt="Review"
    width="700"
    height="1000" />  

The update function fetches the Japan post by its ID. It then retrieves and updates title, content, and user ID. Then it commits changes if successful, or rolls back if an error occurs.

<img src="{{site.baseurl}}/images/4th.png" alt="Review"
    width="700"
    height="700" />  

This deletes the current Japan post from the database. If successful, it commits the deletion. If an error occurs, it rolls back and raises the exception.


*Through this code, I got familiar with CRUD operations. I previously did not know how to use SQLAlchemy functions but through creating and debugging this file I was able to grow my understanding.*

---

## List requests.  Use of list, dictionaries and database.  Code descriptions of area where you work with list (rows) and dictionaries (columns) of the database.
<img width="725" alt="Image" src="https://github.com/user-attachments/assets/e07f65e3-0944-4962-9ce9-7f57ae225aba" />
- Discuss formatting response data (JSON) from API into DOM <br>
<img width="413" alt="Image" src="https://github.com/user-attachments/assets/6fc8ec4a-0d22-4eaf-a035-a38c94bf17a4" /> <br>
frontend: DOM <br> <img width="475" alt="Image" src="https://github.com/user-attachments/assets/77f850db-1a9a-4d52-91ca-c3e0327f6052" />
- Discuss queries from database where you extract a Python List (rows). Mention how these queries are provide by a 3rd. party library. <br> <img width="707" alt="Image" src="https://github.com/user-attachments/assets/8b02993e-0e42-4cda-93ae-0b8cc8e4e7f6" />
- Discuss methods in "class" you created to work with columns (create, read, update, delete)
create:<br> <img width="646" alt="Image" src="https://github.com/user-attachments/assets/0427ec76-3f3c-470a-a680-a68e69b26a29" />
read: <br> <img width="716" alt="Image" src="https://github.com/user-attachments/assets/fc951ae8-cc7f-4ac1-9103-0860890dd49b" />
update:<br>  <img width="302" alt="Image" src="https://github.com/user-attachments/assets/795741c0-8155-41ec-a3b4-998bbbd69897" />
delete:<br> <img width="646" alt="Image" src="https://github.com/user-attachments/assets/0427ec76-3f3c-470a-a680-a68e69b26a29" />

## Algorithmic code request. Show the definition of code blocks to handle a request.
- Discuss API class (code block) you used to perform  get, post, put, and delete methods. <br>
<img width="827" alt="Image" src="https://github.com/user-attachments/assets/9e167ae3-7b46-43b3-9d4a-6bb9f404f1cb" /> <br> <img width="628" alt="Image" src="https://github.com/user-attachments/assets/21185c24-7da9-41b2-aecb-ad6e9b50a4a8" />
- Discuss a method/procedure in class that contains sequencing, selection, and iteration. <br>
<img width="959" alt="Image" src="https://github.com/user-attachments/assets/168658b6-21b5-44be-a8d5-3fb1ca26fecf" />
- Discuss the parameters (body of request) and return type (jasonify) of the function.<br>
<img width="959" alt="Image" src="https://github.com/user-attachments/assets/685c25f4-faa4-4d78-82cc-5edfbe3377a1" />

## Input/Output requests.  Demo ways to Input to your full stack feature.
- Using frontend show  API request and  present API response. (live demo) <br>
<img width="905" alt="Image" src="https://github.com/user-attachments/assets/b543a261-61fb-4416-8822-b89155e5880d" />
- Using postman to show raw API request and RESTful response (error code(s) and JSON) <br>
<img width="915" alt="Image" src="https://github.com/user-attachments/assets/64d22dc5-024f-46cb-b89b-6963bd830ed8" /> <br> <img width="490" alt="Image" src="https://github.com/user-attachments/assets/65008af0-bbcf-41f1-8bbb-7ba4691e8a05" /> <br>  <img width="473" alt="Image" src="https://github.com/user-attachments/assets/1b3cfb4d-197b-49ff-855f-3e479fd49c83" />
- Using db_init, db_restore, db_backup to show tester data creation and data recovery. <br>
<img width="745" alt="Image" src="https://github.com/user-attachments/assets/f0e0110c-dc79-4a01-84c4-ba29a1945a80" /> <br> <img width="731" alt="Image" src="https://github.com/user-attachments/assets/367146db-2717-4b1a-8797-4e7ad6d042b6" />

---

## 📝 Reflections

I was motivated to make the posts save on the website so the posts could be refered back to and expanded upon, creating a platform for a community to form. 

---