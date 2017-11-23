




# tyda.py

This is a very simple tool, written in python, that uses the native tyda.se http request to translate between Swedish and English.




## Installation

Clone the repo and run:

    pip install -r requirements.txt

After that a translation can be made with:

    ./tyda.py translation

The result would be written in your terminal window:

    Did you mean:
       Engelska
        - translation
        - translation agency
        - translation bureau
        - translation contract
        - translation department
       Svenska
        - translation
        - translationell
        - translationshastighet
        - translationsrörelse
    
    translation
       TRANSLATIONS
          Engelska
           - translation
    translation
       SYNONYMS
        -  interpretation 
        -  rendering 
        -  version 
        -  interlingual rendition 
        -  transformation 
        -  assumption [ religion ]
        -  changeover 
        -  conversion 
       TRANSLATIONS
          Svenska
           - översättning
           - tolkning
           - återgivning
           - transformering
           - translation
           - omvandling




## Usage tip

Write a simple alias in your .bash_rc, .bash_completion or similar like this:

    alias tyda='/home/your/path/to/tyda.py'

After that you can translate anywhere in your terminal window by typing:

    tyda the words you want to translate


