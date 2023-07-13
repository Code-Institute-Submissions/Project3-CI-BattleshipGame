<h1>Project Name: Battleship Game</h1>
<h2>1. Purpose of the Project</h2>
<p>The purpose of this project is to create a <em>Battleship game application</em> using Python. The game is played on the mockup terminal of Code Institute on Heroku, where the player will input their name and take turns against the computer, guessing the coordinates to sink each other's battleships. The objective is to be the first player to sink all of their opponent's battleships.</p>
<h2>2. User Stories</h2>
<ul>
  <li>As a user, I want to input my name to start the game.</li>
  <li>As a user, I want to choose the coordinates for my ships.</li>
  <li>As a user, I want to see the location of my ships but not the computer's ships.</li>
  <li>As a user, I want to take turns making guesses to sink the opponent's battleships.</li>
  <li>As a user, I want to be notified of successful hits and misses on the board.</li>
  <li>As a user, I want to receive updated computer guesses after each round.</li>
  <li>As a user, I want input validation to prevent repeating the same coordinates and to ensure valid inputs within the specified range.</li>
</ul>
<h2>3. Features</h2>
<ul>
  <li>User can input their name to start the game.</li>
  
  ![1](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/56cf2477-9275-4adb-ba15-7a02b3943a65)

  <li>User can choose the coordinates for their ships.</li>
  
  ![2](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/b0ef01ff-8a37-4e27-929d-13f779a2093b)

  <li>Computer generates random coordinates for its ships.</li>
  
  ![3](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/5d51c9f9-b40e-4e1e-b537-0d5a0caffd6c)

  <li>User can see the location of their ships on the board.</li>
  
  <li>User can make guesses by inputting coordinates.</li>
  
  <li>User's guesses are marked on the board with appropriate symbols.</li>
  
  <li>User is notified of successful hits and misses.</li>
  
  <li>Computer's guesses are updated after each round.</li>



  
  <li>Input validation prevents repeating the same coordinates.</li>



  
  <li>Input validation ensures valid inputs within the specified range.</li>



  
</ul>
<h2>4. Future Features</h2>
<p>In the future, the following features could be added to enhance the game:</p>
<ul>
  <li>Add different game modes with varying difficulty levels.</li>
  <li>Include sound effects and animations to enhance the gaming experience.</li>
  <li>Implement a multiplayer mode to allow users to play against each other online.</li>
</ul>
<h2>5. Technology</h2>
<p> What was used to realize this project: <br>
•  Python <br>
•  GitHub <br>
•  CodeAnywhere <br>
•  Heroku <br>
</p>
    
 

<h2>6 Testing</h2>
<h3>6.1 Code Validation</h3>
<p>This project was validated using the <strong>Code Institute's PEP8 Python Validator</strong>.</p>

![7](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/6101dce3-56d2-4275-90bb-52800d12c099)

<h3>6.2 Test Cases (User Story Based with Screenshots)</h3>
<ol>
  <li>
    <h4>Test Case: User Input Validation</h4>
    <p>Steps:</p>
    <ol>
      <li>User enters the same coordinates multiple times.</li>
      <li>User enters coordinates outside the specified range.</li>
    </ol>
    <p>Expected Result: Error messages are displayed, preventing invalid inputs.</p>
    <p><em>Screenshot:</em></p>
    
![5](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/5169b0a6-4781-4fab-abae-4a7a1b4279a6)

![6](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/d0669774-dd39-4c0e-aa18-04e56cd02ccc)
  </li>
  <li>
    <h4>Test Case: Successful Hit</h4>
    <p>Steps:</p>
    <ol>
      <li>User enters coordinates of a ship.</li>
      <li>User's guess hits the opponent's ship.</li>
    </ol>
    <p>Expected Result: The board displays a successful hit marker: <strong>"@"</strong></p>
    <p><em>Screenshot:</em></p>
 
  ![4](https://github.com/AEmin96/Project3-CI-BattleshipGame/assets/126208272/642fac03-0159-43e0-8b58-d0da01a1b3aa)
    
  </li>
</ol>
<h3>8.3 Fixed Bugs</h3>
<p><strong>Bug:</strong> User could input the same coordinates repeatedly.</p>
<p><strong>Fix:</strong> Implemented verification to prevent the user from repeating the same coordinates.</p>
<h3>8.4 Supported Screens and Browsers</h3>
<p>The Battleship game will be played on a terminal interface and does not require specific screen sizes or browser support.</p>
<h2>9. Deployment</h2>

<h3>9.1 CodeAnywhere</h3>
<ol>
  <li>Installed CodeAnywhere browser extension.</li>
  <li>Opened the project repository in CodeAnywhere</li>
  <li>Wrote the code</li>
  <li>Tested the deployed application in CodeAnywhere's browser preview.</li>
</ol>
<h3>9.2 Heroku </h3>
<ol>
  <li>Created a new Heroku App</li>
  <li>Set up the buildbacks to Python and NodeJS</li>
  <li>Linked the Heroku app to the repository</li>
  <li>Clicked on Deploy</li>

</ol>
<h2>10. Credits</h2>
<p>This project was inspired by Code Institute's ULTIMATE Battleship Game</p>
