from tendrl.commons import objects


class GlobalNetwork(objects.BaseObject):

    def __init__(self, interface=None, interface_id=None,
                 ipv4=None, ipv6=None, netmask=None, subnet=None,
                 status=None, sysfs_id=None, device_link=None,
                 interface_type=None, model=None, driver_modules=None,
                 driver=None, drive=None, hw_address=None, link_detected=None,
                 *args, **kwargs):
        super(GlobalNetwork, self).__init__(*args, **kwargs)
        self.interface = interface
        self.interface_id = interface_id
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.netmask = netmask
        self.subnet = subnet
        self.status = status
        self.sysfs_id = sysfs_id
        self.device_link = device_link
        self.drive = drive
        self.interface_type = interface_type
        self.model = model
        self.driver_modules = driver_modules
        self.driver = driver
        self.hw_address = hw_address
        self.link_detected = link_detected
        # networks/<subnet>/<node_id>/<interface_id>
        self.value = 'networks/{0}/{1}/{2}'

    def render(self):
        self.value = self.value.format(self.subnet.replace("/", "_"),
                                       NS.node_context.node_id,
                                       self.interface_id
                                       )
        return super(GlobalNetwork, self).render()
