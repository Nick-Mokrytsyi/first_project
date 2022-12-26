def open_file(file="requirements.txt") -> str:
    num_list = []
    with open(file) as file:
        text = file.read().split()
        for count, name in enumerate(text):
            num_list.append(f'{count+1}. {name}\n')
        convert_text = ' '.join(map(str, num_list))
        finale_text = convert_text.strip().replace('\n', '<br>')
        return finale_text


string_html = open_file()
