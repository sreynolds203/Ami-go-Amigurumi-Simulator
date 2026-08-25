import pytest
import core.alias_config.stitch_normalizer as stitch_normalizer
import core.alias_config.stitch_type as stitch_type

@pytest.fixture
def stitch_normalizer_instance():
    return stitch_normalizer.StitchNormalizer()

# Happy path testing
happy_test_cases = [("sc", stitch_type.StitchType.SINGLE_CROCHET),
                    ("single crochet", stitch_type.StitchType.SINGLE_CROCHET),
                    ("dc", stitch_type.StitchType.DOUBLE_CROCHET),
                    ("double crochet", stitch_type.StitchType.DOUBLE_CROCHET),
                    ("tr", stitch_type.StitchType.TRIPLE_CROCHET),
                    ("triple crochet", stitch_type.StitchType.TRIPLE_CROCHET),
                    ("sl st", stitch_type.StitchType.SLIP_STITCH),
                    ("slip stitch", stitch_type.StitchType.SLIP_STITCH),
                    ("ch", stitch_type.StitchType.CHAIN),
                    ("chain", stitch_type.StitchType.CHAIN),
                    ("inc", stitch_type.StitchType.INCREASE),
                    ("increase", stitch_type.StitchType.INCREASE),
                    ("dec", stitch_type.StitchType.DECREASE),
                    ("decrease", stitch_type.StitchType.DECREASE),
                    ("mr", stitch_type.StitchType.MAGIC_RING),
                    ("magic ring", stitch_type.StitchType.MAGIC_RING),
                    ("blo", stitch_type.StitchType.BACK_LOOP_ONLY),
                    ("back loop only", stitch_type.StitchType.BACK_LOOP_ONLY),
                    ("flo", stitch_type.StitchType.FRONT_LOOP_ONLY),
                    ("front loop only", stitch_type.StitchType.FRONT_LOOP_ONLY)]

@pytest.mark.parametrize("user_input, expected", happy_test_cases)
def test_stitch_normalizer(stitch_normalizer_instance, user_input, expected):
    assert stitch_normalizer_instance.normalize_stitch(user_input) == expected

# Case tolerance testing
case_testing = [
    ("sC", stitch_type.StitchType.SINGLE_CROCHET),
    ("sinGle crochet", stitch_type.StitchType.SINGLE_CROCHET),
    ("dC", stitch_type.StitchType.DOUBLE_CROCHET),
    ("double CROchet", stitch_type.StitchType.DOUBLE_CROCHET),
    ("tR", stitch_type.StitchType.TRIPLE_CROCHET),
    ("tRIple crochet", stitch_type.StitchType.TRIPLE_CROCHET),
    ("sl St", stitch_type.StitchType.SLIP_STITCH),
    ("sLIp stitch", stitch_type.StitchType.SLIP_STITCH),
    ("CH", stitch_type.StitchType.CHAIN),
    ("chAin", stitch_type.StitchType.CHAIN),
    ("inC", stitch_type.StitchType.INCREASE),
    ("iNCRease", stitch_type.StitchType.INCREASE),
    ("DEC", stitch_type.StitchType.DECREASE),
    ("dECrease", stitch_type.StitchType.DECREASE),
    ("Mr", stitch_type.StitchType.MAGIC_RING),
    ("mAGic ring", stitch_type.StitchType.MAGIC_RING),
    ("bLO", stitch_type.StitchType.BACK_LOOP_ONLY),
    ("baCk Loop only", stitch_type.StitchType.BACK_LOOP_ONLY),
    ("FLO", stitch_type.StitchType.FRONT_LOOP_ONLY),
    ("FRont loOp only", stitch_type.StitchType.FRONT_LOOP_ONLY)
]

@pytest.mark.parametrize("user_input, expected", case_testing)
def test_stitch_normalizer_case_tolerance(stitch_normalizer_instance, user_input, expected):
    assert stitch_normalizer_instance.normalize_stitch(user_input) == expected

# Error case testing
error_cases = ["sing C", "dub C", "sl stitch", None, "   ", "", "xyz"]

@pytest.mark.parametrize("user_input", error_cases)
def test_stitch_normalizer_test_cases(stitch_normalizer_instance, user_input):
    with pytest.raises(ValueError, match="Stitch not found. Please check your spelling and try again."):
        stitch_normalizer_instance.normalize_stitch(user_input)
