Game Overview:

The game is a shooter game where you control a tank and shoot red targets. 
In the game the player can drive the tank around the screen and can run over the red targets to gain points. The player will also be able to shoot a stream of bullets from a machine gun on the front of the tank. The player will also be able to control the main turret on top of the tank and fire shells from that turret. If either the bullets or the shells hit a target then you gain points. The goal of the game is to hit as many of the red targets in 30 seconds. 

List of assets:

Tank
Turret
Bullet
Shell
Target
TargetsHitLabel
TimerLabel

Sprite Details:

Tank:
Visual Elements: The base of a tank from top-down view
Life span: It is born when the game begins and will last until the game ends after 30 seconds
Movement: It moves under user control of the arrow keys. It uses force based movement so you can drift and carry momentum. It can move forward or backwards and can turn left or right.
Boundary behavior: When it leaves the screen it wraps
Collision behavior - It can collide with the red targets. If it collides with a red target then that target is reset and the targets hit counter is incremented by one

Turret:
Visual Elements: The turret of a tank from top-down view
Life span: It is born when the game begins and will last until the games ends after 30 seconds
Movement: It follows the movement of the tank it is attached to. It can independently turn left or right without having to follow the image angle of the tank base.
Boundary behavior: When it leaves the screen it wraps along with the tank base
Collision behavior: No collision behavior

Bullet:
Visual elements: Small yellow rectangle to represent a bullet
Life span: It is born when the player presses the space bar. It will last until either it reaches the boundary or hits a red target. In either case the bullet will hide itself and then respawn when it is its turn in the rotation of bullets
Movement: It goes in a straight line from the front of the tank following what the tanks image angle was at the moment of firing
Boundary behavior: When it leaves the screen it will hide itself
Collision behavior: It collides with the red targets. When it hits a red target the target will reset and the targets hit counter will increment by one. The bullet will also hide itself on collision with the red target.

Shell:
Visual elements: Small white rectangle to represent a tank shell
Life span: It is born when the player presses the “e” key. It will last until either it reaches the boundary or hits a red target. In either case the shell will hide itself and then respawn it is its turn in the rotation of shells
Movement: It goes in a straight line from the direction that the turret is pointing at the moment of firing
Boundary behavior: When it leaves the screen it will hide itself
Collision behavior. It collides with the red targets. When it hits a red target the target will reset and the targets hit counter will increment by one. The shell will also hide itself on collision with the red target

GUI Labels:
There will be a couple of labels involved.

During the gameplay there will be a label for the targets hit and for the timer of the game. These labels are in classes called TargetsHitLabel and TimerLabel respectively. They are instantiated and updated during gameplay. The TargetsHitLabel will update whenever the tank, bullet, or shell sprite collides with a red target and will increment by one. The TimerLabel consistently updates itself as the timer counts down.

When the game is first launched and before the beginning of the game. There will be a label for the instructions of the game. This is a multi label with the title of the game and instructions to begin. This label is created during the instantiation of the start screen.

When the game is finished there is a game finished screen that has a label that displays the final score you got during the game. This label is created when the game finished screen is displayed and updated with the score of the most recent game played

Other GUI elements:

playAgainButton: A button with the text “Play Again!” If pressed it will bring the player back to the start screen allowing them to replay the game

quitButton: A button with the text “Quit :(“ If pressed it will exit the program

On the start screen if the player clicks their mouse then the gameplay will begin and it will go to the Game screen.

Game class initialization: 

Appearance: It will be an all grey background. 

Sprites: 
All the sprites will be initialized as the game starts. 
There is a list of bullets and shells and these are all hidden to begin. 
The red targets are also in a list and will be displayed randomly across the board constantly resetting to different positions as they are taken out by the player. 
The tank and turret will spawn in together in the upper left section of the map

GUI elements:
There are two labels that appear the TargetsHitLabel and TimerLabel. These are both initialized along with the sprites when the game begins. The targets hit will appear in the upper left corner and the timer will appear in the upper right corner.

Other assets: 
There is the timer which countdown from 30 and constantly updates until the end of the game in which the game is terminated
There is also the targets hit counter which is updated every time that the tank, bullet, and shell collide with a red target

Game class behavior:
Collision management: 
Every frame the game checks if the tank, a bullet, or a shell has collided with a red target. If it does it will reset the target, hide the bullet or shell if that is what collided, and increment the targets hit counter

Score and timing updates: 
Every frame the game updates the timer with how much longer is left and when it reaches 0 it terminates.
Every frame the game checks collisions and when a collision occurs the score is incremented by one

GUI updates:
Only updates that occur is the changing positions of the sprites and the two labels as they are updated during the game.

Game end and or other state conditions:
The game only ends when the timer runs out

Asset list -

Tank Green Base Idle.png
Tank Green Turret Idle.png

Both found in a package found on the following link: https://gherzog.itch.io/top-down-tank

Milestones:
Creation of the tank and making it move
Creation of the turret and making it move
Creation of the bullet and allowing it to fire from the front of the tank
Ability to fire multiple bullets at the same time
Creation of the shell and allowing it to fire from the turret
Ability to fire multiple shells at the same time
Have randomly spawning red targets that the tank, bullets, and shells can collide with
Handle the collisions so that the targets reset and bullets and shells hide themselves
Add in the targets hit counter that will update whenever a collision occurs
Add in a timer that will count down and terminate the game when the timer reaches 0
Create a start screen that explains how the game works and gives the game title
Create an end screen that shows the final score and allows the player to play the game again or exit
This is where I would be happy to submit the game
Add in animations for the turret firing
Add in changing what the shell looks like depending what direction the tank is firing from. Potentially changing the shell to a png
Add in drag to the driving of the tank to limit its speed
Add in sound effects for hitting targets, firing the turret or gun, and moving the tank

Multi-state considerations:
There are 3 different states. The start screen, the game, and the game finished screen
Start screen when the mouse is clicked will start the game
When the game is terminated following the timer ending then the game finished screen will appear
If the player clicks the play again button then it will be brought back to the Start Screen
If the player clicks the quit button then the program terminates





