"""The models file will define the data structures that will be used
through the pipeline."""

from dataclasses import dataclass
from core.alias_config.stitch_type import StitchType

@dataclass
class Stitch:
    """This class holds each stitch that is added to the pattern. This could be a single crochet stitch or slip stitch or any other stitch type."""
    user_stitch: str
    canonical_stitch: StitchType


@dataclass
class Round:
    """The Round is a set of stitches that forms one 'Round' of the pattern. The round is formed with a list of each stitch that is placed in the specified order by the user."""
    stitch_list: list[Stitch]
    round_number: int
    user_stitch_count: int
    # round_join_type will be refactored later to accept specific enum values
    round_join_type: str


@dataclass
class Section:
    """The section defines the piece that is worked with the set of rounds of stitches. This could be a single part, such as a head or body, that is created to be part of a larger piece. The section is a single completed element of the final piece."""
    name: str
    rounds: list[Round]


@dataclass
class Pattern:
    """The Pattern is the final completed project that combines all of the Sections that were created and are to be assembled to complete the project."""
    sections: list[Section]
    metadata: dict
