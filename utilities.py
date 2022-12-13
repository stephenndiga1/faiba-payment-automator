from states import USA_STATES, CANADA_STATES, AUSTRALIA_STATES


def readlines(file_handle, no_of_lines: int) -> list:
    """Reads lines from a file and returns them as a list of strings.

    :param file_handle: The file to read from
    :param lines: The number of lines to read
    :return: A list of strings containing the lines read from the file
    """
    lines = []
    for _ in range(no_of_lines):
        line = file_handle.readline()
        if not line:
            break
        lines.append(line)

    return lines


def code_to_state(country, code):
    """
    Converts a state code to a full state name.

    :param country: The country the state belongs to
    :param code: The state code to convert
    :return: The full state name
    """
    if country == "United States":
        for state in USA_STATES:
            if state["code"] == code:
                return state["state"]
    elif country == "Canada":
        for state in CANADA_STATES:
            if state["code"] == code:
                return state["state"]
    elif country == "Australia":
        for state in AUSTRALIA_STATES:
            if state["code"] == code:
                return state["state"]
    else:
        return False
