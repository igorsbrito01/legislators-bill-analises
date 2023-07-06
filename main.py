from helpers.csv_helpers import read_csv, write_csv
from count_legislators_votes import create_counts_votes_structure, calculate_total_votes
from count_bills_votes import (
    get_legislators_name,
    get_votes_bill_ids,
    create_count_votes_bill_structure,
    calculate_votes_per_bill,
)


def count_legislators_votes():
    legislators_count_votes = read_csv(
        "./legislators.csv", create_counts_votes_structure
    )
    legislators_count_votes = read_csv(
        "./vote_results.csv", calculate_total_votes, data=legislators_count_votes
    )

    csv_data = [["id", "name", "num_supported_bills", "num_opposed_bills"]]

    for key, value in legislators_count_votes.items():
        csv_data.append([key, value[0], value[1], value[2]])

    write_csv("./legislators-support-oppose-count.csv", csv_data)


def count_bills_votes():
    legislators_dict = read_csv("./legislators.csv", get_legislators_name)
    votes_ids_dict = read_csv("./votes.csv", get_votes_bill_ids)
    bills_count_votes_dict = read_csv(
        "./bills.csv",
        create_count_votes_bill_structure,
        legislators_dict=legislators_dict,
    )

    bills_count_votes_dict = read_csv(
        "./vote_results.csv",
        calculate_votes_per_bill,
        votes_ids_dict=votes_ids_dict,
        bills_count_votes_dict=bills_count_votes_dict,
    )

    csv_data = [["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]]
    for key, value in bills_count_votes_dict.items():
        csv_data.append([key, value[0], value[1], value[2], value[3]])

    write_csv("./bills-support-oppose-count.csv", csv_data)


def main():
    count_legislators_votes()
    count_bills_votes()


if __name__ == "__main__":
    main()
