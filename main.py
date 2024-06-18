import re


def digit_to_kanji(digit):
    kanji_numbers = ["〇", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    return kanji_numbers[int(digit)]


# 関数を使用して'()'内の数字を漢数字に置換
def replace_digits_with_kanji(match):
    return f"({digit_to_kanji(match.group(1))})"


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

    # '()'内の数字を漢数字置換
    # content = re.sub(r"\((\d)\)", replace_digits_with_kanji, content)

    # 数字の後に"H"ががある場合、その前に改行を追加
    content = re.sub(r"([0-9])H", r"\n\1H", content)

    # "~"の後に改行がある場合、その改行を削除
    content = re.sub(r"~\n", r"~", content)

    # "。"の後に改行を追加、ただし")"の場合を除く
    content = re.sub(r"。(?!\))", r"。\n", content)

    return content


if __name__ == "__main__":
    input_file = "text_file/202402_航海1級_航海/202402_航海1級_航海.pdf_1.txt"
    print(replace_commas(input_file))
