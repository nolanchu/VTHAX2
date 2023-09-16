// Get a reference to the canvas element
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

const img1 = new Image();
const img2 = new Image();
const img3 = new Image();

img1.src = 'burger.png';
img2.src = 'meat.png';
img3.src = 'top_bun.png';

function draw_burger(patties=1) {
    ctx.drawImage(img1, canvas.width/2, canvas.height-150, img1.width*.2, img1.height*.2);
    for (var i=1; i<patties; ++i) {
        ctx.drawImage(img2, canvas.width/2, canvas.height-150-50*i, img2.width*.2, img2.height*.2);
        ctx.drawImage(img3, canvas.width/2+8, canvas.height-138-50*i, img3.width*.2, img3.height*.2);
    }

}
img1.onload = function() {
    draw_burger();
}

img3.onload = function() {
    draw_burger(4);
}

