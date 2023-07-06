import csv
from typing import List, Any, Callable

def read_csv(file_name: str, executor: Callable, *args, **kawrgs) -> Any:
    result = None
    with open(file_name, "r") as file:
        reader = csv.reader(file, delimiter=",")

        result = executor(reader, *args, **kawrgs)

    return result


def write_csv(file_name: str, data: List[Any]) -> None:
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)
