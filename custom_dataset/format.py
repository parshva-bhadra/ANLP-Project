import json

def modify_json(file_name):
    file = open(file_name, 'r')
    json_file = json.load(file)

    modified_json = []
    for id, input_dict in enumerate(json_file):
        answers = []
        for s_ans in input_dict['answers']:
            answer = {}
            answer['title'] = ""
            answer['text'] = ''
            for s in s_ans['sents']:
                answer['text'] += s['text']
            answers.append(answer)
            
        output_dict = {
            'id': str(id),
            'question': input_dict['question']['question'],
            'target': input_dict['summaries'][0][0],
            'answers': input_dict['summaries'][0],
            'ctxs': answers,
        }
        
        modified_json.append(output_dict)

    output_filename = file_name.split('.')[0] + "_mod.json"
    with open(output_filename, 'w') as f:
        json.dump(modified_json, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    modify_json('answersumm_train.json')
    modify_json('answersumm_validation.json')
    modify_json('answersumm_test.json')
