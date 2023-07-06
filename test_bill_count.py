from count_bills_votes import (
    get_legislators_name,
    create_count_votes_bill_structure,
    get_votes_bill_ids,
    calculate_votes_per_bill,
)


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


def bill_generator():
    data = [
        ["id", "title", "sponsor_id"],
        ["1", "bill 1", "1"],
        ["2", "bill 2", "4"],
    ]

    for row in data:
        yield row


def vote_generator():
    data = [
        ["id", "bill_id"],
        [
            "1",
            "1",
        ],
        [
            "2",
            "2",
        ],
    ]

    for row in data:
        yield row


def test_get_legislators_name():
    expected = {"1": "legislator 1", "2": "legislator 2"}

    reader = legislators_generator()
    data = get_legislators_name(reader)

    assert expected == data


def test_create_count_votes_bill_structure():
    expected = {"1": ["bill 1", 0, 0, "legislator 1"], "2": ["bill 2", 0, 0, "Unknown"]}

    reader = legislators_generator()
    legislators_dict = get_legislators_name(reader)

    reader = bill_generator()
    data = create_count_votes_bill_structure(reader, legislators_dict)
    assert expected == data


def test_get_votes_bill_ids():
    expected = {"1": "1", "2": "2"}

    reader = vote_generator()
    data = get_votes_bill_ids(reader)
    assert expected == data


def test_calculate_votes_per_bill():
    expected = {"1": ["bill 1", 1, 1, "legislator 1"], "2": ["bill 2", 1, 1, "Unknown"]}

    reader = legislators_generator()
    legislators_dict = get_legislators_name(reader)

    reader = bill_generator()
    bills_count_votes_dict = create_count_votes_bill_structure(reader, legislators_dict)

    reader = vote_generator()
    votes_ids_dict = get_votes_bill_ids(reader)

    reader = vote_results_generator()
    data = calculate_votes_per_bill(reader, votes_ids_dict, bills_count_votes_dict)

    assert expected == data
