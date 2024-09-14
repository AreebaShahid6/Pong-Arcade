<img width="448" alt="pong" src="https://github.com/user-attachments/assets/f703a807-879e-4882-9efa-ef099787a7ac">

### PONG Game:
This project is a **Pong Game** implemented using Python's **Turtle module**. The game mimics the classic Pong, where two paddles move vertically to hit a bouncing ball. The objective is to prevent the ball from passing the paddle on your side, while trying to score by making the ball pass the opponent's paddle.

### Key Components:
1. **Ball Class**:
   - The `Ball` class defines the ball's behavior, such as its shape, movement, speed, and bouncing mechanics. It contains methods to move the ball, reverse its direction when hitting a paddle or a boundary, and reset its position when a point is scored.

2. **Paddle Class**:
   - The `Paddle` class represents the paddles controlled by the players. Each paddle can move up and down within the game boundaries. Player 1 controls the left paddle using the **W** and **S** keys, while Player 2 controls the right paddle using the **Up** and **Down** arrow keys.

3. **Score Class**:
   - The `Score` class manages the game's scorekeeping system, displaying the scores of both players on the screen. When the ball crosses a boundary (indicating a point scored), the corresponding player's score is updated and displayed.

4. **Game Logic**:
   - The game loop continuously moves the ball and updates the screen based on the ball's position. The ball bounces off the top and bottom boundaries, as well as the paddles, with an increasing speed on every paddle bounce. If the ball crosses the left or right edge of the screen, it resets to the center, and the opposing player earns a point.

### Controls:
- **Left Paddle**: Move using the `W` key to go up and the `S` key to go down.
- **Right Paddle**: Move using the `Up` arrow key to go up and the `Down` arrow key to go down.

### Features:
- **Paddle and Ball Collision**: The ball bounces back when it hits a paddle.
- **Wall Collision**: The ball bounces off the top and bottom boundaries.
- **Scorekeeping**: The game tracks the score for each player, updating it when the ball passes a paddle.
- **Speed Increase**: Each time the ball bounces off a paddle, its speed slightly increases.

This project demonstrates basic object-oriented programming (OOP) principles in Python, such as class inheritance and method overriding, while using the **Turtle graphics library** to build a simple and interactive graphical game.
