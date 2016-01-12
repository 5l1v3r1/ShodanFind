import json
import os
import urllib2
#from pprint import pprint

RED = '\x1b[91m'
BLUE = '\033[94m'
GREEN = '\033[32m'
OTRO = '\033[36m'
BOLD = '\033[1m'
ENDC = '\033[0m'

API_KEY = "INGRESA TU API"

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])
cls()

logo = RED + BOLD + '''
     ,-,--.  ,--.-,,-,--,   _,.---._                  ,---.      .-._         
   ,-.'-  _\/==/  /|=|  | ,-.' , -  `.   _,..---._  .--.'  \    /==/ \  .-._  
  /==/_ ,_.'|==|_ ||=|, |/==/_,  ,  - \/==/,   -  \ \==\-/\ \   |==|, \/ /, / 
  \==\  \   |==| ,|/=| _|==|   .=.     |==|   _   _\/==/-|_\ |  |==|-  \|  |  
   \==\ -\  |==|- `-' _ |==|_ : ;=:  - |==|  .=.   |\==\,   - \ |==| ,  | -|  
   _\==\ ,\ |==|  _     |==| , '='     |==|,|   | -|/==/ -   ,| |==| -   _ |  
  /==/\/ _ ||==|   .-. ,\\==\ -    ,_ /|==|  '='   /==/-  /\ - \|==|  /\ , |  
  \==\ - , //==/, //=/  | '.='. -   .' |==|-,   _`/\==\ _.\=\.-'/==/, | |- |  
   `--`---' `--`-' `-`--`   `--`--''   `-.`.____.'  `--`        `--`./  `--`
                    _,---.   .=-.-..-._                     
                 .-`.' ,  \ /==/_ /==/ \  .-._  _,..---._   
                /==/_  _.-'|==|, ||==|, \/ /, /==/,   -  \  
               /==/-  '..-.|==|  ||==|-  \|  ||==|   _   _\ 
               |==|_ ,    /|==|- ||==| ,  | -||==|  .=.   | 
               |==|   .--' |==| ,||==| -   _ ||==|,|   | -| 
               |==|-  |    |==|- ||==|  /\ , ||==|  '='   / 
               /==/   \    /==/. //==/, | |- ||==|-,   _`/  
               `--`---'    `--`-` `--`./  `--``-.`.____.' By @s1kr10s
''' + ENDC
print logo

menu = BLUE + '''
  [ E ] Buscar Exploits
  [ Q ] Buscar con Querys
  [ D ] Dns Reversa
  [ R ] Dns Resolver
  [ M ] Mi IP
  [ H ] Ejemplos de Busqueda
''' + ENDC
print menu
opcion = raw_input(BLUE + "  OPCION: " + ENDC)

if opcion == 'e':
    cls()
    print logo
    print BOLD + "\n  BUSCARDOR DE EXPLOIT SHODAN\n" + ENDC
    query = raw_input("  BUSCAR EXPLOIT PARA: ")

    getdata = urllib2.Request("https://exploits.shodan.io/api/search?query=" + query + "&key=" + API_KEY + "")
    contents = urllib2.urlopen(getdata)
    code = contents.getcode()
    html = contents.read()
    contents.close()

    alert_fecha = open('exploit.json', 'a')
    alert_fecha.write(html)
    alert_fecha.close()

    with open('exploit.json') as data_file:
        data = json.load(data_file)

    for matches in data["matches"]:
        source = matches["source"]
        cve = str(matches["source"]) + '-' + str(matches["_id"])
        description = matches["description"]

        if source <> 'Metasploit':
            print BOLD + cve + ENDC
            print BLUE + description + ENDC
            print GREEN + "Busqueda de: " + BOLD + str(query) + ENDC
            print "\n"
        else:
            print RED + cve + ENDC
            print GREEN + description + ENDC
            print "\n"
    os.remove('exploit.json')
