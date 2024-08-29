import re

# text_fileの変数
examdate = "202402"
navigation_or_engineering = "航海"
subject = "航海"
grade = "2級"
text_file_num = 0


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

    # 航海1級 航海大問4の場合、改行を追加
    content = re.sub(r"4 商船が一般", r"\n4 商船が一般", content)

    return content


# 改行を削除
def delete_line_break(content):
    patterns = [
        (r"〜\n", r"〜"),  # "〜"の後に改行がある場合、その改行を削除
        (r"の\n", r"の"),  # "の"の後に改行がある場合、その改行を削除
        (r"び\n", r"び"),  # "び"の後に改行がある場合、その改行を削除
        (r"\n\s*また", r"また"),  # "また"の前に改行がある場合、その改行を削除
        (r"\n\s*ただし", r"ただし"),  # "ただし"の前に改行がある場合、その改行を削除
        (
            r"\n\s*それぞれ",
            r"それぞれ",
        ),  # "それぞれ"の前に改行がある場合、その改行を削除
        (
            r"\n\s*(\d)つあげよ。",
            r"\1つあげよ。",
        ),  # "(\d)つあげよ。"の前に改行がある場合、その改行を削除
        (
            r"\n\s*(\d)つ述べよ。",
            r"\1つ述べよ。",
        ),  # "(\d)つ述べよ。"の前に改行がある場合、その改行を削除
        (r"\n\s*理", r"理"),  # "理"の前に改行がある場合、その改行を削除
        (r"\n\s*計", r"計"),  # "計"の前に改行がある場合、その改行を削除
        (r"\n\s*次", r"次"),  # "次"の前に改行がある場合、その改行を削除
        (r"\n\s*甲", r"甲"),  # "甲"の前に改行がある場合、その改行を削除
        (r"\n\s*要点", r"要点"),  # "要点"の前に改行がある場合、その改行を削除
        (r"\n\s*概要", r"概要"),  # "概要"の前に改行がある場合、その改行を削除
        (
            r"\n\s*例のほか",
            r"例のほか",
        ),  # "例のほか"の前に改行がある場合、その改行を削除
        (
            r"\n\s*図示して説明せよ。",
            r"図示して説明せよ。",
        ),  # "図示して説明せよ。"の前に改行がある場合、その改行を削除
    ]
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)

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

    # "任意の数字"+ "H" + ")の場合、"任意の数字"+"(一)"
    content = re.sub(r"(\d+)H\)", r"\1 (一) ", content)

    # "任意の数字"+ "H", "任意の数字"+"(一)"
    content = re.sub(r"(\d+)H", r"\1 (一) ", content)

    # "任意の数字"+")"の場合、"任意の数字"+"(一)"
    content = re.sub(r"(?<!\()\b(\d+)\)", r"\1 (一) ", content)

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
