---
layout: base
title: Student Home 
description: Home Page
hide: true
image: /images/mario_animation.png
---


**Trimester 3**
<br>
Benificial and Harmful effects HW:
<br>
AI is a new technology that has crated a lot of controversy. It has lead to a great increase in eficiency and automation so people can have more specialized jobs. It has also lead to quick diagnoses and information in the vast arrary of medical implications. However there is a lot of job displacement. Though AI is taking over some jobs that are repetitive and don't require personalization, many new jobs are being introduced. Since job displacement is invesitable, I think AI is more benifiical than harmful. However, environmentally there is a major impact on global warming. therefore, I think that while AI can result in more benifits, it should be limited in use. 


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