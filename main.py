import re


def replace_commas(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # コンマを全角コンマに置換
    content = content.replace(",", "、")

    # 数字の後に"口)"がある場合、"()"に置換
    content = content.replace("口)", "()")

    # 全角コンマの後に空文字削除
    content = re.sub(r"、\s", "、", content)

    # 改行をリセット
    content = "".join(content.splitlines())

    # "(" の後にアラビア数字または漢数字がある場合、その前に改行を追加
    content = re.sub(r"(\()([0-9一二三四五])", r"\n\1\2", content)

    # 数字の後に"H"ががある場合、その前に改行を追加
    content = re.sub(r"([0-9])H", r"\n\1H", content)

    # "。"の後に改行を追加、ただし")"の場合を除く
    # content = re.sub(r"。(?!\))", r"。\n", content)
    content = re.sub(r"。(?!\))", r"。\n", content)

    return content


if __name__ == "__main__":
    input_file = "text_file/202310_航海1級_航海/202310_航海1級_航海.pdf_5.txt"
    print(replace_commas(input_file))
