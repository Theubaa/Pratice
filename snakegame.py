const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const scoreElement = document.getElementById("score");

const box = 10;
let snake = [
    { x: 100, y: 50 },
    { x: 90, y: 50 },
    { x: 80, y: 50 },
    { x: 70, y: 50 }
];

let direction = "RIGHT";
let fruit = spawnFruit();
let score = 0;

document.addEventListener("keydown", changeDirection);

function changeDirection(event) {
    const key = event.keyCode;
    if (key === 37 && direction !== "RIGHT") direction = "LEFT";
    if (key === 38 && direction !== "DOWN") direction = "UP";
    if (key === 39 && direction !== "LEFT") direction = "RIGHT";
    if (key === 40 && direction !== "UP") direction = "DOWN";
}

function spawnFruit() {
    return {
        x: Math.floor(Math.random() * (canvas.width / box)) * box,
        y: Math.floor(Math.random() * (canvas.height / box)) * box
    };
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw snake
    ctx.fillStyle = "green";
    snake.forEach(segment => {
        ctx.fillRect(segment.x, segment.y, box, box);
    });

    // Draw fruit
    ctx.fillStyle = "white";
    ctx.fillRect(fruit.x, fruit.y, box, box);

    // Move snake
    const head = { ...snake[0] };
    if (direction === "UP") head.y -= box;
    if (direction === "DOWN") head.y += box;
    if (direction === "LEFT") head.x -= box;
    if (direction === "RIGHT") head.x += box;

    // Game over conditions
    if (
        head.x < 0 || head.x >= canvas.width ||
        head.y < 0 || head.y >= canvas.height ||
        snake.some(segment => segment.x === head.x && segment.y === head.y)
    ) {
        alert("Game Over! Your Score is: " + score);
        document.location.reload();
        return;
    }

    snake.unshift(head);

    // Eating the fruit
    if (head.x === fruit.x && head.y === fruit.y) {
        score += 10;
        fruit = spawnFruit();
    } else {
        snake.pop();
    }

    // Update score
    scoreElement.textContent = "Score: " + score;
}

setInterval(draw, 100); // game speed
