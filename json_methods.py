import json
def json_load(file)->any:
    with open(file,"r+") as f: 
        d=json.load(f)
        return d

def json_update(file,Category,updates):
    with open(file,"r+") as f:
            d=json.load(f)
            d.update({Category:updates}) 
            f.seek(0)
            json.dump(d,f)