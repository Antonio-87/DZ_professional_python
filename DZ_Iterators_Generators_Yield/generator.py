def flat_generator(nested_list):
    for l in nested_list:
        for i in l:
            yield i


def flat_generator_any(nested_list):
    if isinstance(nested_list, list):   
        return sum(map(flat_generator_any, nested_list), [])
    else:
        return [nested_list]