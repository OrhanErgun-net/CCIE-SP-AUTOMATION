# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
from . import helpers

# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
class ServiceCallbacks(Service):

    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')

        vars = ncs.template.Variables()
        vars.add('VLAN_ID', service.vlan_id)
        vars.add('VLAN_NAME', f'{service.name}_VLAN')
        template = ncs.template.Template(service)
        template.apply('vlan-template', vars)

        for device in service.device:
            if device.ip_address:
                vars.add('DEVICE', device.name)
                vars.add('SVI_DESC', f'{service.name}_SVI')
                vars.add('ADDRESS', helpers.get_address(device.ip_address))
                vars.add('NETMASK', helpers.get_netmask(device.ip_address))
                template.apply('svi-template', vars)



# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        self.log.info('Main RUNNING')

        self.register_service('svi-servicepoint', ServiceCallbacks)

    def teardown(self):

        self.log.info('Main FINISHED')
