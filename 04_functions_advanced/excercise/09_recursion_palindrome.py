def palindrome(word, index):
    # reversed_word = word[::-1]
    # if word == reversed_word:
    #     return f'{word} is a palindrome'
    # else:
    #     return f'{word} is not a palindrome'
    if index == len(word) // 2:
        return f'{word} is a palindrome'
    if word[index] != word[-index - 1]:
        return f'{word} is not a palindrome'
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
