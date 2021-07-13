<html>
    <head>
    %include header
        <style>
            #myHeader{
                background-color: dodgerblue;
                width: 500px;
                color: black;
                padding: 20px;
                margin: 20px;
                text-align: center;
                font-family: Helvetica, Arial, sans-serif;
                font-size: 28px;
            }
            #newHeader{
                background-color: tomato;
                width: 500px;
                color: black;
                padding: 20px;
                margin: 20px;
                text-align: center;
                font-family: Helvetica, Arial, sans-serif;
                font-size: 28px;
            }
            .hp{
                width: 500px;
                padding: 10px;
                margin: 20px;
                text-align: center;
                font-family: Helvetica, Arial, sans-serif;
                font-size: 16px;
            }
        </style>
    </head>

    <body>
        %include banner
        <div class="container-fluid">
            <div class="row">
                <div class="col"><h1 id="myHeader"><span class="material-icons md-48">face</span> The Basics</h1>
                    <p class="hp">My name's Austin Donovan! I'm 23 years old and live in Northeast Ohio.</p>
                    <p class="hp">I am a student at Kent State University, but I plan to graduate later this year. I have a major in Computer Science and a minor in Sociology. When I'm not studying, I'm usually at my day job at Giant Eagle.</p>
                    </div>
                <div class="col"><h1 id="myHeader"><span class="material-icons md-48">thumb_up</span> My Hobbies</h1>
                    <p class="hp">In my free time, I like drawing, playing video games and listening to music. I also enjoy talking with my friends online, but since we live in different places around the world, we're rarely all awake at the same time.</p>
                    <p class="hp">I've been looking to get more into creative coding, and as fun as it is, I am not very good at it yet. I've also been getting back into reading lately, so let me know if you have any good books for me!</p>
                    </div>
                <div class="col"><h1 id="myHeader"><span class="material-icons md-48">favorite</span> Favorite Things</h1>
                    <p class="hp">My favorite video game right now is <b>Animal Crossing: New Horizons.</b> Some other games I've been playing a lot are <i>Minecraft</i> and <i>Final Fantasy 9</i>.</p>
                    <p class="hp">My favorite album right now is <b>In Rainbows</b> by Radiohead. I've also been listening to <i>Remain in Light</i> by Talking Heads lately.</p>
                    <img src="/static/images/acnh.jpg" alt="Animal Crossing" height="160" width="160">
                    <img src="/static/images/inrainbows.png" alt="In Rainbows" height="160" width="160">
                    </div>
                </div><br>
                <div class="col"><h1 id="newHeader"><span class="material-icons md-48">done</span> The End</h1>
                    <p class="hp">It seems you've reached the end of this page. <a href="https://www.youtube.com/watch?v=7VORU2tNTxA" target="_blank"><br>Here's a video just for you!</a></p> 
                </div></div><br><br>
        <p><span class="material-icons md-24">schedule</span> This page was last updated on July 13, 2021.</p>
    </body>
</html>