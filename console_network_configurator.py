import winreg as reg
import wmi


def set_network(ip, mask, gateway, dns_servers):
    try:
        # Obtain network adapter configurations
        nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

        # First network adapter
        nic = nic_configs[0]

        # Set IP address, subnet mask, default gateway, and DNS servers
        nic.EnableStatic(IPAddress=[ip], SubnetMask=[mask])
        nic.SetGateways(DefaultIPGateway=[gateway])
        nic.SetDNSServerSearchOrder(dns_servers)
        print("Network settings successfully configured.")
    except Exception as e:
        print("An error occurred while configuring network settings: ", e)


# Function to set proxy server
def set_proxy(proxy_server):
    try:
        # Open registry key for Internet Settings
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, reg.KEY_ALL_ACCESS)

        # Set proxy server parameters
        reg.SetValueEx(reg_key, 'ProxyServer', 0, reg.REG_SZ, proxy_server)
        reg.SetValueEx(reg_key, 'ProxyEnable', 0, reg.REG_DWORD, 1)

        # Close the registry key
        reg.CloseKey(reg_key)
        print("Proxy successfully configured:", proxy_server)
    except Exception as e:
        print("Error configuring proxy:", e)


# Set IP address, subnet mask, gateway, and DNS servers
ip = u'192.168.2.12'
subnetmask = u'255.255.255.0'
gateway = u'192.168.2.1'
dns_servers = ['95.167.167.95', '95.167.167.96']
set_network(ip, subnetmask, gateway, dns_servers)

# Set proxy server
proxy_server = '10.0.23.52:3128'
set_proxy(proxy_server)
