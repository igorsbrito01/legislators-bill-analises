from helpers.csv_helpers import read_csv, write_csv
from count_legislators_votes import create_counts_votes_structure, calculate_total_votes


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


def main():
    count_legislators_votes()


if __name__ == "__main__":
    main()
