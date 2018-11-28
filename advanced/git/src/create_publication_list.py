#! /usr/bin/env python

import re
import sys

###############################################################################
# Markdown Formatting Functions
###############################################################################

def MDheader(string, level=4):
    return(f'#### {string}')

def MDbold(string):
    return(f'**{string}**')

def MDitalic(string):
    return(f'*{string}*')

def MDstrikethrough(string):
    return(f'~{string}~')

def MDlink(string, target_url):
    return(f'[{string}]({target_url})')

def MDquote(string):
    return(f'> {string}')

def MDcode(string, mode='guess', language='python'):
    if mode in ('guess', 'g'):
        if '\n' in string:
            mode = 'multi'
        else:
            mode = 'single'
    if mode in ('single', 's'):
        return(f'`{string}`')
    elif mode in ('multi', 'm'):
        return(f'''```{language}\n{string}\n```''')
    else:
        raise ValueError(f'Invalid value, {mode}, provided for "mode" argument. Must be one of "single"/"s", "multi"/"m". or "guess"/"g".')

def MDlist(strings, mode='bullet'):
    symbols = {'bullet': '-',
                    'b': '-',
                    '-': '-',
                    '+': '+',
                    '*': '*'}
    if mode in symbols:
        return(''.join([f'{symbols[mode]} {string}\n' for string in strings]))
    elif mode in ('numeric', 'n', '1'):
        return (''.join([f'{i+1}. {string}\n' for i, string in enumerate(strings)]))
    else:
        raise ValueError(f'Invalid value, {mode}, provided for "mode" argument. Must be one of "bullet"/"b"/"-", "numeric"/"n"/"1", "*", or "+".')

def HTMLcomment(string):
    return(f'<!--{string}-->')

###############################################################################
# Processing Functions
###############################################################################

def output_formatted_entry(author_list, title, journal, year, doi, pmid):
    if len(author_list.split(',')) > 2:
        first_author = author_list.split(',')[0]
        author_list = first_author.split(' ')[0] + ' et al'
    elif len(author_list.split(',')) == 2:
        authors = author_list.split(',')
        author_list = authors[0].split(' ')[0] + ' & ' + authors[1].split(' ')[0]
    return (year, f'{MDbold(title)}. {author_list}. {MDitalic(journal)}. {doi}. {MDlink(pmid, f"https://www.ncbi.nlm.nih.gov/pubmed/?term={pmid}")}')


def match_publication_info(string):
    match = re.match(r"\d+: ([^\.]+)\. ([-:\(\)\w\d\s,']+[\.\?]) ([\w\s]+)\. (\d{4}).+doi: ([\d\.\/\w]+)\..+PubMed PMID: (\d+).*", string)
    if match:
        return match.groups()
    else:
        raise ValueError(f"couldn't match publication info in string\n{string}\n")

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    infile = sys.argv[1]
    entries_by_year = {}

    with open(infile, 'r') as infh:
        info_string = ''
        for line in infh.readlines():
            line = line.strip()
            if line:
                info_string += f'{line} '
            elif info_string:
                info = match_publication_info(info_string)
                year, entry = output_formatted_entry(*info)
                if year in entries_by_year:
                    entries_by_year[year].append(entry)
                else:
                    entries_by_year[year] = [entry]
                info_string = ''

    for year, entries in entries_by_year.items():
        sys.stdout.write(f'{MDheader(year, level=2)}\n\n')
        sys.stdout.write(f'{MDlist(entries)}\n')
