import argparse

def argument_parser():
    parser=argparse.ArgumentParser(description='print a person name....')
    parser.add_argument('-n','--nombre',type=str,help="specify a name...")
    arg=parser.parse_args()
    return arg

def main(argument):
    print(argument.nombre)

if __name__=='__main__':
    arguments=argument_parser()
    main(arguments)