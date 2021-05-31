Meme generator project created as final project of the Udacity Large Codebases with Libraries course.

The project aims at learning code organization with creations of modules, import of 3rd libraries and
coding style.

This project will create meme from quote that can be parsed from a .csv, .docx, .pdf or .txt file and
an image. The program will take the image, resize it with a max width of 500px and include some the
quote body and author. 
The image data manipulation library used is pillow.

The program can be used as a CLI tool or through a FLASK server

Instructions:
    CLI:
        1) clone the repository: git clone https://github.com/Bechev/Meme_generator
        2) create a virtual environement (as wanted): python3 -m venv .
        3) activate the venv: source ./bin/activate
        4) install the dependencies: pip install -r requirements.txt
        5) run the meme.py script with the arguments wanted: python3 meme.py --path --body --author

    FLASK server:
        1) clone the repository: git clone https://github.com/Bechev/Meme_generator
        2) create a virtual environement (as wanted): python3 -m venv .
        3) activate the venv: source ./bin/activate
        4) install the dependencies: pip install -r requirements.txt
        5) run the app.py script: python3 app.py
        6) Navigate to your localhost as served by flask (http://127.0.0.1:5000/ by default)


Program organization:
- app.py: runs the flask server
- meme.py: runs the CLI 
- _data: used to get store the data (quotes or images)
- MemeGenerator: module in charge of taking the image, resizing it and implementing a quote
- QuoteEngine: module in charge or parsing the data from the quotes document for the specified extensions
- tmp: default folder used to drop the output meme
- templates:
