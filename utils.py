import json
import logging

def save_results(data, output, is_list=False):
    with open(output, 'w') as f:
        if is_list:
            if isinstance(data, list):
                for item in data:
                    f.write(f"{item}\n")
        else:
            json.dump(data, f, indent=4)
    logging.info(f"Results saved to {output}")
