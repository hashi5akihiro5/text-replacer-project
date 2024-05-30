import re

def replace_commas(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # コンマを全角コンマに置換
    content = content.replace(',', '、')

    # 全角コンマの後に空文字削除
    content = re.sub(r'、\s', '、', content)

    # 改行をリセット
    content = "".join(content.splitlines())

    # "(" の後にアラビア数字または漢数字がある場合、その前に改行を追加
    content = re.sub(r"(\()([0-9一二三四五])", r"\n\1\2", content)

    # アラビア数字の後に"H"ががある場合、その前に改行を追加
    content = re.sub(r"([0-9])H", r"\n\1H", content)

    # "。"の後に改行を追加
    content = re.sub(r"。", r"。\n", content)

    return content


if __name__ == "__main__":
    input_file = "text_file/202307_航海3級_航海/202307_航海3級_航海.pdf_2.txt"
    print(replace_commas(input_file))
    