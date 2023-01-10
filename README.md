# century
### What is this project?
This is project of the game written on python with PyQt5 for GUI.

### Why it was created? / Aim of project
After finishing some courses I've decicded to challenge myself to make simething more complicated than blackjack or some other simplified card game.
For this reason I've looked at my board games and decide to try recreate one of them.

I was needed some GUI, game logic, images etc. After quick research I've found PyQt library and dediced to give it a shot - entire project is 
about implementing game https://boardgamegeek.com/boardgame/209685/century-spice-road into playable computer version.

### State of project
The game is now playable for single player and it is possible do finish it
 - It was developed until all type of cards are implemented, 
 - all mechanic like card buying, card playing, resting (to get used cards back),
 - Resources/points are tracked and displayed
 - GUI to interact with game works
 - History (and any other informations) are displayed correctly
 - Record (fastes game finish) is saved
 - Trading resources and buying treasures works
 - Game can be finished
 
 WHAT IS NOT IMPLEMENTED:
 Add onboarding/rules explanation
 - I was thinkin about implement tooltips and onboarding for new players, however PyQt was not fun enough to interact with and I've dropped that idea
 
 Multiplayer option wasn't finished
 - it is possible to add more players in config but I've started to develop something else before implement swaping players and it's far from state "finished, tested and ready"
 
 Online connection is not even started
 - there was some idea to work to make it work for play online, but it was aimed to develop AFTER local multiplyer
