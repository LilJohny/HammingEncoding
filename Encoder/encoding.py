from tree import Tree


def get_possibilities(phrase):
    symbols = list(set(list(phrase)))
    for i in range(len(symbols)):
        symbols[i] = symbols[i], phrase.count(symbols[i]) / len(phrase)
    return sorted(symbols, key=lambda x: x[1], reverse=True)


def sort_key(object_):
    if isinstance(object_, Tree):
        return object_.data[-1]
    else:
        return object_[-1]


def sorted_possibilities(possibilities):
    possibilities = sorted(possibilities, key=sort_key, reverse=True)
    result = []
    possibilities_vals = set(map(get_possibility, possibilities))
    for possibility_val in sorted(possibilities_vals, reverse=True):
        possibility_tuples = list(
            filter(lambda x: isinstance(x, tuple) and x[-1] == possibility_val,
                   possibilities))
        possibility_trees = list(
            filter(
                lambda x: isinstance(x, Tree) and x.data[-1] ==
                possibility_val, possibilities))
        possibility_tuples = sorted(possibility_tuples,
                                    key=lambda x: x[0],
                                    reverse=True)
        result.extend(possibility_tuples)
        result.extend(possibility_trees)
    return result


def calculate_sum_pos(object_1, object_2):
    sum_pos = 0
    if isinstance(object_1, tuple):
        sum_pos += object_1[-1]
    elif isinstance(object_1, Tree):
        sum_pos += object_1.data[-1]
    if isinstance(object_2, tuple):
        sum_pos += object_2[-1]
    elif isinstance(object_2, Tree):
        sum_pos += object_2.data[-1]
    return sum_pos


def get_possibility(encode_sym):
    if isinstance(encode_sym, tuple):
        return encode_sym[-1]
    elif isinstance(encode_sym, Tree):
        return encode_sym.data[-1]


def encode(possibilities):
    possibilities = sorted_possibilities(possibilities)
    while len(possibilities) != 1:
        f_possibility = possibilities[-1]
        s_possibility = possibilities[-2]
        f_possibility = Tree(
            ('', calculate_sum_pos(f_possibility, s_possibility)))
        if get_possibility(
                possibilities[-1]) <= get_possibility(s_possibility):
            f_possibility.left = possibilities[-1]
            f_possibility.right = s_possibility
        else:
            f_possibility.left = s_possibility
            f_possibility.right = possibilities[-1]
        del possibilities[-1]
        del possibilities[-1]
        possibilities.append(f_possibility)
        #possibilities = sorted(possibilities, key=sort_key, reverse=True)
        possibilities = sorted_possibilities(possibilities)
    return possibilities[-1]


def decode_tree(tree):
    def _decode_child(code_tree, code):
        if isinstance(code_tree.left, tuple):
            encoded = (code_tree.left[0], code + '0')
            code_tree.left = None
            if code_tree.left is None and code_tree.right is None:
                code_tree = None
            return encoded
        if isinstance(code_tree.right, tuple):
            encoded = (code_tree.right[0], code + '1')
            code_tree.right = None
            if code_tree.left is None and code_tree.right is None:
                code_tree = None
            return encoded
        if isinstance(code_tree.left, Tree):
            if code_tree.left.left is None and code_tree.left.right is None:
                code_tree.left = None
            else:
                return _decode_child(code_tree.left, code + '0')
        if isinstance(code_tree.right, Tree):
            if code_tree.right.left is None and code_tree.right.right is None:
                code_tree.right = None
                return -1
            else:
                return _decode_child(code_tree.right, code + '1')

    result = []
    encoded_sym = 0
    while encoded_sym is not None:
        encoded_sym = _decode_child(tree, "")
        if encoded_sym is not None:
            result.append(encoded_sym)
    return result


phrase = "hello"
p = get_possibilities(phrase)
print(p)
t = encode(p)
rez = decode_tree(t)
rez = list(filter(lambda x: x != -1, rez))
rez = dict(rez)

print(phrase.translate(str.maketrans(rez)))
print(rez)
k = 0
