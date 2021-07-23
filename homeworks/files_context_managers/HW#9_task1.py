"""
Task 1

У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст
складається з міток часу і репліки яка була сказана в той момент часу.
Причому репліка знаходиться в наступному рядку після мітки часу.
Прочитайте вміст файлу

Результатом виконнання завдання повинно бути:
1. словник елементами якого буде пара ключ:значення де ключ - мітка часу,
значення - репліка в даний момент часу

2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі
субтитри повинні мати вигляд простого тексту.
Це означає що окрім видалення міток часу, вам потрібно видалити переноси
рядків

"""


def make_dict(file_name):
    dict_ = {}
    file = open(file_name)
    while True:
        key = file.readline().strip('\n')
        if key == '':      # stop iteration
            break
        dict_[key] = file.readline().strip('\n')
    file.close()
    return dict_


def make_file(file_name):
    file = open(file_name)
    text = []
    new_file = open('new_file.txt', 'w')
    while True:
        flag = file.readline()
        if flag == '':
            break
        text.append(file.readline().strip('\n'))
    new_file.write(' '.join(text))
    file.close()
    new_file.close()
    return 'new_file.txt'


print("*** Task 1.1 ***\n", make_dict("task1.txt"))

file = open(make_file('task1.txt'))
print("\n*** Task 1.2 ***\n", file.read())
file.close


# *** Task 1.1 ***
#  {'00:00': 'We all know you should take a sick day', '00:01': 'or a mental health day', '00:03': 'or even a personal day.', '00:04': 'But a financial day is just as important.', '00:07': '[Your Money and Your Mind with Wendy De La Rosa]', '00:11': 'You deserve to take time to get your life in order', '00:14': "when you aren't on edge and under pressure.", '00:16': "Employers, if you're watching this: you should also think about", '00:20': 'giving your employees a financial health day.', '00:22': 'Throughout this series,', '00:23': "I've shared ways that you can change your environment", '00:26': 'so you can spend less and save more.', '00:28': 'But the secret ingredient for each tip has been time:', '00:31': 'calling your credit card company to change your interest rate takes time;', '00:35': 'deleting an app off your phone takes time.', '00:37': "And if you haven't had time to put these changes into action,", '00:41': 'this is your chance.', '00:42': 'Mark a day on your calendar right now', '00:45': 'to devote to reorganizing your finances.', '00:47': 'Really commit to this day', '00:49': 'and make that day as productive as possible.', '00:52': 'But here are the big headlines that are the most important to cover,', '00:55': 'both from earlier episodes and beyond.', '00:58': 'So first I want you to focus on your fixed expenses.', '01:01': 'Take the day to evaluate your bills.', '01:03': 'Can you truly afford your housing payment?', '01:06': 'Is it time to start looking for a cheaper place?', '01:08': 'Do you need to switch to a low-cost cell phone provider?', '01:11': 'Do you need to trade in your car for something else?', '01:14': 'This is the day where I really want you to think about', '01:16': 'those large fixed expenses', '01:18': 'and make that one-time change.', '01:20': 'Number two: sign up for the boring-but-necessary stuff.', '01:24': 'Do you have life insurance?', '01:25': 'No? Sign up now.', '01:26': "Are you enrolled in your company's 401(k)?", '01:29': 'No? Sign up now.', '01:30': 'Are you contributing enough to that 401(k)?', '01:32': 'No? Edit your contribution rate right now.', '01:35': "Number three: if you haven't already,", '01:37': 'talk to your significant other about money.', '01:39': 'Get on the same page; it matters.', '01:42': 'Visit the link below for a list of questions', '01:44': 'to help get you started.', '01:46': 'Number four: create a singular savings goal.', '01:49': 'You can start by setting up an automatic plan', '01:51': 'so that a portion of every paycheck', '01:53': 'goes directly into your savings account.', '01:55': 'Number five: start paying off your debt every week,', '01:58': 'not just every month.', '02:00': "Maybe it's your credit card debt", '02:01': 'or your mortgage debt or whatever you have,', '02:03': "you'll end up reducing more of your debt over the course of a year", '02:07': 'if you pay that debt more often.', '02:09': 'Number six: renegotiate your credit card interest rate', '02:12': 'and change your payment due date.', '02:14': 'Get on the phone, call your credit card company', '02:17': 'and make your credit card company work for you.', '02:19': 'Number seven: use technology to your advantage.', '02:22': 'Redesign your online environment', '02:24': 'by unsubscribing from all your shopping newsletters', '02:28': 'and install an ad blocker.', '02:29': "You can't spend on what you can't see.", '02:32': 'Number eight: delete those distracting delivery apps.', '02:35': 'Number nine:', '02:37': 'now, my tips are not all about cutting back spending.', '02:39': 'I want you to spend on things that increase your happiness.', '02:43': 'So focus on experiences, on spending time with others', '02:46': 'and on expenditures that help save you time,', '02:49': 'like hiring someone to clean your house', '02:51': 'or mow your lawn.', '02:53': 'That will save you time and boost your happiness.', '02:56': 'Number 10: last but certainly not least,', '02:59': 'schedule another financial health day', '03:01': 'for a few weeks later.', '03:02': "Chances are, you'll need to revisit some of the things", '03:05': 'you started today.', '03:06': 'I know all of this may seem tedious or boring,', '03:08': "but it's better to make these vital changes", '03:11': 'when you have the time to think about them,', '03:13': 'and not under the stressful conditions', '03:15': 'when we usually make these very important decisions.', '03:18': 'Not every day can be a spa day,', '03:20': 'but I think a financial day', '03:22': 'will leave you feeling soothed and pampered.'}
#
# *** Task 1.2 ***
#  We all know you should take a sick day or a mental health day or even a personal day. But a financial day is just as important. [Your Money and Your Mind with Wendy De La Rosa] You deserve to take time to get your life in order when you aren't on edge and under pressure. Employers, if you're watching this: you should also think about giving your employees a financial health day. Throughout this series, I've shared ways that you can change your environment so you can spend less and save more. But the secret ingredient for each tip has been time: calling your credit card company to change your interest rate takes time; deleting an app off your phone takes time. And if you haven't had time to put these changes into action, this is your chance. Mark a day on your calendar right now to devote to reorganizing your finances. Really commit to this day and make that day as productive as possible. But here are the big headlines that are the most important to cover, both from earlier episodes and beyond. So first I want you to focus on your fixed expenses. Take the day to evaluate your bills. Can you truly afford your housing payment? Is it time to start looking for a cheaper place? Do you need to switch to a low-cost cell phone provider? Do you need to trade in your car for something else? This is the day where I really want you to think about those large fixed expenses and make that one-time change. Number two: sign up for the boring-but-necessary stuff. Do you have life insurance? No? Sign up now. Are you enrolled in your company's 401(k)? No? Sign up now. Are you contributing enough to that 401(k)? No? Edit your contribution rate right now. Number three: if you haven't already, talk to your significant other about money. Get on the same page; it matters. Visit the link below for a list of questions to help get you started. Number four: create a singular savings goal. You can start by setting up an automatic plan so that a portion of every paycheck goes directly into your savings account. Number five: start paying off your debt every week, not just every month. Maybe it's your credit card debt or your mortgage debt or whatever you have, you'll end up reducing more of your debt over the course of a year if you pay that debt more often. Number six: renegotiate your credit card interest rate and change your payment due date. Get on the phone, call your credit card company and make your credit card company work for you. Number seven: use technology to your advantage. Redesign your online environment by unsubscribing from all your shopping newsletters and install an ad blocker. You can't spend on what you can't see. Number eight: delete those distracting delivery apps. Number nine: now, my tips are not all about cutting back spending. I want you to spend on things that increase your happiness. So focus on experiences, on spending time with others and on expenditures that help save you time, like hiring someone to clean your house or mow your lawn. That will save you time and boost your happiness. Number 10: last but certainly not least, schedule another financial health day for a few weeks later. Chances are, you'll need to revisit some of the things you started today. I know all of this may seem tedious or boring, but it's better to make these vital changes when you have the time to think about them, and not under the stressful conditions when we usually make these very important decisions. Not every day can be a spa day, but I think a financial day will leave you feeling soothed and pampered.
#
