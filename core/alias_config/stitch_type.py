"""StitchType represents the list of stitches that the system will read and use to generate the simulated rendering. The other files will convert the user input into the correct standard verbiage."""

from enum import Enum

class StitchType(Enum):
    """These are the canonical terms that should be used in the program after the user inputs their own types"""
    SINGLE_CROCHET = "sc"
    HALF_DOUBLE_CROCHET = "hdc"
    DOUBLE_CROCHET = "dc"
    TRIPLE_CROCHET = "tr"
    INCREASE = "inc"
    DECREASE = "dec"
    HALF_DOUBLE_DECREASE = "hdc dec"
    DOUBLE_DECREASE = "dc dec"
    TRIPLE_DECREASE = "tr dec"
    CHAIN = "ch"
    SLIP_STITCH = "sl st"
    BOBBLE_STITCH = "bobble"
    PUFF_STITCH = "puff"
    POPCORN_STITCH = "popcorn"
    MAGIC_RING = "mr"
    JOIN = "join"
    FASTEN_OFF = "fo"
    # FRONT_LOOP and BACK_LOOP are stitch modifiers. 
    BACK_LOOP_ONLY = "blo"
    FRONT_LOOP_ONLY = "flo"
    
    