elif opcion == 'q':
    cls()
    print logo
    print BOLD + "\n  BUSCARDOR POR QUERY SHODAN\n" + ENDC
    query = raw_input("  BUSCAR: ")
    facetas = raw_input("  FACETA: ")
    
    getdata = urllib2.Request("https://api.shodan.io/shodan/host/search?key=" + API_KEY + "&query=" + query + "&facets=" + facetas + "")
    contents = urllib2.urlopen(getdata)
    code = contents.getcode()
    html = contents.read()
    contents.close()
    
    alert_fecha = open('search.json', 'a')
    alert_fecha.write(html)
    alert_fecha.close()
    
    with open('search.json') as data_file:
	data = json.load(data_file)

    for matches in data["matches"]:
        port = matches["port"]
        domains = matches["domains"]
        ip_str = matches["ip_str"]
        hostnames = matches["hostnames"]
        org = matches["org"]

        if len(domains) == 0:
            domains = RED + "None" + ENDC
        if len(hostnames) == 0:
            hostnames = RED + "None" + ENDC
        
        print BLUE + "  ORGANIZACION : " + ENDC + OTRO + BOLD + str(org) + ENDC
        print BLUE + "  IP           : " + ENDC + GREEN + str(ip_str) + ENDC
        print BLUE + "  DOMINIO      : " + ENDC + GREEN + str(domains) + ENDC
        print BLUE + "  HOSTNAME     : " + ENDC + GREEN + str(hostnames) + ENDC
        print BLUE + "  PUERTO       : " + ENDC + GREEN + str(port) + ENDC
        print "\n"
    os.remove('search.json')
elif opcion == 'd':
    cls()
    print logo
    print BOLD + "\n  DNS REVERSA SHODAN\n" + ENDC
    query = raw_input("  CUAL ES LA IP: ")
    
    getdata = urllib2.Request("https://api.shodan.io/dns/reverse?ips=" + query + "&key=" + API_KEY + "")
    contents = urllib2.urlopen(getdata)
    code = contents.getcode()
    html = contents.read()
    contents.close()
    
    alert_fecha = open('reverse.json', 'a')
    alert_fecha.write(html)
    alert_fecha.close()
    
    with open('reverse.json') as data_file:
        data = json.load(data_file)
        
    ps1 = str(data[query]).split("[u'")
    dominio = str(ps1[1]).split("']")
    
    print BLUE + "\n  IP      : " + ENDC + GREEN + query + ENDC
    print BLUE + "  DOMINIO : " + ENDC + GREEN + dominio[0] + "\n" + ENDC
    os.remove('reverse.json')
elif opcion == 'r':
    cls()
    print logo
    print BOLD + "\n  DNS RESOLVER SHODAN\n" + ENDC
    query = raw_input("  CUAL ES EL DOMINIO: ")
    
    getdata = urllib2.Request("https://api.shodan.io/dns/resolve?hostnames=" + query + "&key=" + API_KEY + "")
    contents = urllib2.urlopen(getdata)
    code = contents.getcode()
    html = contents.read()
    contents.close()
    
    alert_fecha = open('resolver.json', 'a')
    alert_fecha.write(html)
    alert_fecha.close()
    
    with open('resolver.json') as data_file:
        data = json.load(data_file)
        
    ps1 = str(data).split("': u'")
    ip = str(ps1[1]).split("'}")
    
    print BLUE + "\n  DOMINIO : " + ENDC + GREEN + query + ENDC
    print BLUE + "  IP      : " + ENDC + GREEN + ip[0] + "\n" + ENDC
    os.remove('resolver.json')
elif opcion == 'm':
    cls()
    print logo
    print BOLD + "\n  DNS RESOLVER SHODAN\n" + ENDC
    
    getdata = urllib2.Request("https://api.shodan.io/tools/myip?key=" + API_KEY + "")
    contents = urllib2.urlopen(getdata)
    code = contents.getcode()
    html = contents.read()
    contents.close()
    
    alert_fecha = open('miip.json', 'a')
    alert_fecha.write(html)
    alert_fecha.close()
    
    with open('miip.json') as data_file:
        data = json.load(data_file)
    
    print BLUE + "\n  MI IP : " + ENDC + GREEN + data + "\n" + ENDC
    os.remove('miip.json')
elif opcion == 'h':
    cls()
    print logo
    print BOLD + "\n  EJEMPLOS DE QUERY" + ENDC
    print GREEN
    print "  1 -  nasa port:23"
    print "  2 -  sftp domain:nasa"
    print "  3 -  netcam country:CL city:santiago"
    print "  4 -  port:21 anonymous country:CL"
    print "  5 -  Server: SQ-WEBCAM"
    print '  6 -  "default password"'
    print "  7 -  hostname:nasa.gov"
    print "  8 -  admin+1234"
    print "  Etc...\n"
    print "  (MAS INFO: https://www.shodan.io/explore)"
    print ENDC
