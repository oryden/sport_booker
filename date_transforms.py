month_dictionary = {"January": 1,
                    "February": 2,
                    "Mars": 3,
                    "April": 4,
                    "May": 5,
                    "June": 6,
                    "July": 7,
                    "August": 8,
                    "September": 9,
                    "October": 10,
                    "November": 11,
                    "December": 12
                    }


def matchi_date_split(test_text):
    """
    Help function that takes a string and returns the month and date based on a string from Matchi
    :param test_text:
    :return:
    """
    date = int(test_text.split()[1])
    month = int(month_dictionary[test_text.split()[2]])

    return date, month


if __name__ == '__main__':
    test_text = "Monday 25 January"
    date, month = matchi_date_split(test_text)

    print(date)
    print(month)