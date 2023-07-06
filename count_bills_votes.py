from typing import List, Dict, Union


def get_legislators_name(reader) -> Dict[str, str]:
    """
    From a file reader create a dictionary with the legislator id and name

    This function must be used inside the csv_helpers/read_csv function
    and it will handle the data from the legislators.csv.

    :param reader: Iterable containing the row of a file
    :return: dictionary with the key as the legislator id and the value as legislator name
    """
    legislators_dict = {}

    next(reader)
    for row in reader:
        legislators_dict[row[0]] = row[1]

    return legislators_dict


def create_count_votes_bill_structure(
    reader, legislators_dict: Dict[str, str]
) -> Dict[str, List[Union[str, int]]]:
    """
    Gets a reader from a file and generate a structured dictionary.

    This function must be used inside the csv_helpers/read_csv function
    and it will handle the data from the bills.csv.

    :param reader: Iterable containing the row of a file
    :return: dictionary with the key as the bill id and the value as a list with four elements,
    the first is the bill title, the second is the amount of support votes, the third is the amount
    of oppose votes and the fourth is the sponsor name
    """
    bills_count_votes_dict = {}

    next(reader)
    for row in reader:
        primary_sponsor = legislators_dict.get(row[2], "Unknown")
        bills_count_votes_dict[row[0]] = [row[1], 0, 0, primary_sponsor]

    return bills_count_votes_dict


def get_votes_bill_ids(reader) -> Dict[str, str]:
    """
    From a file reader create a dictionary with the vote id and the bill

    This function must be used inside the csv_helpers/read_csv function
    and it will handle the data from the votes.csv.

    :param reader: Iterable containing the row of a file
    :return: dictionary with the key as the vote id and the value as the bill id
    """
    votes_ids_dict = {}

    next(reader)
    for row in reader:
        votes_ids_dict[row[0]] = row[1]

    return votes_ids_dict


def calculate_votes_per_bill(
    reader, votes_ids_dict:  Dict[str, str], bills_count_votes_dict: Dict[str, List[Union[str, int]]] ={}
) -> Dict[str, List[Union[str, int]]]:
    next(reader)
    for row in reader:
        bill_id = votes_ids_dict[row[2]]

        bills_count_votes_dict[bill_id] = bills_count_votes_dict.get(
            bill_id, ["Unknow", 0, 0, "Unknow"]
        )
        if row[3] == "1":
            bills_count_votes_dict[bill_id][1] += 1
        elif row[3] == "2":
            bills_count_votes_dict[bill_id][2] += 1

    return bills_count_votes_dict
