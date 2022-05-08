from nso import NsoRestconf


nso = NsoRestconf()


def create_svi_service(path, payload):
    resp = nso.post(path, payload)
    print(resp.status_code)

def get_svi_service(path):
    resp = nso.get(path)
    print(resp.text)

def replace_svi_service(path, payload):
    resp = nso.put(path, payload)
    print(resp.status_code)

def merge_svi_service(path, payload):
    resp = nso.patch(path, payload)
    print(resp.status_code)

def delete_svi_service(path):
    resp = nso.delete(path)
    print(resp.status_code)


if __name__ == '__main__':
    print('POST')
    create_svi_service('tailf-ncs:services', './payloads/create_svi_service.json')
    get_svi_service('tailf-ncs:services/svi:vlan')
    print('!'*50)
    print('PUT')
    replace_svi_service('tailf-ncs:services/svi:vlan=IPTV', './payloads/replace_svi_service.json')
    get_svi_service('tailf-ncs:services/svi:vlan')
    print('!'*50)
    print('PATCH')
    merge_svi_service('tailf-ncs:services/svi:vlan=IPTV', './payloads/merge_svi_service.json')
    get_svi_service('tailf-ncs:services/svi:vlan')
    print('!'*50)
    print('DELETE')
    delete_svi_service('tailf-ncs:services/svi:vlan=IPTV')
    get_svi_service('tailf-ncs:services/svi:vlan')
    print('!'*50)