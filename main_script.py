import argparse
from p_acquisition import m_acquisition
from p_wrangling import m_wrangling
from p_analysis import m_analysis
from p_reporting import m_reporting

def argument_parser():
    parser = argparse.ArgumentParser(description = 'Specify imput db,api key and web url')
    parser.add_argument("-c", "--country", type = str, dest ='country', help="Specify a country...", required=True)
    args = parser.parse_args()
    return args

def main(country):
    print('Starting pipe line')
    df_acq = m_acquisition.data_df()
    print('Cleaning retrieved data!')
    df_wrang= m_wrangling.wrangle()
    print('Analysing data!')
    df_analysis=m_analysis.analyze()
    print('Reporting data!')


if __name__ == '__main__':
    arguments = argument_parser()
    print(arguments.country)
    main(arguments)
