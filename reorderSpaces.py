def reorder_spaces(text: str):
    spaces = 0
    words = []

    # adding extra space for ease in word seperation
    extra_space_added = 0
    if text[0] != " " or text[-1] != " ":
        if text[0] != " ":
            text = " "+text
            extra_space_added += 1
        if text[-1] != " ":
            text += " "
            extra_space_added += 1

    # seperating the words from the text
    i = 0
    while i < len(text):
        # word that will will take the alphabetical characters.
        word = ""

        # counting the spaces and continue when done
        # so that we donot append empty space into words.
        if not text[i].isalpha():
            if text[i] == " ":
                spaces += 1
            i += 1
            continue

        # seperating the words from the text appending to the words
        while text[i].isalpha():
            word += text[i]
            i += 1
        words.append(word)

    # remove the extra space that were added earlier.
    spaces -= extra_space_added


    # words less 2 does not get spaces in between.
    if len(words) > 1:
    # equaly distributed spaces between the words
        space_btw_words = spaces // (len(words) - 1)


    # adding the word to ans with space after it
    reordered_space_text = ""
    remaining_spaces_for_use = spaces

    for i in range(len(words)):
        if i == len(words)-1:
            # at n-1 index only add the word and break
            reordered_space_text += words[i]
            break

        reordered_space_text += words[i] + " "*space_btw_words
        remaining_spaces_for_use -= space_btw_words

    if remaining_spaces_for_use:
        reordered_space_text += " "*remaining_spaces_for_use

    return reordered_space_text


if __name__ == "__main__":
    view_list = []
    view_list.append(reorder_spaces("                "))
    view_list.append(reorder_spaces("                a"))
    view_list.append(reorder_spaces("  this   is  a sentence "))
    view_list.append(reorder_spaces(" practice   makes   perfect"))
    print(view_list)
