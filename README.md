# simple_shoot_em_up
A simple scrolling shoot 'em up game made with pygame using starter code from this source: https://125summer.tech/pygame

# How to install

### Installing python and pip
<p> To install the required libraries, you need python: https://www.python.org/downloads/ <br>
Additionally, you must install pip: https://pip.pypa.io/en/stable/installing/
</p>

### Installing required libraries
<p> Using the command line, run the following command <br> (if you have python3, then you may have to type pip3 instead of pip):

`$ pip install pygame`

</p>
  
# Running the program
<p> Download the files in this repository and place all of them in their own directory. To run the program, simply navigate to the directory where the files from this repository are located, and use python to run game.py like so (if you have python3, simply change python to python3):

`$ python game.py`
</p>

# How to Play
<p> The game begins immediately upon starting the program (there is no menu). The objective of the game is to manuever your ship to dodge enemy UFOs for as long as possible. Your ship can take 5 hits before it is destroyed, causing a game over. The longer you survive, the higher your score will be. Your score and lives are displayed in the upper-left corner of the screen like so: </p>

![image](https://user-images.githubusercontent.com/85647626/124369791-5e653300-dc35-11eb-94ac-c81840ecf2cc.png)

<p> Enemies will spawn at increasingly short intervals and will move in straight patterns diagonally, left, right, or down. Enemies will only spawn from the top, left, and right walls, so use this to your advantage to survive for as long as possible!
</p>


## Controls
| Key | Action |
| ------- | --------|
| `w` | Move up |
| `a` | Move left |
| `s` | Move right |
| `d` | Move down |
| 'SPACE' | Quit game (at the game over screen)


## Sprite/Background sources:
I only took images that had creative commons licenses. Here are their sources.

Background: https://gamedevelopment.tutsplus.com/tutorials/create-a-simple-space-shooter-game-in-html5-with-easeljs--active-10944 <br>
Spaceship sprite: Made by me in pixelformer <br>
UFO sprite: https://pixabay.com/illustrations/ufo-pixel-art-flying-saucer-aliens-3628773/

