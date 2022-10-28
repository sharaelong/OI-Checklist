from sys import stdin, stderr

checklist = {}
accepted_problems = []

curr_contest = ''
curr_year = ''

for line in stdin:
    line = line.strip('\n')
    args = line.split('\t')
    
    if len(args[0]):
        if args[0].isdigit():
            problem_id = args[0]
            accepted_problems.append(problem_id)
        else:
            contest = args[0]
            year = args[1]
            if contest not in checklist:
                checklist[args[0]] = {}
            if year not in checklist[args[0]]:
                checklist[contest][year] = []
            curr_contest = contest
            curr_year = year
    else:
        if len(args) >= 3:
            problem_id = args[1]
            problem_name = args[2]
            checklist[curr_contest][curr_year].append((problem_id, problem_name))

# print(checklist, file=stderr)

html = '''
<!DOCTYPE html>
<html>
<head><title>OI Checklist</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<style>
table tr td { border: 1px solid black; }
table { border-collapse: collapse; }
td { width: 150px; font-size: 18px; height: 40px; text-align: center; }
td#ac { background-color: #CCFF99; }
a { all: unset; }
a:hover { text-decoration: underline; }
</style>
<body>
'''

for contest in checklist:
    html += '<h2>{}</h2>'.format(contest)
    html += '<table><tbody>'
    for year in checklist[contest]:
        row = '<tr><td><b>{}</b></td>'.format(contest + ' ' + year)
        problem_list = checklist[contest][year]
        for (problem_id, problem_name) in problem_list:
            url = 'https://boj.kr/{}'.format(problem_id)
            row += '<td{}><a href={} target=_blank>{}</a></td>'.format(' id="ac"' if problem_id in accepted_problems else '', url, problem_name)
        row += '</tr>'
        html += row
    html += '</tbody></table>'

html += '</body></html>'
print(html)
