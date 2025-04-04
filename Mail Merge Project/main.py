with open("Input/Names/invited_names.txt",mode='r') as name:
    content=name.readlines()
for selected_name in content:
    with open("Input/Letters/starting_letter.txt", mode='r') as envelop:
        body = envelop.read()
    stripped_name=selected_name.strip()
    with open(f"Output/ReadyToSend/{stripped_name}.txt",mode='w') as letter:
        body=body.replace("[name]",stripped_name)
        letter.write(body)
