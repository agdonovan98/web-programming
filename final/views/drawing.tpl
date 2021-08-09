<!-- design made with p5.js -->
<html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.js"></script>
        <script>
            const Y_AXIS = 1;
            const X_AXIS = 2;
            let b1, b2, c1, c2;

            let maxDistance;
            let distances = [];
            let spacer = 20;

            function setup() {
            createCanvas(400, 400);
            b1 = color(30);
            b2 = color(200);
            
            maxDistance = dist(width/2, height/2, width, height);
            for(let x = 0; x < width; x++){
                distances[x] = [];
                for(let y= 0; y < height; y++){
                let distance = dist(width/2, height/2, x, y);
                distances[x][y] = (distance / maxDistance) * 255;
                }
            }
            }

            function draw() {
            setGradient(0, 0, width, height, b2, b1, Y_AXIS);
            
            for(let x = 0; x < width; x += spacer){
                for(let y = 0; y < height; y += spacer){
                strokeWeight(1);
                stroke(distances[x][y]);
                ellipse(x + spacer/2, y + spacer/2, 1, 1);
                }
            }
            
            strokeWeight(5);
            stroke(100,200,250);
            fill(60,150,250);
            ellipse(width * 0.5, height * 0.6, 250, 250);
            
            textSize(48);
            strokeWeight(3);
            stroke(0, 180, 150);
            fill(0,150,100);
            text("A T L A S", width * 0.25, height * 0.2);
            
            }

            function setGradient(x, y, w, h, c1, c2, axis){
            for(let i = y; i <= y+h; i++){
                let inter = map(i, x, x + w, 0, 1);
                let c = lerpColor(c1, c2, inter);
                stroke(c);
                line(x, i, x + w, i);
            }
            }
        </script>
    </head>
    <body>
        <main></main>
    </body>
</html>