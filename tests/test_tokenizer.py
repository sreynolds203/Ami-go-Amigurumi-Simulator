import pytest
from core.parser.tokenizer import Tokenizer, Token, TokenType

@pytest.fixture
def tokenizer():
    return Tokenizer("placeholder")
    
def test_parse_stitch_chunk_happy_path(tokenizer):
    result = tokenizer._parse_stitch_chunk("sc 6")
    assert result.token_type == TokenType.STITCH
    assert result.value == "sc"
    assert result.count == 6
    
def test_parse_stitch_chunk_empty_value_error(tokenizer):
    with pytest.raises(ValueError):
        tokenizer._parse_stitch_chunk("")
        
def test_parse_stitch_chunk_missing_count_value_error(tokenizer):
    with pytest.raises(ValueError):
        tokenizer._parse_stitch_chunk("sc")
        
def test_parse_stitch_chunk_no_repeat(tokenizer):
    result = Tokenizer("sc 6, inc 1 (8)").tokenize()
    assert result[0].token_type == TokenType.STITCH
    assert result[0].value == "sc"
    assert result[0].count == 6
    assert result[1].token_type == TokenType.STITCH
    assert result[1].value == "inc"
    assert result[1].count == 1
    assert result[2].token_type == TokenType.STITCH_COUNT
    assert result[2].value is None
    assert result[2].count == 8
    assert len(result) == 3
    
def test_parse_stitch_chunk_with_repeat(tokenizer):
    result = Tokenizer("sc 6, [sc 2, inc 1] x4 (24)").tokenize()
    assert result[0].token_type == TokenType.STITCH
    assert result[0].value == "sc"
    assert result[0].count == 6
    assert result[1].token_type == TokenType.REPEAT_START
    assert result[1].value is None
    assert result[1].count is None
    assert result[2].token_type == TokenType.STITCH
    assert result[2].value == "sc"
    assert result[2].count == 2
    assert result[3].token_type == TokenType.STITCH
    assert result[3].value == "inc"
    assert result[3].count == 1
    assert result[4].token_type == TokenType.REPEAT_END
    assert result[4].value is None
    assert result[4].count == 4
    assert result[5].token_type == TokenType.STITCH_COUNT
    assert result[5].value is None
    assert result[5].count == 24
    assert len(result) == 6
    
def test_parse_stitch_chunk_extra_whitespace(tokenizer):
    result = Tokenizer("sc 6,  inc 1 (8)").tokenize()
    assert result[0].token_type == TokenType.STITCH
    assert result[0].value == "sc"
    assert result[0].count == 6
    assert result[1].token_type == TokenType.STITCH
    assert result[1].value == "inc"
    assert result[1].count == 1
    assert result[2].token_type == TokenType.STITCH_COUNT
    assert result[2].value is None
    assert result[2].count == 8
    assert len(result) == 3
    
def test_parse_stitch_chunk_missing_closing_parenthsis(tokenizer):
    with pytest.raises(ValueError):
        Tokenizer("sc 6, inc 1 (8").tokenize()
        
def test_parse_stitch_chunk_missing_repeat_multiplier(tokenizer):
    with pytest.raises(ValueError):
        Tokenizer("sc 6, [sc 2, inc 1] 4 (24)").tokenize()
