import sys
import csv
import conf


filename = 'maps.csv'               #name of the csv-file, where the maps are stored
vName = 'RACE'        #Servername
vPort = '8308'                      #Serverport
vRcon = 'admin'                #rcon-password
vMax = '32'                         #max clients
vMaxTries = '3'                     #max tries rcon login
vMap = 'run_colorless'              #default map at startup
vPassword = ''                      #server-password
vGametype = 'race'                  #gametype


# Do NOT change these values!!!
svName = ['sv_name', vName, 'nameless server']
svPort = ['sv_port', vPort, '8303']
svRcon = ['sv_rcon_password', vRcon, 'password']
svMax = ['sv_max_clients', vMax, '16']
svMaxTries = ['sv_rcon_max_tries', vMaxTries, '3']
svMap = ['sv_map', vMap, 'dm1']
password = ['password', vPassword, '']
svGametype = ['sv_gametype', vGametype, 'race']

addVote = 'add_vote'
changeMap = 'change_map'

delim = '-------'


maps = []
with open('maps.csv', 'rt') as csvfile:
    line = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in line:
        maps.append(row)

maps = sorted(maps, key=lambda maps: (maps[1], maps[0]))

# for line in maps:
#     print(line)


config = []


config.append(conf.check(svName))
config.append(conf.check(svPort))
config.append(conf.check(svGametype))
config.append(conf.check(svMap))
config.append(conf.check(svMax))
config.append(conf.check(svMaxTries))
config.append(conf.check(svRcon))
config.append(conf.check(password))

cat = ''
for m in maps:
    if m[1] == '':
        m[1] = 'No Category'

    if cat != m[1]:
        config.append([addVote, ''.join([delim, m[1], delim])])
    config.append([addVote, m[0], changeMap, m[0]])
    cat = m[1]

# for i in config:
#     print(i)

with open('config.cfg', 'wt') as configFile:
    filewriter = csv.writer(configFile, delimiter=' ', lineterminator='\n')
    for i in config:
        filewriter.writerow(i)
