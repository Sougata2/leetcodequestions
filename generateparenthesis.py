def generate_paranthesis(n, s=[], opening=0, closing=0, ans=[]):
    if len(s) == 2*n:
        ans.append("".join(s))

    if opening < n:
        s.append("(")
        generate_paranthesis(n, s, opening+1, closing, ans)
        s.pop()

    if closing < opening:
        s.append(")")
        generate_paranthesis(n, s, opening, closing+1, ans)
        s.pop()

    return ans


print(generate_paranthesis(3))
