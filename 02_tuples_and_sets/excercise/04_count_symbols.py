text = input()
text_set = set(text)
to_print = sorted(list(text_set))
for sym in to_print:
    print(f'{sym}: {text.count(sym)} time/s')
