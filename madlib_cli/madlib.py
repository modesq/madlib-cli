def read_template(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except:
        raise


def parse_template():
    pass


def merge():
    pass


if __name__ == "__main__":
    read_template("assets/make_me_a_video_game_template.txt")
