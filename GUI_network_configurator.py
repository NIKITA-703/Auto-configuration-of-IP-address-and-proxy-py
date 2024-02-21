import tkinter as tk
from tkinter import messagebox
import wmi
import winreg as reg


# Function to set network parameters
def set_network(ip, mask, gateway, dns_servers):
    try:
        nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
        nic = nic_configs[0]
        nic.EnableStatic(IPAddress=[ip], SubnetMask=[mask])
        nic.SetGateways(DefaultIPGateway=[gateway])
        nic.SetDNSServerSearchOrder(dns_servers)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while configuring the IP address: " + str(e))


# Function to set proxy
def set_proxy(proxy_server):
    try:
        reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, reg.KEY_ALL_ACCESS)
        reg.SetValueEx(reg_key, 'ProxyServer', 0, reg.REG_SZ, proxy_server)
        reg.SetValueEx(reg_key, 'ProxyEnable', 0, reg.REG_DWORD, 1)
        reg.CloseKey(reg_key)
        messagebox.showinfo("Success", "Proxy successfully configured: " + proxy_server)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while configuring the proxy: " + str(e))


# Function to handle the button click for configuring the proxy
def configure_proxy():
    last_octet = last_octet_entry.get()
    if not last_octet.isdigit():
        messagebox.showerror("Error", "The last octet should be a number.")
        return
    last_octet = int(last_octet)
    if last_octet < 1 or last_octet > 255:
        messagebox.showerror("Error", "The last octet should be in the range from 1 to 255.")
        return

    ip = '10.23.22.' + str(last_octet)
    subnetmask = '255.255.255.0'
    gateway = '10.23.22.1'
    dns_servers = ['95.167.167.95', '95.167.167.96']
    set_network(ip, subnetmask, gateway, dns_servers)

    proxy_server = '10.0.23.52:3128'
    set_proxy(proxy_server)


# Creating the graphical interface
root = tk.Tk()
root.title("Proxy Configuration")

last_octet_label = tk.Label(root, text="Last Octet IP:")
last_octet_label.pack()
last_octet_entry = tk.Entry(root)
last_octet_entry.pack()

configure_button = tk.Button(root, text="Configure Proxy", command=configure_proxy)
configure_button.pack()

root.resizable(0, 0)
root.geometry("300x100")
root.mainloop()
