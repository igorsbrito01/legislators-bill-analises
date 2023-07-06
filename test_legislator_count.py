from count_legislators_votes import create_counts_votes_structure, calculate_total_votes


def legislators_generator():
    data = [["id", "name"], ["1", "legislator 1"], ["2", "legislator 2"]]

    for row in data:
        yield row


def vote_results_generator():
    data = [
        ["id", "legislator_id", "vote_id", "vote_type"],
        ["1", "1", "1", "1"],
        ["2", "1", "2", "1"],
        ["3", "2", "1", "2"],
        ["3", "2", "2", "2"],
    ]

    for row in data:
        yield row


def test_create_counts_votes_structure():
    expected = {"1": ["legislator 1", 0, 0], "2": ["legislator 2", 0, 0]}

    reader = legislators_generator()
    data = create_counts_votes_structure(reader)
    assert expected == data


def test_calculate_total_votes():
    expected = {"1": ["legislator 1", 2, 0], "2": ["legislator 2", 0, 2]}

    reader = legislators_generator()
    legislators = create_counts_votes_structure(reader)

    reader = vote_results_generator()
    data = calculate_total_votes(reader, data=legislators)
    assert expected == data
