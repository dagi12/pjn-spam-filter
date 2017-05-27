#!/usr/bin/python3.5
import csv

from sklearn.linear_model import LogisticRegression

from Mail import Mail

junk_training_set = []
desired_training_set = []
test_set = []


def init_training_set():
    with open('res/desired/index.csv') as csvfile:
        desired_mail_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in desired_mail_reader:
            desired_training_set.append(Mail(row, False))

    with open('res/junk/index.csv') as csvfile:
        junk_mail_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in junk_mail_reader:
            junk_training_set.append(Mail(row, True))


def init_logistic_regression():
    lr = LogisticRegression()
    jts_arr = [[jts.word_count, jts.sign_count] for jts in junk_training_set]
    dts_arr = [[dts.word_count, dts.sign_count] for dts in desired_training_set]
    training_set = jts_arr + dts_arr
    target_set = ([0] * len(junk_training_set) + [1] * len(desired_training_set))
    lr.fit(training_set, target_set)
    return lr


def predict_test_mails():
    lr = init_logistic_regression()
    for mail in test_set:
        mail.is_junk_predicted = lr.predict([mail.word_count, mail.sign_count])


def check_prediction_result():
    positive_prediction_count = 0
    for mail in test_set:
        if mail.is_junk == mail.is_junk_predicted:
            positive_prediction_count += 1
    print("Skuteczność wynosi: ", round(positive_prediction_count / len(test_set), 4) * 100, "%")


def init_test_set():
    with open('test/desired/index.csv') as csvfile:
        desired_mail_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in desired_mail_reader:
            test_set.append(Mail(row))
    with open('test/junk/index.csv') as csvfile:
        junk_mail_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in junk_mail_reader:
            test_set.append(Mail(row, True))


init_training_set()
init_test_set()
predict_test_mails()
check_prediction_result()
