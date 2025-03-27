---
layout: base
title: Student Home 
description: Home Page
hide: true
image: /images/mario_animation.png
---


**Trimester 3**

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organized Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        .section {
            border: 1px solid #ddd;
            margin-bottom: 10px;
            border-radius: 5px;
            overflow: hidden;
        }
        .section-title {
            background: #f4f4f4;
            padding: 10px;
            cursor: pointer;
            font-weight: bold;
        }
        .section-content {
            display: none;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h2>Trimester 3</h2>
    <div class="section">
        <div class="section-title">Crowdsourcing</div>
        <div class="section-content">
            <p>Crowdsourcing is a method of collecting help, ideas, or input from a large and varied group of people, typically through online platforms.
            The broader the crowdsourcing effort, the more you go beyond your immediate circle, the better chance you have to reduce Computer Bias.</p>
            <ul>
                <li>Popcorn Hack #1: What are the different types of crowdsourcing, and how do they contribute to innovation? Provide a brief description of each type:
                    <ul>
                        <li><strong>Crowdfunding</strong> - Raising money by collecting small contributions from a large group of people.</li>
                        <li><strong>Crowd Creation</strong> - Gathering creative input from a crowd, often for content generation or design.</li>
                        <li><strong>Crowd Voting</strong> - Collecting public opinion or feedback to make decisions or rank options.</li>
                        <li><strong>Crowd Wisdom</strong> - Using collective intelligence for decision-making or problem-solving.</li>
                    </ul>
                </li>
                <li>Data Crowdsourcing & Open Source Development</li>
                <li>Distributed Computing
                Data Crowdsourcing: Data crowdsourcing is a method of collecting data from a large group of people, typically through online platforms.
                <br>
  - Data creates Quick data collection, Diverse input, Cost-effective, and Scalability.
  <br>
- Open Source Development: Open source development is a way of building software where the code is shared openly with the public. 
  - This means anyone can view, use, improve, and share the code.
  - It can be hard to manage lots of different contributors.
  - Project leaders can get overwhelmed and it can also be unreliable (maintainer burnout).
  - It’s important to follow legal rules about using and sharing code (licenses).
- What is data crowdsourcing, and how does it contribute to open-source development?
  - Data crowdsourcing is the process of collecting and compiling large amounts of data from a distributed group of individuals, often through online platforms.
  - An example is wikipedia which is an online information platform for knowledge. 
- Distributed Computing:
  - Distributed computing involves a system of multiple computers working together over a network to solve a problem or complete a task. These systems share resources, such as processing power, storage, and data, to achieve a common goal.
  <br> 
  <br>
- Popcorn Hack: How does distributed computing contribute to innovations through crowdsourcing?
  - Distributed computing refers to a system where computing tasks are spread across multiple networked devices, allowing large-scale processing of complex problems. When combined with crowdsourcing, it enables significant innovations by leveraging the collective power of volunteers’ devices to solve scientific, medical, and technological challenges.</li>
            </ul>
        </div>
    </div>
    <div class="section">
        <div class="section-title">Beneficial and Harmful Effects</div>
        <div class="section-content">
            <p>AI is a new technology that has crated a lot of controversy. It has lead to a great increase in eficiency and automation so people can have more specialized jobs. It has also lead to quick diagnoses and information in the vast arrary of medical implications. However there is a lot of job displacement. Though AI is taking over some jobs that are repetitive and don’t require personalization, many new jobs are being introduced. Since job displacement is invesitable, I think AI is more benifiical than harmful. However, environmentally there is a major impact on global warming. therefore, I think that while AI can result in more benifits, it should be limited in use..</p>
        </div>
    </div>
    <div class="section">
        <div class="section-title">Computing Bias</div>
        <div class="section-content">
            <p>Notes:
Computing bias occurs when computer programs, algorithms, or systems produce results that unfairly favor or disadvantage certain groups.
Creates flawed data and outputs
Happens because of Unrepresentative or Incomplete Data, Flawed or Biased Data, and Data Collection & Labeling (Human annotators may introduce biases due to different cultural or personal biases during the data labeling process).
Explicit data: Data that the user or programmer directly provides.
Implicit data: Data that is inferred from the user’s actions or behavior, not directly provided.
Implicit Data can lead to reinforcing bias by suggesting content based on past behavior, potentially limiting diversity and preventing users from discovering new genres.
Explicit Data is generally more accurate but can still be biased if user input is limited or influenced by the design of the platform.
Algorithmic bias is bias generated from a repeatable but faulty computer system that produces inaccurate results.
ex: AI analyzing resumes to filter them out. Finds that some key words are used more my a specific ethniticity which makes them biased in the data.
Data bias occurs when the data itself includes bias caused by incomplete or erroneous informations.</p>
            <ul>
                <li>HW: Explain the difference between implicit and explicit data. Provide an example of each:
Explicit data is where a user or system directly provides data. Implicit data is when data is not directly provided but is inferred from other information. An example of explicit data is a user inputting their name, gender, and age when signing up for Netflix. Implicit data is a suggestion Netflix gives a user based on their previous watches.</li>
            </ul>
        </div>
    </div>
    <div class="section">
        <div class="section-title">Digital Divide</div>
        <div class="section-content">
            <p>The digital divide refers to the gap between those who have easy access to digital technology and those who do not, impacting education, employment, and innovation opportunities.</p>
            <p>• POPCORN HACK #1: Identify one area (e.g., education, employment, healthcare, or community participation) where you’ve seen the digital divide in action. How does it affect people in different socioeconomic backgrounds?
            <br> One clear example of the digital divide is in education. Students from lower-income backgrounds often lack access to high-speed internet, personal computers, or even a quiet space to study. This makes it harder for them to complete online assignments, attend virtual classes, or access digital learning resources. In contrast, students from wealthier families usually have access to multiple devices, reliable internet, and additional learning tools like online tutoring or educational subscriptions. This gap creates unequal learning opportunities, making it more difficult for underprivileged students to keep up with their peers, ultimately affecting their academic performance and future career prospects.
            <br>
            POPCORN HACK #2: Voice assistants like Siri or Alexa can unintentionally exclude people with strong accents or speech impairments. This happens because these systems are trained mostly on standard speech patterns, making them less accurate for diverse voices.</p>
        </div>
    </div>
    <script>
        document.querySelectorAll('.section-title').forEach(title => {
            title.addEventListener('click', function() {
                const content = this.nextElementSibling;
                content.style.display = content.style.display === 'block' ? 'none' : 'block';
            });
        });
    </script>
</body>
</html>


<Br>

Crowdsourcing:
- Crowdsourcing is a method of collecting help, ideas, or input from a large and varied group of people, typically through online platforms. 
- The broader the crowdsourcing effort, the more you go beyond your immediate circle, the better chance you have to reduce Computer Bias.
- Popcorn Hack #1: What are the different types of crowdsourcing, and how do they contribute to innovation? Provide a brief description of each type:
1. Crowdfunding - Raising money by collecting small contributions from a large group of people.
2. Crowd Creation -  Gathering creative input from a crowd, often for content generation or design.
3. Crowd Voting -  Collecting public opinion or feedback to make decisions or rank options.
4. Crowd Wisdom - Using collective intelligence for decision-making or problem-solving.
- Data Crowdsourcing: Data crowdsourcing is a method of collecting data from a large group of people, typically through online platforms.
  - Data creates Quick data collection, Diverse input, Cost-effective, and Scalability.
- Open Source Development: Open source development is a way of building software where the code is shared openly with the public. 
  - This means anyone can view, use, improve, and share the code.
  - It can be hard to manage lots of different contributors.
  - Project leaders can get overwhelmed and it can also be unreliable (maintainer burnout).
  - It’s important to follow legal rules about using and sharing code (licenses).
- What is data crowdsourcing, and how does it contribute to open-source development?
  - Data crowdsourcing is the process of collecting and compiling large amounts of data from a distributed group of individuals, often through online platforms.
  - An example is wikipedia which is an online information platform for knowledge. 
- Distributed Computing:
  - Distributed computing involves a system of multiple computers working together over a network to solve a problem or complete a task. These systems share resources, such as processing power, storage, and data, to achieve a common goal.
- Popcorn Hack: How does distributed computing contribute to innovations through crowdsourcing?
  - Distributed computing refers to a system where computing tasks are spread across multiple networked devices, allowing large-scale processing of complex problems. When combined with crowdsourcing, it enables significant innovations by leveraging the collective power of volunteers’ devices to solve scientific, medical, and technological challenges.

<br>
Benificial and Harmful effects HW:
<br>
AI is a new technology that has crated a lot of controversy. It has lead to a great increase in eficiency and automation so people can have more specialized jobs. It has also lead to quick diagnoses and information in the vast arrary of medical implications. However there is a lot of job displacement. Though AI is taking over some jobs that are repetitive and don't require personalization, many new jobs are being introduced. Since job displacement is invesitable, I think AI is more benifiical than harmful. However, environmentally there is a major impact on global warming. therefore, I think that while AI can result in more benifits, it should be limited in use. 
<br>
<br>
Computing Bias:
<Br>
Notes:
- Computing bias occurs when computer programs, algorithms, or systems produce results that unfairly favor or disadvantage certain groups. 
- Creates flawed data and outputs 
- Happens because of Unrepresentative or Incomplete Data, Flawed or Biased Data, and Data Collection & Labeling (Human annotators may introduce biases due to different cultural or personal biases during the data labeling process).
- Explicit data: Data that the user or programmer directly provides.
- Implicit data: Data that is inferred from the user’s actions or behavior, not directly provided.
- Implicit Data can lead to reinforcing bias by suggesting content based on past behavior, potentially limiting diversity and preventing users from discovering new genres.
- Explicit Data is generally more accurate but can still be biased if user input is limited or influenced by the design of the platform.
- Algorithmic bias is bias generated from a repeatable but faulty computer system that produces inaccurate results.
  - ex: AI analyzing resumes to filter them out. Finds that some key words are used more my a specific ethniticity which makes them biased in the data.
- Data bias occurs when the data itself includes bias caused by incomplete or erroneous informations 
<br>
HW: 
Explain the difference between implicit and explicit data. Provide an example of each:
<br>
Explicit data is where a user or system directly provides data. Implicit data is when data is not directly provided but is inferred from other information. An example of explicit data is a user inputting their name, gender, and age when signing up for Netflix. Implicit data is a suggestion Netflix gives a user based on their previous watches. 



<div class="Games.md">
  <a href="{{site.baseurl}}/navigation/Games/index">
  <button>Games 🎮 </button>
</a>

<div class="Games.md">
  <a href="{{site.baseurl}}/navigation/Hacks/index">
  <button>Hacks </button>
</a>

<div class="Sprint5.md">
  <a href="{{site.baseurl}}/navigation/Sprint5/index">
  <button>Sprint 5 Review </button>
</a>

<div class="BigIdea4.md">
  <a href="{{site.baseurl}}/navigation/BigIdea4/index">
  <button>Big Idea 4 </button>
</a>

<div class="final.md">
  <a href="{{site.baseurl}}/navigation/final/index">
  <button>final </button>
</a>

<div class="2020MC.md">
  <a href="{{site.baseurl}}/navigation/2020MC/index">
  <button>2020 MC </button>
</a>

<div class="CPTNTM.md">
  <a href="{{site.baseurl}}/navigation/CPTNTM/index">
  <button>CPT & NTM </button>
</a>











<!--- Concatenation of site URL to frontmatter image  --->
{% assign sprite_file = site.baseurl | append: page.image %}
<!--- Has is a list variable containing mario metadata for sprite --->
{% assign hash = site.data.mario_metadata %}  
<!--- Size width/height of Sprit images --->
{% assign pixels = 256 %}

<!--- HTML for page contains <p> tag named "Mario" and class properties for a "sprite"  -->

<p id="mario" class="sprite"></p>
  
<!--- Embedded Cascading Style Sheet (CSS) rules, 
        define how HTML elements look 
--->
<style>

  /*CSS style rules for the id and class of the sprite...
  */
  .sprite {
    height: {{pixels}}px;
    width: {{pixels}}px;
    background-image: url('{{sprite_file}}');
    background-repeat: no-repeat;
  }

  /*background position of sprite element
  */
  #mario {
    background-position: calc({{animations[0].col}} * {{pixels}} * -1px) calc({{animations[0].row}} * {{pixels}}* -1px);
  }
