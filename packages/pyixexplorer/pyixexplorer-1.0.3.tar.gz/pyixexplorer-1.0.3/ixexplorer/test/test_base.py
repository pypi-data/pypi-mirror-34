"""
Base class for all IxExplorer package tests.

@author yoram@ignissoft.com
"""

from os import path

from trafficgenerator.test.test_tgn import TgnTest

from ixexplorer.ixe_app import init_ixe


class IxeTestBase(TgnTest):

    TgnTest.config_file = path.join(path.dirname(__file__), 'IxExplorer.ini')

    def setUp(self):
        super(IxeTestBase, self).setUp()
        self.ixia = init_ixe(self.logger, host=self.config.get('IXE', 'server'),
                             port=self.config.getint('IXE', 'tcp_port'), rsa_id=self.config.get('IXE', 'rsa_id'))
        self.ixia.connect(self.config.get('IXE', 'user'))
        self.ixia.add(self.config.get('IXE', 'chassis'))

        self.port1 = self.config.get('IXE', 'port1')
        self.port2 = self.config.get('IXE', 'port2')

        self.ports = {}

    def tearDown(self):
        for port in self.ports.values():
            port.release()
        self.ixia.disconnect()
        super(IxeTestBase, self).tearDown()

    def testHelloWorld(self):
        pass

    def _reserve_ports(self, *ports):
        self.ports = self.ixia.session.reserve_ports(ports, force=True)

    def _load_configs(self, *cfgs):
        for port, cfg in zip(self.ports.values(), cfgs):
            port.load_config(cfg)

    def _reserver_and_load(self, *cfgs):
        self._reserve_ports(self.port1, self.port2)
        self._load_configs(*cfgs)
