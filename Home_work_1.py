lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

correct_result_as_example = [
    (34587, 164),
    (98762, 284),
    (77226, 109),
    (88112, 85),
]
# result_order = list(map(lambda x: x[0], lst))
# result_total_value = list(
#     map(lambda x: round(x[2] * x[3]) + 10 if round(x[2] * x[3]) < 100 else round(x[2] * x[3]), lst))
# result = [(i, j) for i, j in zip(result_order, result_total_value)]
# print(result)

# result = [(i, j) for i, j in zip(list(map(lambda x: x[0], lst)), list(
#     map(lambda x: round(x[2] * x[3]) + 10 if round(x[2] * x[3]) < 100 else round(x[2] * x[3]), lst)))]
# print(result)


res = list(map(lambda x: (x[0], round(x[2] * x[3]) + 10 if round(x[2] * x[3]) < 100 else round(x[2] * x[3])), lst))
print(res)
