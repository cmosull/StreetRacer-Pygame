import csv

def check_scores(total_score):
    r2 = csv.reader(open('scores.csv', newline=''))
    lines2 = list(r2)
    cnt = 0
    for row2 in lines2:
        if (cnt != 0):
            if (int(total_score) > int(row2[1])):
                return True
        
        cnt+=1


def high_score_add(score):
    new_score_check = 0
    count = 0
    newname = " "

    r = csv.reader(open('scores.csv', newline=''))
    lines = list(r)

    for row in lines:
        if (row[0] == 'None' and count > 1 and new_score_check == 0):
            break

        if (count >= 1):
            if (int(score) > int(row[1])):
                oldname = row[0]
                oldscore = row[1]
                row[0] = newname
                row[1] = score
                newname = oldname
                score = oldscore
                new_score_check = 1           

        count+=1

    w = csv.writer(open('scores.csv', 'w', newline=''))
    w.writerows(lines)

def read_data():
    r3 = csv.reader(open('scores.csv', newline=''))
    return list(r3)
        
def add_name(new_name, the_score):
    new_score_check = 0
    count = 0

    r = csv.reader(open('scores.csv', newline=''))
    lines4 = list(r)

    for rows4 in lines4:
        if (rows4 == ' ' and the_score == rows4[1]):
            rows4[0] = new_name
            break

    w4 = csv.writer(open('scores.csv', 'w', newline=''))
    w4.writerows(lines4)