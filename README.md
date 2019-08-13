# Game of cell cycle life
Written by Yuval Kushmaro and Keren Avnery - https://github.com/kerenavnery
For a class project in `Systems Medicine by Uri Alon` 
https://www.weizmann.ac.il/mcb/UriAlon/download/systems-medicine-course-2019

Weizmann Institute of Science, 2019

## This repository
A model for a tissue's cell cycle, based on `Conway's Game Of Life`. Implemented in python, forked from https://github.com/radomirbosak/game-of-life


## Cell cycle theory

Once critical stress is applied on a cell  - P53 ( transcription factor) is activated by the damage to the DNA →  halting the cell cycle and its proliferation. After the halt different fates are optional- if damage is successfully fixed the cell continues its cycle. if not the cell will become scenecent or will undergo apoptosis (programmed cell death). Once a cell is scenecent it can influence its environment in different ways as shown here:

![Secescent cell actions](Secescent_cell_actions.jpg)

 Another possible fate is cancer when the P53 pathway is overrun leading to proliferation of a cancerous tissue.


## State machine model
A cell starts in normal cell cycle (white colored). Stress may cause it to malfunction, and several other states can emerge:
### todo: add state machine drawing
Cancer - red colored
Senscence - gray colored
Cell death (apoptosis or autophagy) - black colored

### Limitations:
- This model does not allow cell reproduction
- No neighborhood effects (cells do not influence each other)
- Chances and rates are randomaly selected, true values need to be determined ampirically

