import csv
from typing import List, Dict, Optional, Union


def create_counts_votes_structure(reader) -> Dict[str, List[Union[str, int]]]:
    """
    Gets a reader from a file and generate a structured dictionary.

    This function must be used inside the csv_helpers/read_csv function
    and it will handle the data from the legislators.csv.
    The dicionary generated will be used to calculate the amount of votes(supporting, opposing) for each legislator.

    :param reader: Iterable containing the row of a file.
    :return: a dicionary having the key as the legislators ids,
    and the value as a list with three elements, the first one is the legislators name,
    the second is the amount of support votes and the third is the amount of oppose votes.
    """
    legislators_count_votes = {}
    next(reader)
    for row in reader:
        legislators_count_votes[row[0]] = [row[1], 0, 0]

    return legislators_count_votes


def calculate_total_votes(
    reader, data: Dict[str, List[Union[str, int]]] = {}
) -> Dict[str, List[Union[str, int]]]:
    """
    Gets a reader from a file and generate a structured dictionary.
    It will calculate the total amount of votes supporting and opposing a bill for each legislator

    This function must be used inside the csv_helpers/read_csv function
    and it will handle the data from the vote_results.csv.
    the dictionary generated will have the the amount of support and oppose votes.

    :param reader: Iterable containing the row of a file
    :return: a dicionary having the key as the legislators ids,
    and the value as a list with three elements, the first one is the legislators name,
    the second is the amount of support votes and the third is the amount of oppose votes.
    """
    legislators_count_votes = data

    next(reader)
    for row in reader:
        legislators_count_votes[row[1]] = legislators_count_votes.get(
            row[1], ["Unknow", 0, 0]
        )
        if row[3] == "1":
            legislators_count_votes[row[1]][1] += 1
        elif row[3] == "2":
            legislators_count_votes[row[1]][2] += 1

    return legislators_count_votes
