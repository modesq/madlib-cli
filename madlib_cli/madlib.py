import re


def read_template(path):
    """
    opens the the path sent as a parameter and reads it, then returns the file contents.
    """
    try:
        with open(path, "r") as file:
            return file.read()
    except:
        raise


def parse_template(original_template):
    """
    takes the original template and extracts the required_words from between the curly
    brackets, returns them in a new tuple, alongside the now emptied template.
    """
    required_words = re.findall("{(.*?)}", original_template)
    empty_template = re.sub("{.+?}", "{}", original_template)
    return empty_template, (tuple)(required_words)


def merge(empty_template, required_words: tuple):
    """
    takes the empty template and the words required to be entered by the player and
    inserts them into the template as needed.
    """
    return empty_template.format(*required_words)


def welcome():
    """
    prints out a welcome message for the player
    """
    print(
        """
*****************************************
** Hello and welcome to this game, to  **
**  participate in the game you only   **
**    need to follow the prompts on    **
**  the on the screen as they come up. **
*****************************************
"""
    )


def user_interface(path):
    """
    used to display the user interface and run the other functions where needed to make the game run as needed.

    """
    welcome()
    # template = read_template("assets/make_me_a_video_game_template.txt")
    # template = read_template(path)
    # required_words, required_words = parse_template(template)
    # filled_template = list()
    # for word in required_words:
    #     filled_template.append(input(f"\nplease enter a {word} \n >"))
    # with open(path, "w") as file:
    #     temp = merge(required_words, (tuple)(filled_template))
    #     file.write(temp)
    #     print(temp)
    reuseable_text = read_template(path)
    empty_template, required_words = parse_template(reuseable_text)
    filled_template = list()
    for word in required_words:
        filled_template.append(input(f"\nplease enter a {word} \n >"))
    with open("assets/output.txt", "w") as file:
        temp = merge(empty_template, (tuple)(filled_template))
        file.write(temp)
        print(temp)


if __name__ == "__main__":
    # read_template("assets/dark_and_stormy_night_template.txt")
    # read_template("assets/make_me_a_video_game_template.txt")
    user_interface("assets/make_me_a_video_game_template.txt")
