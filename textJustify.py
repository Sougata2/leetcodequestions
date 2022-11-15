def text_justify(words: list[str], maxWidth: int):
    n = len(words)
    justified_text = []
    sixteen_character_set = []
    space_left = maxWidth
    i = 0
    while i <= n:
        if i == n:
            if len(sixteen_character_set) > 1:
                space_in_between = space_left // (
                    len(sixteen_character_set) - 1)
                seperator = " " * space_in_between
                justified_text.append([seperator.join(sixteen_character_set)])
            else:
                justified_text.append(
                    [sixteen_character_set[-1] + " " * space_left])
            break
        word = words[i]
        if len(word) < space_left:
            if not sixteen_character_set:
                sixteen_character_set.append(word)
                space_left -= len(word)
                i += 1
                continue

            if (space_left - len(word)) // (len(sixteen_character_set)) >= 1:
                sixteen_character_set.append(word)
                space_left -= len(word)
                i += 1
            else:
                if len(sixteen_character_set) > 1:
                    space_in_between = space_left // (
                        len(sixteen_character_set) - 1)
                    seperator = " " * space_in_between
                    justified_text.append(
                        [seperator.join(sixteen_character_set)])
                else:
                    justified_text.append(
                        [sixteen_character_set[-1] + " " * space_left])
                space_left = maxWidth
                sixteen_character_set.clear()
        else:
            if len(sixteen_character_set) > 1:
                space_in_between = space_left // (
                    len(sixteen_character_set) - 1)
                seperator = " " * space_in_between
                justified_text.append([seperator.join(sixteen_character_set)])
            else:
                justified_text.append(
                    [sixteen_character_set[-1] + " " * space_left])
            space_left = maxWidth
            sixteen_character_set.clear()

    return justified_text


print(text_justify(["What", "must", "be",
      "acknowledgment", "shall", "be"], 16))
print(text_justify(["This", "is", "an", "example",
                    "of", "text", "justification."], 16))
print(text_justify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], 20))
