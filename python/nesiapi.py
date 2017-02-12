import urllib.request
import requests
import json
import xlsxwriter


def create_customer(first_name, last_name, street_number, street_name, city, state, zipp):
    url = 'http://api.reimaginebanking.com/customers?key=75ca43c1c9a8ea978abcc0c4bf5f56d7'
    payload = {
      "first_name": first_name,
      "last_name": last_name,
      "address": {
        "street_number": street_number,
        "street_name": street_name,
        "city": city,
        "state": state,
        "zip": zipp
      }
    }
    response = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'},)
    if response.status_code == 201:
        print('Customer created')


def create_account(accid, typ, nickname, rewards, balance):
    url = 'http://api.reimaginebanking.com/customers/' + accid + '/accounts?key=75ca43c1c9a8ea978abcc0c4bf5f56d7'
    payload = {
            "type": typ,
            "nickname": nickname,
            "rewards": rewards,
            "balance": balance
        }
    response = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}, )
    if response.status_code == 201:
        print('Account created')


def view_customers():
    inputurl = "http://api.reimaginebanking.com/customers?key=75ca43c1c9a8ea978abcc0c4bf5f56d7"
    stream = urllib.request.urlopen(inputurl)
    result = []
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        result.append(decoded)

    result = "".join(result)
    result = result.strip("[").strip("{").strip("]")
    result = result.split("},{")

    for y in range(len(result)):
        result[y] = result[y].replace('"', "")
        result[y] = result[y].replace('{', '')
        result[y] = result[y].replace('}', '')
        result[y] = result[y].replace("address:", '')
        result[y] = result[y].replace('_', "")

    workbook = xlsxwriter.Workbook('customers.xlsx')
    worksheet = workbook.add_worksheet("Sheet_1")

    for row in range(0, len(result)):
        final = []
        working = result[row]
        working = working.split(",")
        for j in working:
            final.append(j)

        for itr in range(0, 8):
            cutoff = final[itr].find(":")
            worksheet.write(row+1, itr, (final[itr])[cutoff+1:len(final[itr])])
            worksheet.write(0, itr, (final[itr])[0:cutoff])
    workbook.close()


def view_accounts():
    viewUrl = "http://api.reimaginebanking.com/accounts?key=75ca43c1c9a8ea978abcc0c4bf5f56d7"
    stream = urllib.request.urlopen(viewUrl)
    result2 = []
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        result2.append(decoded)

    result2 = "".join(result2)
    result2 = result2.strip("[").strip("{").strip("]")
    result2 = result2.split("},{")

    for y in range(len(result2)):
        result2[y] = result2[y].replace('"', "")
        result2[y] = result2[y].replace('{', '')
        result2[y] = result2[y].replace('}', '')
        result2[y] = result2[y].replace('_', "")

    workbook2 = xlsxwriter.Workbook('accounts.xlsx')
    worksheet2 = workbook2.add_worksheet("Sheet_1")

    for row in range(0, len(result2)):
        final = []
        working = result2[row]
        working = working.split(",")
        for j in working:
            final.append(j)

        for itr in range(0, 6):
            cutoff = final[itr].find(":")
            worksheet2.write(row+1, itr, (final[itr])[cutoff+1:len(final[itr])])
            worksheet2.write(0, itr, (final[itr])[0:cutoff])
    workbook2.close()

# andrew  95ba331703fd9508cccf48b68cb48848
# rash    e8b756c83dac079e2e3abb5d42d97f76
# mic     75ca43c1c9a8ea978abcc0c4bf5f56d7

#


def get_account(userid):
    url = "http://api.reimaginebanking.com/accounts/" + userid + "?key=75ca43c1c9a8ea978abcc0c4bf5f56d7"
    stream = urllib.request.urlopen(url)
    result = []
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        result.append(decoded)
    result = "".join(result)
    print(result)


def get_customer(userid):
    url = "http://api.reimaginebanking.com/customers/" + userid + "?key=75ca43c1c9a8ea978abcc0c4bf5f56d7"
    stream = urllib.request.urlopen(url)
    result = []
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        result.append(decoded)
    result = "".join(result)
    print(result)

def transfer_money(payer_id, payee_id, amount):
    url = 'http://api.reimaginebanking.com/accounts/' + payer_id + '/transfers?key=75ca43c1c9a8ea978abcc0c4bf5f56d7'
    payload = {

            "medium": "balance",
            "payee_id": payee_id,
            "amount": amount,
            "transaction_date": "2017-02-12",
            "description": "string"
        }
    response = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}, )
    if response.status_code == 201:
        print('Transfer Completed')




