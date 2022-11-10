import json
path = '/Users/kpham/Desktop/combio_clean/oral_histories_array.json'

with open(path,'r') as in_json_file:

  # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)

    for json_obj in json_obj_list:
        filename=json_obj['_id']
        # print(filename['$oid'])

        with open(filename['$oid'], 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`
            json.dump(json_obj, out_json_file, indent=4)