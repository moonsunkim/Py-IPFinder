# -*- coding: UTF-8 -*-
#pyinstaller --onefile ip_changer.py
import wmi, sys, os

def search_vlan(zone):
    search_vlan_zone_4 = {'11ip': u'10.14.11.254', '11gw': u'10.14.11.1',
                          '12ip': u'10.14.12.254', '12gw': u'10.14.12.1',
                          '13ip': u'10.14.13.254', '13gw': u'10.14.13.1',
                          '14ip': u'10.14.14.254', '14gw': u'10.14.14.1',
                          '15ip': u'10.14.15.254', '15gw': u'10.14.15.1',
                          '16ip': u'10.14.16.254', '16gw': u'10.14.16.1',
                          '17ip': u'10.14.17.254', '17gw': u'10.14.17.1',
                          '18ip': u'10.14.18.254', '18gw': u'10.14.18.1',
                          '19ip': u'10.14.19.254', '19gw': u'10.14.19.1',
                          }
    search_vlan_zone_5 = {'11ip': u'10.15.11.254', '11gw': u'10.15.11.1',
                          '12ip': u'10.15.12.254', '12gw': u'10.15.12.1',
                          '13ip': u'10.15.13.254', '13gw': u'10.15.13.1',
                          '14ip': u'10.15.14.254', '14gw': u'10.15.14.1',
                          '15ip': u'10.15.15.254', '15gw': u'10.15.15.1',
                          '16ip': u'10.15.16.254', '16gw': u'10.15.16.1',
                          '17ip': u'10.15.17.254', '17gw': u'10.15.17.1',
                          '18ip': u'10.15.18.254', '18gw': u'10.15.18.1',
                          '19ip': u'10.15.19.254', '19gw': u'10.15.19.1',
                          }
    search_vlan_subnet_mask = u'255.255.255.0'
    search_vlan_server_subnet_mask = u'255.255.0.0'

    if zone == '4':
        for i in range(11, 20):
            setting_ip(search_vlan_zone_4[str(i) + 'ip'], search_vlan_zone_4[str(i) + 'gw'], search_vlan_subnet_mask)
    elif zone == '5':
        for i in range(11, 20):
            setting_ip(search_vlan_zone_5[str(i) + 'ip'], search_vlan_zone_5[str(i) + 'gw'], search_vlan_subnet_mask)
    elif zone == '10':
        setting_ip('10.10.254.254', '10.10.1.1', search_vlan_server_subnet_mask)
    elif zone == '100':
        setting_ip('10.100.254.254', '10.100.0.1', search_vlan_server_subnet_mask)
    elif zone == '200':
        setting_ip('10.200.254.254', '10.200.0.1', search_vlan_server_subnet_mask)
    elif zone == '222':
        setting_ip('10.222.254.254', '10.222.0.1', search_vlan_server_subnet_mask)
    else:
        print("[!] Not Support Floor.")

def setting_ip(ip, gateway, subnetmask):
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    nic = nic_configs[0]
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
    if ping(gateway) == True:
        print('[!] Network is %s' % gateway)
    else:
        pass

def ping(gateway):
    return not os.system('ping %s -n 2 > NUL' % (gateway,))

def vlan_help():
    print(" Argvs: 4, 5, 10, 100, 200, 222, test")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) is 1:
        vlan_help()

    else :
        if sys.argv[1] == '4':
            search_vlan(sys.argv[1])
        elif sys.argv[1] == '5':
            search_vlan(sys.argv[1])
        elif sys.argv[1] == '10':
            search_vlan(sys.argv[1])
        elif sys.argv[1] == '100':
            search_vlan(sys.argv[1])
        elif sys.argv[1] == '200':
            search_vlan(sys.argv[1])
        elif sys.argv[1] == '222':
            search_vlan(sys.argv[1])
        elif sys.argv[1] == 'test':
            if ping('10.10.1.1') == True:
                print("[!]Ping OK!")
            else:
                pass
        else:
            vlan_help()
