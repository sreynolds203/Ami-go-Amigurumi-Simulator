# Ami-go: Amigurumi Pattern Simulator

Ami-go simulates amigurumi patterns stitch by stitch, so you can see the size and shape of a piece before you crochet it.

## Why I'm building this
I crochet and love designing new amigurumi toys, but the process of creating new projects can be time consuming and involve a lot of trial and error. I wanted to create this as a free tool for anyone that shares my passion to be able to explore their own creative mind and build new projects in a more efficient manner.

## Status: early development
**Working now**
- Stitch normalization: write stitches however you like (“sc”, “SC”, “single crochet”) and they resolve to the same stitch type. Covered by passing unit tests.
- Data models: a pattern is represented as Pattern → Section → Round → Stitch, the structure the parser will fill in.

**In progress**
- Building the parser to convert user input into the canonical stitches and rounds the simulator uses.

**Planned**
- 3D preview of the pattern once entered by the user
- Ability to save/export as text, markdown, or pdf
- Create canvas view that allows multiple pattern imports that can be positioned on one screen. (Think about a bear project that needs arms and legs added to the body, all created as different pieces.)

## How it will work
The user will enter the pattern as they would, one round at a time, and will submit the pattern to be rendered in a separate pane. Additions and changes can be made and a new submission can be rendered. When the user is happy with the final result, they will be able to save the pattern or export it in a format they prefer.

Under the hood, a pattern moves through a pipeline:

```mermaid
flowchart LR
    A[Pattern text] --> B[Parser]
    B --> C[Stitch normalizer]
    C --> D[Data models]
    D --> E[3D preview]
```

## Project structure
```
core/
  alias_config/   # stitch types and normalization
  parser/         # pattern parsing (in progress)
  models.py       # Pattern, Section, Round, Stitch
tests/            # pytest suite
```

## Run it locally
```bash
git clone https://github.com/sreynolds203/Ami-go-Amigurumi-Simulator.git
cd Ami-go-Amigurumi-Simulator
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Roadmap
- [x] Stitch normalization
- [x] Core data models
- [ ] Parser
- [ ] 3D rendering
- [ ] Save/Export function
- [ ] Canvas view

## Tech
Python, dataclasses, pytest
