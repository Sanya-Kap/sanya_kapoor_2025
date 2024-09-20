<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Three Buttons</title>
    <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 50px;
        }
        .button-container a {
            padding: 15px 30px;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .button-container a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="button-container">
        <a href="{{site.baseurl}}/navigation/cookieclicker.html/index">Cookie Clicker</a>
        <a href="{{site.baseurl}}/navigation/calculator.html/index">Calculator</a>
        <a href="{{site.baseurl}}/navigation/othergame.html/index">Tic Tac Toe</a>
    </div>

</body>
</html>






<html>
    <body>
        <h1>Cookie Clicker</h1>
        <img src="{{site.baseurl}}/images/cookieclicker.png" alt="Cookie"
    width="350"
    height="350"
    onclick = "increment()"/>
        <p>Cookies Clicked: <span id = "counter">0</span></p>
        <audio id="clickSound">
            <source src="{{site.baseurl}}/images/CookieSound.mp3"  type="audio/mpeg">
        </audio>
    <body>
    <script>
        var clicks = 0;
        var sound = document.getElementById("clickSound");
        function increment(){
            clicks = clicks +1;
            counter.innerHTML = clicks;
            sound.play();
        }
    </script>
    <style>
        body{
                background-color: white;
                color: brown;
            }
        #counter{
            color: red;
        }
    </style>
