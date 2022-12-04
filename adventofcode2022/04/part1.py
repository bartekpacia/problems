def overlaps(a: range, b: range) -> bool:
    

with open("sample.txt") as file:
    common: list[str] = []

    for l in file:
        line = l.strip().split(",")
        first_section = list(map(lambda x: int(x), line[0].split("-")))
        second_section = list(map(lambda x: int(x), line[1].split("-")))

        if first_section[0] < second_section[0]:
            section_start = 'first'
            begin = first_section[0]
        elif second_section[0] < first_section[0]:
            section_start = 'second'
            begin = second_section[0]
        else: # equal start
            begin = first_section[0]
            section_start = 'both'

        if first_section[1] > second_section[1]:
            section_end = 'first'
            end = first_section[1]
        elif second_section[1] > first_section[1]:
            section_end = 'second'
            end = second_section[1]
        else: # equal end
            begin = first_section[1]
            section_end = 'both'

        if (
            (section_start == section_end) or
            (section_start == 'both' and second)
            ):
            print(f'fully contained: {line}')


        # print(f"{first_section=}, {second_section=}")
