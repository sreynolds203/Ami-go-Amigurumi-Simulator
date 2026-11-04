from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    STITCH = auto()
    REPEAT_START = auto()
    REPEAT_END = auto()
    STITCH_COUNT = auto()
    STITCH_MODIFIER_START = auto()
    STITCH_MODIFIER_END = auto()


@dataclass
class Token:
    token_type: TokenType
    value: str | None = None
    count: int | None = None


class Tokenizer():
    def __init__(self, user_input):
        self.user_input = user_input
        self.token_list: list = []
        self.current_str_chunk: str = ""
        self.current_state: int = 0 # state dictates depth of repeat sections

    def _parse_stitch_chunk(self, chunk):
        if not chunk:
            raise ValueError("Cannot parse empty chunk")
        split_chunk = chunk.split(" ")
        if len(split_chunk) < 2:
            raise ValueError("Chunk must contain a stitch name and count")
        return Token(token_type=TokenType.STITCH, value=split_chunk[0], count=int(split_chunk[1]))

    def tokenize(self):
        skip_until = -1
        for i, char in enumerate(self.user_input):
            if i <= skip_until:
                continue

            if char == ",":
                if self.current_str_chunk.strip():
                        self.token_list.append(self._parse_stitch_chunk(self.current_str_chunk.strip()))
                        self.current_str_chunk = ""

            elif char == "[":
                self.token_list.append(Token(token_type=TokenType.REPEAT_START))
                self.current_state += 1
                self.current_str_chunk = ""

            elif char == "]":
                if self.current_str_chunk.strip():
                        self.token_list.append(self._parse_stitch_chunk(self.current_str_chunk.strip()))
                        self.current_str_chunk = ""
                self.current_state -= 1
                x_pos = self.user_input.find("x", i)
                if x_pos == -1:
                    raise ValueError("Expected repeat count after ]")

                current_pos = x_pos +1
                digit_as_string = ""

                while current_pos < len(self.user_input) and self.user_input[current_pos].isdigit():
                    digit_as_string += self.user_input[current_pos]
                    current_pos += 1
                    skip_until = current_pos - 1

                repeat_count = int(digit_as_string)
                self.token_list.append(Token(token_type=TokenType.REPEAT_END, count=repeat_count))

            elif char == "(":
                if self.current_str_chunk.strip():
                        self.token_list.append(self._parse_stitch_chunk(self.current_str_chunk.strip()))
                        self.current_str_chunk = ""
                x_pos = self.user_input.find(")", i)
                if x_pos == -1:
                    raise ValueError("Expected closing ) for stitch count")

                current_pos = i + 1
                stitch_count = int(self.user_input[current_pos : x_pos])
                self.token_list.append(Token(token_type=TokenType.STITCH_COUNT, count=stitch_count))
            else:
                self.current_str_chunk += char

        return self.token_list
