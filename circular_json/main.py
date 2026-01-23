import json

serialized_arr = {
    "content": [],
    "mappings": {},
}

def encode(input_arr: list[any]) -> map:
    map: dict[str, any] = {}
    for _, element in enumerate(input_arr):
        if not isinstance(element, list):
            serialized_arr["content"].append(f"literal({element})") # int, strings, bools
        else:
            # serialized_arr["mappings"][_id] # written into by encode_elemn
            serialized_arr["content"].append(encode_elem(element))
            
    

def encode_elem(input: list[any]) -> str:
    index = -1 # index into serialized_arr.mappings

    for _, element in enumerate()
    _id = id(element)

    retrun f"ref({index})"

json.dumps(serialized_arr)


a = [1, 2]
a += a

print(a)
print(encode(a))


### --> encoding
# input: a = [1, 2, a]
# output:
#{
#    "mappings": {
#        "0": "[literal(1)", "literal(2)", "ref(0)]",
#        "1": "0"
#    }
#}

### --> encoding
# input: a = [1, 2, [3, 4]], b = []
# output:
#{
#    "original": ["literal(1)", "literal(2)", "literal([literal(3), literal(4), ref(1)]])"],
#    "mappings": {
#        "1": ""
#    }
#}


### <-- decode
# [1, 2, "id(140177850081216)"]

# output_list = []
# for elem in input_list:
#   if elem.startWith("id(")


# a = [1, 2]
# b = [3, a]
# 
# a = [1, 2, [3, a]]
