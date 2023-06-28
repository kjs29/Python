
# 
#     histogram function takes str as a parameter,
#         str: String, sentences or paragraphs to be assessed.
#     , returns object { word: frequency }
#   
def histogram(string):
    arr = string.replace('\n', ' ').split(' ')
    answer = {}
    for each_word in arr:
        if each_word in answer:
            answer[each_word] += 1
        else:
            answer[each_word] = 1
    return answer


def sort_by_value(obj, trim):
    entries = sorted(obj.items(), key=lambda x: x[1], reverse=True)[:trim]
    return dict(entries)


def delete_useless_words(string, excluded_words):
    string = string.replace('\n', '').replace(':', '').replace('.', '').replace(',', '').lower()
    words = string.split(' ')

    words = [word for word in words if word not in excluded_words]
    return ' '.join(words)
