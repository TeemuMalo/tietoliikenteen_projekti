import requests

data = requests.get('http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=82').text

with open('C:/Koulu (Tietotekniikka)/anturidataa/dataa.csv','w') as f:
    f.write(data)

