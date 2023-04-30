from pybtex.database.input import bibtex


def bib_to_markdown(bib_field_dict: dict, title_key: str) -> list:
    """Create a list of Markdown-formatted strings with bib_field_dict

    :param bib_field_dict: An object that converts the fields contained in the entries of the BIB file into a dict
    :type bib_field_dict: dict
    :param title_key: The key value of the field that will be the main heading of the md file
    :type title_key: str
    :return: List of strings converted to MarkDown format
    :rtype: list
    """
    md_body = []
    for k, v in bib_field_dict.items():
        if k ==title_key:
            md_body.append(f'\n## {k.upper()}: {v} \n')
        else:
            md_body.append(f'- **{k}:** {v} \n')
    return md_body

def bib2md(bib_path: str, title_key: str, save_md_path: str) -> list:
    """Convert bib file to markdown format

    :param bib_path: Input BIB file path.
    :type bib_path: str
    :param title_key: The key value of the field that will be the main heading of the md file
    :type title_key: str
    :param save_md_path: Output MarkDown file path.
    :type save_md_path: str
    :return: List of strings that will be consist of MarkDown.
    :rtype: list
    """
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_path)
    entries_dict = bib_data.entries

    md_total_body = []
    for _,v in entries_dict.items():
        bib_field_dict = dict(v.fields)
        md_total_body += bib_to_markdown(bib_field_dict, title_key)

    with open(save_md_path, 'w') as f:
        f.write("".join(md_total_body))

    return md_total_body