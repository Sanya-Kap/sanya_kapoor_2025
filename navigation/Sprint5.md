
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


## 📝 Reflections

I was motivated to make the posts save on the website so the posts could be refered back to and expanded upon, creating a platform for a community to form. 

---