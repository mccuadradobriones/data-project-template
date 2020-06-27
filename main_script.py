import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description = 'Specify imput db,api key and web url')
    parser.add_argument("-p", "--path", help="Specify job list file...", required="True")
    args = parser.parse_args()
    return args

def main(arguments):
    m_acquisition.get_db()

if __name__ == '__main__':
    arguments = argument_parser()
    print(arguments.path)
    main(arguments)
