#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.
    Worst case runtime O(n * len(pattern))?"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    i = 0
    if len(pattern) == 0:
        return True
    while i < len(text):
        if text[i] == pattern[0]:
            j = 0
            while j < len(pattern):
                if text[i + j] != pattern[j]:
                    break
                j += 1
            if j == len(pattern):
                return True
        i += 1
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    Worst case runtime O(n * len(pattern))?"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    i = 0
    answer = []
    if len(pattern) == 0:
        return 0
    answer = find_all_indexes(text, pattern)
    if len(answer) > 0:
        return answer[0]
    else:
        return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Worst case runtime O(n * len(pattern))?"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    i = 0
    answer = []
    while i < len(text):
        if len(pattern) == 0 or text[i] == pattern[0]:
            answer.append(i)
            j = 0
            while j < len(pattern):
                if j + i > len(text) - 1 or text[i + j] != pattern[j]:
                    answer.pop()
                    break
                j += 1
            if j == len(pattern):
                j = 0
        i += 1
    return answer


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
