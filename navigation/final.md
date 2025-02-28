def format_achievements(filename):
    md_content = """
# 🌟 **Achievements This Trimester** 🌟

## 🎯 **My Top 5 Accomplishments**

---

### 🥇 **Achievement 1:**
📌 *Describe your first major accomplishment in detail.*

---

### 🥈 **Achievement 2:**
📌 *Describe your second major accomplishment in detail.*

---

### 🥉 **Achievement 3:**
📌 *Describe your third major accomplishment in detail.*

---

### 🎖️ **Achievement 4:**
📌 *Describe your fourth major accomplishment in detail.*

---

### 🎖️ **Achievement 5:**
📌 *Big Idea 4 Poster.*

<img src="{{site.baseurl}}/images/terms.png" alt="Review"
    width="1000"
    height="400" />  

<img src="{{site.baseurl}}/images/terms.png" alt="Review"
    width="1000"
    height="400" />  

📌 I designed a detailed and visually appealing poster for Big Idea 4. The poster highlighted key definitions and real-world applications that aligns with what we built in class. This helped my understanding as putting the diagram together helped me piece together the different parts of the internet protocal. I learned how data is transfered through smaller packets and how computers communicate along the network. Having a visual summary helped my classmates engage with the material beyond classroom work and lectures.Some students learn better visually, and my poster provided an alternative method to absorb the information. 
---

## ✨ **Reflection** ✨
📌 *Write a comprehensive reflection on your achievements. Discuss what you learned, challenges you faced, and how you grew.*

---

## 🚀 **Goals for Next Trimester** 🚀
📌 *Outline your goals and strategies for improvement moving forward.*
"""
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(md_content)
    
    print(f"Formatted achievements section written to {filename}")

# Usage
format_achievements("achievements.md")