</style>

<!--- Embedded executable code--->
<script>
  ////////// convert YML hash to javascript key:value objects /////////

  var mario_metadata = {}; //key, value object
  {% for key in hash %}  
  
  var key = "{{key | first}}"  //key
  var values = {} //values object
  values["row"] = {{key.row}}
  values["col"] = {{key.col}}
  values["frames"] = {{key.frames}}
  mario_metadata[key] = values; //key with values added

  {% endfor %}

  ////////// game object for player /////////

  class Mario {
    constructor(meta_data) {
      this.tID = null;  //capture setInterval() task ID
      this.positionX = 0;  // current position of sprite in X direction
      this.currentSpeed = 0;
      this.marioElement = document.getElementById("mario"); //HTML element of sprite
      this.pixels = {{pixels}}; //pixel offset of images in the sprite, set by liquid constant
      this.interval = 100; //animation time interval
      this.obj = meta_data;
      this.marioElement.style.position = "absolute";
    }

    animate(obj, speed) {
      let frame = 0;
      const row = obj.row * this.pixels;
      this.currentSpeed = speed;

      this.tID = setInterval(() => {
        const col = (frame + obj.col) * this.pixels;
        this.marioElement.style.backgroundPosition = `-${col}px -${row}px`;
        this.marioElement.style.left = `${this.positionX}px`;

        this.positionX += speed;
        frame = (frame + 1) % obj.frames;

        const viewportWidth = window.innerWidth;
        if (this.positionX > viewportWidth - this.pixels) {
          document.documentElement.scrollLeft = this.positionX - viewportWidth + this.pixels;
        }
      }, this.interval);
    }

    startWalking() {
      this.stopAnimate();
      this.animate(this.obj["Walk"], 3);
    }

    startRunning() {
      this.stopAnimate();
      this.animate(this.obj["Run1"], 6);
    }

    startPuffing() {
      this.stopAnimate();
      this.animate(this.obj["Puff"], 0);
    }

    startCheering() {
      this.stopAnimate();
      this.animate(this.obj["Cheer"], 0);
    }

    startFlipping() {
      this.stopAnimate();
      this.animate(this.obj["Flip"], 0);
    }

    startResting() {
      this.stopAnimate();
      this.animate(this.obj["Rest"], 0);
    }

    stopAnimate() {
      clearInterval(this.tID);
    }
  }

  const mario = new Mario(mario_metadata);

  ////////// event control /////////

  window.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
      event.preventDefault();
      if (event.repeat) {
        mario.startCheering();
      } else {
        if (mario.currentSpeed === 0) {
          mario.startWalking();
        } else if (mario.currentSpeed === 3) {
          mario.startRunning();
        }
      }
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      if (event.repeat) {
        mario.stopAnimate();
      } else {
        mario.startPuffing();
      }
    }
  });

  //touch events that enable animations
  window.addEventListener("touchstart", (event) => {
    event.preventDefault(); // prevent default browser action
    if (event.touches[0].clientX > window.innerWidth / 2) {
      // move right
      if (currentSpeed === 0) { // if at rest, go to walking
        mario.startWalking();
      } else if (currentSpeed === 3) { // if walking, go to running
        mario.startRunning();
      }
    } else {
      // move left
      mario.startPuffing();
    }
  });

  //stop animation on window blur
  window.addEventListener("blur", () => {
    mario.stopAnimate();
  });

  //start animation on window focus
  window.addEventListener("focus", () => {
     mario.startFlipping();
  });

  //start animation on page load or page refresh
  document.addEventListener("DOMContentLoaded", () => {
    // adjust sprite size for high pixel density devices
    const scale = window.devicePixelRatio;
    const sprite = document.querySelector(".sprite");
    sprite.style.transform = `scale(${0.2 * scale})`;
    mario.startResting();
  });

