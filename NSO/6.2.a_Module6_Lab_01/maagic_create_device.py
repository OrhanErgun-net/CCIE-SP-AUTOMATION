import yaml
import ncs

with open('devices.yaml', 'r') as f:
    nodes = yaml.safe_load(f)

def main(nodes):
    for node in nodes:
        with ncs.maapi.Maapi() as m:
            with ncs.maapi.Session(m, 'admin', 'python'):
                with m.start_write_trans() as t:
                    root = ncs.maagic.get_root(t)
                    device_list = root.devices.device
                    if node.get('name') not in device_list:
                        device = device_list.create(node.get('name'))
                        device.address = node.get('address')
                        device.port = node.get('port')
                        device.description = node.get('desc')
                        device.authgroup = node.get('auth')
                        dev_type = device.device_type.cli
                        dev_type.ned_id = node.get('ned')
                        device.ssh_algorithms.public_key = ['ssh-rsa']
                        device.state.admin_state = 'unlocked'
                        print(f'Commiting the device {node.get("name")} configuration')
                        t.apply()
                        print(f'Device {node.get("name")} commited!')
                    else:
                        print(f'Device {node.get("name")} already exists!')
                root = ncs.maagic.get_root(m)
                device = root.devices.device[node.get('name')]
                print(f'Fetching SSH keys from device {node.get("name")}')
                output = device.ssh.fetch_host_keys()
                print(f'Result: {output.result}')
                output = device.sync_from()
                print(f'Result: {output.result}')
                if not output.result:
                    print(f'Error: {output.info}')

if __name__ == '__main__':
    main(nodes)


