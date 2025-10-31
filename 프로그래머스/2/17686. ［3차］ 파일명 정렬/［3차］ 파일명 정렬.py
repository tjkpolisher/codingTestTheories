import re
def solution(files):
    def split_file(file):
        match = re.match(r'([a-zA-Z\-\.\s]+)(\d{1,5})', file)
        head, number = match.group(1), match.group(2)
        return head, number
    
    answer = sorted(
        files,
        key=lambda x: (
            split_file(x)[0].lower(),
            int(split_file(x)[1])
        )
    )
    
    return answer