</script>

<body style="background-color:powderblue;">

<style>
  .border_tomato {
    border-width: 5px;
    border-style:solid;
    border-radius: 30px;
  }
  </style>
<html lang="en">
<div class="border_tomato">
      <p class="solid"> </p>
      <p style="color: green;">
          Cookie Instructions: Chocolate chip cookies are a timeless favorite, known for their soft, chewy texture and sweet, buttery flavor. Studded with rich, melty chocolate chips, they offer a delightful contrast between the slightly crisp edges and the gooey center. They’re a classic dessert that never goes out of style.
    </p>
  <button style="color:yellow; font-family:monospace; border-color:blue; background-color:lightgreen;">Button
  </button> 
  <br>
  <br>
  <br>
  <br>
  <br>
  </div>



<style>
  .border_toma {
    border-width: 5px;
    border-style:solid;
    border-radius: 30px;
  }
  </style>
<div class="border_toma">
      <p class="solid"> </p>
      <p style="color: green;"></p>

<a href="https://www.organic-center.org/recipes/ancho-chile-chocolate-cookies-sensient-natural-ingredients?gad_source=1&gclid=Cj0KCQjwiuC2BhDSARIsALOVfBLVTfmtUEc2ZzOrlBRdMd9DbbEF1Fy-5v-q4729sr0iEwZOBE0ZSFEaAhx9EALw_wcB">Chocolate Cookie </a>
<br>
<a href="https://pinchofyum.com/the-best-soft-chocolate-chip-cookies">Classic Chocolate Chip Recipe </a>
<p> Above are two recipies and baking instructions for two types of cookies. For chocolate lovers, this recipe includes cocoa powder in the dough for an extra rich, chocolatey experience. The cookies come out soft and decadent, with an irresistible fudgy taste. Step-by-step guidance on mixing and baking ensures you get perfect cookies every time. For the classic chocolate chip, the recipe offers the perfect balance of crispy edges and a chewy center, made with simple ingredients like butter, sugar, eggs, and semi-sweet chocolate chips. The instructions provide tips on achieving that ideal texture and flavor, including chilling the dough for a more intense cookie. </p>
</div>