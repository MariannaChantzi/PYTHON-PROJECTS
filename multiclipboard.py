# Libraries
import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}
    
def delete_data(filepath, data, key):
    del data[key]
    with open(filepath, 'w') as f:
        json.dump(data,f)


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key to save this data under: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data saved!")

    elif command == 'load':
        key = input('Enter the key to be loaded: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print('Error! No such key exists.')
        
    elif command == 'list':
        print(data)
    
    elif command == 'delete':
        key = input('Enter the key to be deleted: ')
        if key in data:
            delete_data(SAVED_DATA, data, key)
            print('Data deleted from clipboard.')
        else:
            print('Error! No such key exists.')
    
    else:
        print('Unknown command')

else:
    print('Please pass exactly one command')
