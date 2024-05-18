import re

def replace_commas(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(',', '、')
    content = "".join(content.splitlines())
    content = re.sub(r"(\()([0-9一二三四五])", r"\n\1\2", content)

    return content


if __name__ == "__main__":
    input_file = "text_file/202307_航海1級_/202307_航海1級_.pdf_5.txt"
    print(replace_commas(input_file))
    