import numpy as np
import json


def deal_answer():

    model_answer = np.load('example.npy',allow_pickle=True)
    category = np.load('category.npy',allow_pickle=True)

    cu_mdoel_answer = model_answer[np.where(category == '0')]
    cr_mdoel_answer = model_answer[np.where(category == '1')]
    mur_mdoel_answer = model_answer[np.where(category == '2')]
    # 0 for cu for Conceptual Understanding,
    # 1 for cr for Commonsense Reasoning, 
    # 2 for mhr for Multi-Hop Reasoning, 


    json_data = {
            'Conceptual Comprehention': {str(index): item for index, item in enumerate(cu_mdoel_answer)},
            'Commonsense Reasoning': {str(index): item for index, item in enumerate(cr_mdoel_answer)},
            'Multi-hop/Complex Reasoning': {str(index): item for index, item in enumerate(mur_mdoel_answer)},
            }

    b = json.dumps(json_data,indent=4)
    with open('example.json', 'w') as f:
        f.write(b)

    return 0



if __name__=="__main__":
    deal_answer()

    pass