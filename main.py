import re

def replace_commas(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # コンマを全角コンマに置換
    content = content.replace(',', '、')

    # 改行をリセット
    content = "".join(content.splitlines())

    # "(" の後にアラビア数字または漢数字がある場合、その前に改行を追加
    content = re.sub(r"(\()([0-9一二三四五])", r"\n\1\2", content)

    return content


if __name__ == "__main__":
    input_file = "text_file/202307_航海1級_/202307_航海1級_.pdf_5.txt"
    print(replace_commas(input_file))
    