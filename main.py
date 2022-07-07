import sys

import mysql.connector
import requests

if __name__ == '__main__':

    session = requests.session()
    url = "https://bilder.campuswoche.de/webapi/login"
    data = {"uname": sys.argv[5], "upass": sys.argv[6]}
    print(session.post(url, data).text)

    mydb = mysql.connector.connect(
        host=sys.argv[1],
        user=sys.argv[2],
        password=sys.argv[3],
        database=sys.argv[4]
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT vorname, nachname, geb FROM wp_cw_user")
    rows = cursor.fetchall()

    url = "https://bilder.campuswoche.de/webapi/useradd"
    for row in rows:
        username = str(row[0][:3]).lower() + str(row[1])[:3].lower()
        password = username + row[2].strftime("%Y")
        data = {'vorname': row[0], 'nachname': row[1], 'uname': username, 'upass': password, 'upassw': password}
        print(data)
        print(session.post(url, data).text)
