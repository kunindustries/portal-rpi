import configparser

configLocation = "/home/pi/python/portal-rpi/config.ini"

config = configparser.ConfigParser()
config.read(configLocation)

my_name = config['DEFAULT']['MyName']
my_purpose = config['DEFAULT']['MyPurpose']
api_token = config['KUNINDUSTRIES_API']['Token']
api_status_interval = config['KUNINDUSTRIES_API']['StatusInterval']
api_status_interval = config['KUNINDUSTRIES_API']['AutoUpdateAddressAndPort']
api_device_id = config['KUNINDUSTRIES_API']['DeviceID']

def updateConfig(section, key, value):
	config[section][key] = value

	with open(configLocation, 'w') as configfile:
	    config.write(configfile)