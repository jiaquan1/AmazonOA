def reorderlogfiles(logs):
    for log in logs:
        if not log:
            logs.remove(log)
    return sorted(logs,key = sort)
def sort(logs):
    
    a,b = logs.split(' ',1)
    a=a.lower()
    b=b.lower()
    if b[0].isalpha():
        return (0,b,a)
    else:
        return (1,None,None)
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderlogfiles(logs))


