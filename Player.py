"""
This module contains functions relating to user interaction,
including automated players.
"""

import random
import Canvas
import utils
import board
import utils
import globVar

def turn():
    Canvas.drawBoard()

    runagain = True

    if not globVar.noPlayers:
        while runagain:
            fromSqr = select()
            availMoves = fromSqr.piece.scan()
            runagain = not utils.hasMoves(availMoves)

            if runagain:
                board.Grid(fromSqr.row, fromSqr.col).piece.selected = False
                Canvas.chooseAvailableMessage()
                Canvas.drawBoard()

    choice = choose(availMoves)
    utils.move(fromSqr, availMoves, choice)

def select():
    print(" Select which piece to move.")
    selecting = True
    while selecting:
        col = utils.r_c('c')
        row = utils.r_c('r')

        if board.Grid(row,col).piece.color != globVar.player:
            Canvas.selectError()
        else:
            board.Grid(row,col).piece.selected = True # display fromSqr as selected
            selecting = False

    return board.Grid(row,col)

def choose(availMoves):
    Canvas.drawBoard()
    running = True

    while running:
        running = False
        choice = int(input(" Choose a move (number): "))

        if (choice < 1) or (choice > len(availMoves)):
            Canvas.pickValidMoveMessage()
            running = True

    return choice
