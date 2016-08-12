# Author = CCortello
# Date = 8/12/2016

"""Description"""


def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict):
                if not v:
                    result["/".join((path + (k,)))] = ""
                else:
                    stack.append([path + (k,), v])
            else:
                result["/".join((path + (k,)))] = v
    return result

print(flatten({"name": {
    "first": "One",
    "last": "Drone"},
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}}}))

# if __name__ == '__main__':
#     assert flatten({"name": {
#                         "first": "One",
#                         "last": "Drone"},
#                     "job": "scout",
#                     "recent": {},
#                     "additional": {
#                         "place": {
#                             "zone": "1",
#                             "cell": "2"}}}
#     ) == {"name/first": "One",
#           "name/last": "Drone",
#           "job": "scout",
#           "recent": "",
#           "additional/place/zone": "1",
#           "additional/place/cell": "2"}
