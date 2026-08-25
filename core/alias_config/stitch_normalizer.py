"""This file will use the stitch type enum to convert the user input into the
standard language that is defined in the stitch_type file. It will return the
stitches to the parser as common language stitches for use in the program."""

from .stitch_type import StitchType

class StitchNormalizer:
    """This class is going to accept user input as a string and convert it to
    the canonical stitch type that is defined in the stitch_type file."""

    stitches = {
    "single crochet": StitchType.SINGLE_CROCHET,
    "sc": StitchType.SINGLE_CROCHET,
    "single": StitchType.SINGLE_CROCHET,
    "s crochet": StitchType.SINGLE_CROCHET,
    "half double crochet": StitchType.HALF_DOUBLE_CROCHET,
    "half double": StitchType.HALF_DOUBLE_CROCHET,
    "hdc": StitchType.HALF_DOUBLE_CROCHET,
    "half dc": StitchType.HALF_DOUBLE_CROCHET,
    "double crochet": StitchType.DOUBLE_CROCHET,
    "double": StitchType.DOUBLE_CROCHET,
    "dc": StitchType.DOUBLE_CROCHET,
    "d crochet": StitchType.DOUBLE_CROCHET,
    "triple crochet": StitchType.TRIPLE_CROCHET,
    "triple": StitchType.TRIPLE_CROCHET,
    "tr": StitchType.TRIPLE_CROCHET,
    "tc": StitchType.TRIPLE_CROCHET,
    "treble": StitchType.TRIPLE_CROCHET,
    "treble crochet": StitchType.TRIPLE_CROCHET,
    "tr crochet": StitchType.TRIPLE_CROCHET,
    "sl st": StitchType.SLIP_STITCH,
    "slip stitch": StitchType.SLIP_STITCH,
    "slip": StitchType.SLIP_STITCH,
    "slst": StitchType.SLIP_STITCH,
    "sl": StitchType.SLIP_STITCH,
    "ss": StitchType.SLIP_STITCH,
    "ch": StitchType.CHAIN,
    "chain": StitchType.CHAIN,
    "inc": StitchType.INCREASE,
    "increase": StitchType.INCREASE,
    "2sc in same st": StitchType.INCREASE,
    "2sc": StitchType.INCREASE,
    "inc sc": StitchType.INCREASE,
    "sc inc": StitchType.INCREASE,
    "dec": StitchType.DECREASE,
    "decrease": StitchType.DECREASE,
    "sc dec": StitchType.DECREASE,
    "sc2tog": StitchType.DECREASE,
    "sc 2 tog": StitchType.DECREASE,
    "sc2 tog": StitchType.DECREASE,
    "mr": StitchType.MAGIC_RING,
    "magic ring": StitchType.MAGIC_RING,
    "mc": StitchType.MAGIC_RING,
    "magic circle": StitchType.MAGIC_RING,
    "magic loop": StitchType.MAGIC_RING,
    "back loop only": StitchType.BACK_LOOP_ONLY,
    "back loop": StitchType.BACK_LOOP_ONLY,
    "blo": StitchType.BACK_LOOP_ONLY,
    "front loop only": StitchType.FRONT_LOOP_ONLY,
    "front loop": StitchType.FRONT_LOOP_ONLY,
    "flo": StitchType.FRONT_LOOP_ONLY,
    "join": StitchType.JOIN,
    "fo": StitchType.FASTEN_OFF,
    }

    def normalize_stitch(self, user_input):
        """This function accepts the input from the user and returns the
        canonical stitch type"""
        if not isinstance(user_input, str):
            raise ValueError("Stitch not found. Please check your spelling and try again.")
        user_input_lower = user_input.lower().strip().replace("-", " ")
        if user_input_lower in self.stitches:
            return self.stitches[user_input_lower]
        else:
            raise ValueError("Stitch not found. Please check your spelling and try again.")
