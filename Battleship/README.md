# How to play : 

1. Every team is required to submit a single python file

2. The program should have a `class BattleShip` with the following member variables
    *   `team_name: str` - Name of your team
    *   `ships : list(list(int))` - 2D list called ships, indicating the position of your ships
    *   `opponent_board : list(int) `- 2D list for tracking enemy ships
    *   `info : int` - Contains details about your attack.

3. Member Functions :
    * `set_ships(self)` - Returns your 2D list of your ships
    * `attack(self)` - Return a tuple of two integers. The two integers denotes the position of the board where you want to shoot.

    * `hit_or_miss(self, x, y , info)` - Doesn't return anything.
      x and y is the co-ordinate at which you hit the enemy board. `info` contains information about the state of your attack.
      * If info = 1 , it means you have missed your shot.
      * If info = 0 , it means you have hit an enemy ship
      * If info = -1 , it means you have attempted to shoot at a place outside the dimensions of the enemy board
      * If info = 2, it means you have availed `Nullify` special Shot (More on Special Shot later)
      * If info = 3, it means you have availed `Missile Hawkeye Special Move`!

4.  You may create additional member variables/global variables and functions. But the `above member functions/variables are neccesary`.

5.  You are **not allowed** to import any third party libraries or import from the main game file. You can only use libraries found in Vanilla Python. 

6. Special Moves : 

    In your opponent's board, two randomly selected tile/co-ordinates will be assigned with special spot. The special spot are always in one of the ships. So, when you hit this special part of the ship, you get to use one of the following special moves : 

    *   `Nullify` : Pretty Self Explanatory. It nullifies your opponent's next chance and hence gives you double hit.

    *   `Missile Hawkeye` : When you activate the missile hawkeye, the next time you hit any co-ordinate say (x,y) , you get to eliminate the entire row and column (sort of like a plus symbol).

    Note : When you activate missile Hawkeye, the very next move is treated as your special attack.

7. The board is a 2D matrix of 1s and 0s. 

    How to Set Up Your Ships : 
    * There are 5 ships. One of size 3, two of size 4 , and two of size 5.


    * The presence of a ship is determined by the ship array you have to input. So, 
    ```
    ships = [
		[3, 3, 3, 1],
		[4, 3, 4, 0],
		[5, 8, 4, 0],
		[1, 1, 5, 1],
		[9, 1, 5, 1]
    ]
    ```
    means there are 5 ships.
    The first two parameters represent the row and column numbers of the first tile of the ship, respectively.
    The third parameter represents the size of the ship.
    Lastly, the last parameter represents the orientation of the ship, 0 is for vertical and 1 is for horizontal (the tiles get added towards the right (horizontal) or towards the bottom (vertical)).
    * The ships cannot be placed diagonally, but can be placed horizontally and Vertically only. Note that the ships cannot overlap!


8. The following link redirects you to a sample code that every team is expected to submit. Check out the valid board settings! [Click here for 1st example code](https://github.com/MU-Enigma/BattleShip-BattleGround/blob/master/Battleship/example_submission/team1.py). [Click here for 2nd example code](https://github.com/MU-Enigma/BattleShip-BattleGround/blob/master/Battleship/example_submission/team2.py). 
You may use the same as a boiler plate for your code submission.


9. Know more about the classic [BattleShip Game](https://www.youtube.com/watch?v=RY4nAyRgkLo)

10. For any other queries or questions, team of Enigma is always available on discord. See Contact Info below.
