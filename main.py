import re

# text_fileの変数
examdate = "202404"
navigation_or_engineering = "航海"
subject = "航海"
grade = "1級"
text_file_num = 1


def digit_to_kanji(digit):
    kanji_numbers = ["〇", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
    return kanji_numbers[int(digit)]


# 関数を使用して'()'内の数字を漢数字に置換
def replace_digits_with_kanji(match):
    return f"({digit_to_kanji(match.group(1))})"


# 任意の文字を置換
def replace_arbitrary_characters(content):
    # コンマを全角コンマに置換
    content = content.replace(",", "、")

    # "~"を"〜"に置換
    content = content.replace("~", "〜")

    # 数字の後に"口)"がある場合、"()"に置換
    content = content.replace("口)", "()")

    return content


# 改行を追加
def add_line_break(content):
    # "(" の後にアラビア数字または漢数字がある場合、その前に改行を追加
    content = re.sub(r"(\()([0-9一二三四五])", r"\n\1\2", content)

    # 数字の後に"H"ががある場合、その前に改行を追加
    content = re.sub(r"([0-9])H", r"\n\1H", content)

    # "。"の後に改行を追加、ただし")"の場合を除く
    content = re.sub(r"。(?!\))", r"。\n", content)

    return content


# 改行を削除
def delete_line_break(content):
    # "また"の前に改行がある場合、その改行を削除
    content = re.sub(r"\nまた", r"また", content)
    content = re.sub(r"\n また", r"また", content)

    # "〜"の後に改行がある場合、その改行を削除
    content = re.sub(r"〜\n", r"〜", content)

    # "の"の後に改行がある場合、その改行を削除
    content = re.sub(r"の\n", r"の", content)

    # "び"の後に改行がある場合、その改行を削除
    content = re.sub(r"び\n", r"び", content)

    # "理"の前に改行がある場合、その改行を削除
    content = re.sub(r"。\n理", r"。理", content)
    content = re.sub(r"。\n 理", r"。理", content)

    # "計"の前に改行がある場合、その改行を削除
    content = re.sub(r"。\n計", r"。計", content)
    content = re.sub(r"。\n 計", r"。計", content)

    # "次"の前に改行がある場合、その改行を削除
    content = re.sub(r"。\n次", r"。次", content)
    content = re.sub(r"。\n 次", r"。次", content)

    # "ただし"の前に改行がある場合、その改行を削除
    content = re.sub(r"。\n ただし", r"。ただし", content)
    content = re.sub(r"。\nただし", r"。ただし", content)

    # "◯つあげよ。"の前に改行がある場合、その改行を削除
    content = re.sub(r"。\n (\d)つあげよ。", r"。\1つあげよ。", content)

    # "図示して説明せよ。"の前に改行がある場合、その改行を削除
    content = re.sub(r"。\n 図示して説明せよ。", r"。図示して説明せよ。", content)
    content = re.sub(r"。\n図示して説明せよ。", r"。図示して説明せよ。", content)

    return content


# スペースを作成
def add_space(content):
    # "改行(数字)"の後にスペースを追加
    content = re.sub(r"(\n\(\d\))(?! )(\D)", r"\1 \2", content)

    # "改行(漢数字)"の後にスペースを追加
    content = re.sub(r"(\n\([一二三四]\))(?! )(\D)", r"\1 \2", content)

    return content


# 漢数字に変換
def replace_str_to_kanjinum(content):
    # "(一)に変換"
    content = content.replace("(土)", " (一)").replace("台)", " (一)")
    content = re.sub(r"(\d+)H\)", r"\1 (一) ", content)

    return content


def replace_commas(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # 任意の文字を置換
    content = replace_arbitrary_characters(content)

    # 全角コンマの後に空文字削除
    content = re.sub(r"、\s", "、", content)

    # 改行をリセット
    content = "".join(content.splitlines())

    # '()'内の数字を漢数字置換
    # content = re.sub(r"\((\d)\)", replace_digits_with_kanji, content)

    # 改行を追加
    content = add_line_break(content)

    # 改行を削除
    content = delete_line_break(content)

    # スペースを作成
    content = add_space(content)

    # 漢数字に変換
    content = replace_str_to_kanjinum(content)

    return content


if __name__ == "__main__":
    input_file = (
        f"text_file/{examdate}_{navigation_or_engineering}{grade}_{subject}/"
        f"{examdate}_{navigation_or_engineering}{grade}_{subject}.pdf_{text_file_num}.txt"
    )
    print(replace_commas(input_file))
