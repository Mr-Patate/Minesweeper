# Minesweeper
A Minesweeper on Python using Tkinter and random

I uploaded 3 versions of Minesweeper.

Minesweeper v1

I decided to start with the following method:

  Each case has reference POSITION, which is between 1 and 100.
  That means, I have only a 1 dimensionnal Array.
  Each case has also a reference NUMBER, which is normally 0
  
  The script put some random number between 1 and 100. The random number is taken as reference POSITION for a case and will become a mine.
  If a case is affected as mine, it becomes a 9 for it's reference NUMBER.
  All neighbour around the mine are incrementing a +1 for it's reference NUMBER.
  
  For each discovered case from the player, the reference NUMBER from the reference POSITION is given.
  
  
Problem:  There is a lot of If statements. There is a lot of conditions and the code is not efficient. 
          Also, the reference POSITION (between 1 and 100) is a really bad idea and i would better have a 2 dimension array. It will make the reference NUMBER affectation much more easier.
I decided to do v2.

Minesweeper v2

 It has now a reference POSITION with 2 dimensional Array
 It still has the same method for mine placing: A random number will affect the reference POSITION
 
 Change: Now, each case calculate it's refence NUMBER by looking to his neighbour:
  For each neighbour, a +1 occurs.
 We might be thinking that the calculation time is now bigger. But it is a pre-function for the v3

Problem:  The effiency of code calculation is bad. I can do better

Minesweeper v3

  Change: only clicked case is calculated. This inproves the programm efficiency: only what we need to see is calculated.
  I have also less stored data because of the direct live calculation.
  
 

I hope this project would be usefull for you.
I am sure the Minesweeper can be a lot more improved.
If you have some recommandations or ameliorations, feel free to propose :)
