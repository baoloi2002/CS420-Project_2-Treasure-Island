There are the following files:
- main.py: The core to implement game rule.
- AgenP.py: The agent.
- MapGenerator.py: Generate a map.
- Visualization.py: Visualize the game to docx.
- MapPaint.py: Help Visualization.py to draw map.
- Map.txt: Store the map for the game.
- test.png: The image draw by MapPaint.py .
- log.txt: The steps in the game.
- Visualization.docx: same with log.txt but have a colorfull map to know what happend.

To run the game:
# Normal run the game, Map.txt must have a map in it.
python main.py

# Run the game with the map GENERATOR
python main.py -g "size of the map"
python main.py --Gen "size of the map"
"size of the map" can be any integer greater or equal to 16

Ex:
python main.py -g 32
python main.py --Gen 64

# Run the game with the map in another file, copy to the Map.txt
python main.py -m "name of that file"
python main.py --Map "name of that file"

Ex:
python main.py -m Map5.txt
python main.py --Map Map1.txt
