<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.js"></script>
<script>
let maxDistance;
let distances = [];
let spacer = 25;
let speed = 2;
let xpos = 160;
let dotS = 255;

function setup() {
  createCanvas(300, 200);
  
  maxDistance = dist(width/2, height/2, width, height);
  for(let x =  0; x < width; x++){
    distances[x] = [];
    for(let y = 0; y < height; y++){
      let distance = dist(width/2, height/2, x, y);
      distances[x][y] = (distance / maxDistance) * 255;
    }
  }
}

function draw() {
  background(180,20,100);
  strokeWeight(3);
  
  for(let x = 0; x < width; x += spacer){
    for(let y = 0; y < height; y += spacer){
      stroke(dotS);
      ellipse(x + spacer/2, y + spacer/2, 2, 2);
    }
  }
  textSize(36);
  stroke(255);
  text("welcome", xpos -= speed, 150);
  if(xpos == 0 || xpos == 160){
    speed *= -1;
  }
}

function mouseClicked(){
  if(dotS === 255) { dotS = 0; noLoop(); }
  else{ dotS = 255; loop(); }
}
</script>
</head>
<body>
<main></main>
<hr/>
<h5>Please enjoy this humble welcome graphic.</h5>
<p>Something may happen if you click it!</p>
</body>
</html>