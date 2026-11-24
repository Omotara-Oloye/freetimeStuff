import pytest

from tictactoe import has_won, main


@pytest.mark.parametrize(
    ("board", "winner"),
    [
        ("XXXOO    ", "X"),
        ("OX OX O  ", "O"),
        ("X OXOXO X", "O"),
    ],
)
def test_has_won(board, winner):
    loser = "O" if winner == "X" else "X"
    assert has_won(list(board), winner)
    assert not has_won(list(board), loser)


@pytest.mark.parametrize(
    ("moves", "result"),
    [
        ("14253", "Player X has won the game"),
        ("123546879", "All slots have been filled resulting in a tie game."),
    ],
)
@pytest.mark.parametrize("replay", [False, True])
def test_play_again(monkeypatch, capsys, moves, result, replay):
    answers = ["2", *moves]
    if replay:
        answers.extend([" YeS ", "2", *"14253"])
    answers.append("no")
    answers = iter(answers)

    def respond(prompt):
        print(prompt)
        return next(answers)

    monkeypatch.setattr("builtins.input", respond)
    main()

    assert next(answers, None) is None
    output = capsys.readouterr().out
    rounds = output.split("Play Again? (y/n): ")
    assert len(rounds) == (3 if replay else 2)
    assert result in rounds[0]
    if replay:
        empty_board = " | | \n---------\n | | \n---------\n | | \n"
        assert empty_board + "Player X, enter your move 1-9:" in rounds[1]
        assert "Player X has won the game" in rounds[1]
    assert not rounds[-1].strip()
