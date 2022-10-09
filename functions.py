from art import *

def prepare(name: str, citate: list) -> str:
    """

    :param name: name of the user
    :param citate: citate to display
    :return: HTML to render
    """



    output_html = ""
    # some text
    text = [
        "Happy",
        "teachers_day!",
        "------------------",
        "from_programmers",
        "to teachers",
    ]

    for elem in text:
        output_html += text2art(elem.center(18, "."), font="block", chr_ignore=False) + "\n"

    output_html += text2art(f"{name} - to dla Ciebie", "random") + "\n"
    output_html += text2art("CYTAT", font="dohn") + "\n"
    output_html += citate[0] + "\n"
    output_html += text2art(citate[1], font="white_bubble") + "\n"
    output_html += "----------------------------------------------------------------" + "\n"
    output_html += text2art("Selkcja Informatyki szkolnej", font="white_bubble") + "\n"
    output_html += "https://github.com/PTI/" + "\n"


    return output_html

