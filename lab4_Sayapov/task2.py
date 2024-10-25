import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(input_f, output_f) -> None:
    list_of_rows = []
    with open(input_f, 'r') as input_file:
        reader = csv.DictReader(input_file, delimiter=",", lineterminator="\n")
        for row in reader:
            list_of_rows.append(row)
    print(json.dumps(list_of_rows, indent=4, ensure_ascii=False)) # Абсолютно всё правильно, но не проходит проверку из-за пустой последней строки, которой нет в файле output.json
    with open(output_f, "w") as output_file:  # Задание выглядит не полным
        json.dump(list_of_rows, output_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task(INPUT_FILENAME, OUTPUT_FILENAME)
