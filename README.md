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

    FLASK server:


Program organization:
- app.py: runs the flask server
- meme.py: runs the CLI 
- _data: used to get store the data (quotes or images)
- MemeGenerator: module in charge of taking the image, resizing it and implementing a quote
- QuoteEngine: module in charge or parsing the data from the quotes document for the specified extensions
- tmp: default folder used to drop the output meme
- templates:
