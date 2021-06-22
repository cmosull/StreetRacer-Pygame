import csv
import game

player_name = str()

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
    newname = 'Your Initials Here'

    r = csv.reader(open('scores.csv', newline=''))
    lines = list(r)

    for row in lines:
        if (count >= 1):
            if (int(score) >= int(row[1])):
                oldname = row[0]
                oldscore = row[1]
                row[0] = newname
                row[1] = score
                newname = oldname
                score = oldscore
                new_score_check = 1       

        count+=1

    if (new_score_check == 0 and int(score) > int(row[1])):
        oldname = row[0]
        oldscore = row[1]
        row[0] = newname
        row[1] = score
        newname = oldname
        score = oldscore
        new_score_check = 1

    w = csv.writer(open('scores.csv', 'w', newline=''))
    w.writerows(lines)
        
def add_name(new_name):
    r = csv.reader(open('scores.csv', newline=''))
    lines4 = list(r)

    check_name = 0
    counter = 0
    game.first_time_check = 1

    for rows4 in lines4:
        if (counter != 0):
            if (int(game.TotalScore) == int(rows4[1])):
                check_name = 1
                rows4[0] = str(new_name)
                break

        counter+=1
    
    if (check_name == 0 and int(game.TotalScore) == int(rows4[1])):
        rows4[0] = str(new_name)
    
    w4 = csv.writer(open('scores.csv', 'w', newline=''))
    w4.writerows(lines4)