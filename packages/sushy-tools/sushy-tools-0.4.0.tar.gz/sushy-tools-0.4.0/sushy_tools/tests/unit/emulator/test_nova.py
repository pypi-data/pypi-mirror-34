# Copyright 2018 Red Hat, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from oslotest import base
from six.moves import mock

from sushy_tools.emulator.drivers.novadriver import OpenStackDriver
from sushy_tools.emulator import main


@mock.patch.object(os, 'environ', dict(OS_CLOUD='fake-cloud', **os.environ))
@mock.patch.object(main, 'driver', None)  # This enables Nova driver
@mock.patch('openstack.connect', autospec=True)
class EmulatorTestCase(base.BaseTestCase):

    def setUp(self):
        self.app = main.app.test_client()
        super(EmulatorTestCase, self).setUp()

    def test_root_resource(self, nova_mock):
        response = self.app.get('/redfish/v1/')
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json)

    def test_collection_resource(self, nova_mock):
        server0 = mock.Mock(id='host0')
        server1 = mock.Mock(id='host1')
        nova_mock.return_value.list_servers.return_value = [server0, server1]

        response = self.app.get('/redfish/v1/Systems')

        self.assertEqual(200, response.status_code)
        self.assertEqual({'@odata.id': '/redfish/v1/Systems/host0'},
                         response.json['Members'][0])
        self.assertEqual({'@odata.id': '/redfish/v1/Systems/host1'},
                         response.json['Members'][1])

    def test_system_resource_get(self, nova_mock):
        server = mock.Mock(id='zzzz-yyyy-xxxx',
                           power_state=1,
                           image={'id': 'xxxx-zzzz-yyyy'})
        nova_mock.return_value.get_server.return_value = server

        flavor = mock.Mock(ram=1024, vcpus=2)
        nova_mock.return_value.get_flavor.return_value = flavor

        image = mock.Mock(hw_firmware_type='bios')
        nova_mock.return_value.glance.find_image.return_value = image

        response = self.app.get('/redfish/v1/Systems/xxxx-yyyy-zzzz')

        self.assertEqual(200, response.status_code)
        self.assertEqual('xxxx-yyyy-zzzz', response.json['Id'])
        self.assertEqual('zzzz-yyyy-xxxx', response.json['UUID'])
        self.assertEqual('On', response.json['PowerState'])
        self.assertEqual(
            response.json['MemorySummary']['TotalSystemMemoryGiB'], 1)
        self.assertEqual(2, response.json['ProcessorSummary']['Count'])
        self.assertEqual(
            'Pxe', response.json['Boot']['BootSourceOverrideTarget'])
        self.assertEqual(
            'Legacy', response.json['Boot']['BootSourceOverrideMode'])

    def test_system_resource_patch(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=0)
        nova_conn_mock.get_server.return_value = server

        data = {'Boot': {'BootSourceOverrideTarget': 'Cd'}}
        response = self.app.patch('/redfish/v1/Systems/xxxx-yyyy-zzzz',
                                  json=data)
        self.assertEqual(204, response.status_code)

        nova_conn_mock.compute.set_server_metadata.assert_called_once_with(
            server.id, {'libvirt:pxe-first': ''})

    def test_system_reset_action_on(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=0)
        nova_conn_mock.get_server.return_value = server

        data = {'ResetType': 'On'}
        response = self.app.post(
            '/redfish/v1/Systems/xxxx-yyyy-zzzz/Actions/ComputerSystem.Reset',
            json=data)
        self.assertEqual(204, response.status_code)
        nova_conn_mock.compute.start_server.assert_called_once_with(server.id)

    def test_system_reset_action_forceon(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=0)
        nova_conn_mock.get_server.return_value = server

        data = {'ResetType': 'ForceOn'}
        response = self.app.post(
            '/redfish/v1/Systems/xxxx-yyyy-zzzz/Actions/ComputerSystem.Reset',
            json=data)
        self.assertEqual(204, response.status_code)
        nova_conn_mock.compute.start_server.assert_called_once_with(server.id)

    def test_system_reset_action_forceoff(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=1)
        nova_conn_mock.get_server.return_value = server

        data = {'ResetType': 'ForceOff'}
        response = self.app.post(
            '/redfish/v1/Systems/xxxx-yyyy-zzzz/Actions/ComputerSystem.Reset',
            json=data)
        self.assertEqual(204, response.status_code)
        nova_conn_mock.compute.stop_server.assert_called_once_with(server.id)

    def test_system_reset_action_shutdown(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=1)
        nova_conn_mock.get_server.return_value = server

        data = {'ResetType': 'GracefulShutdown'}
        response = self.app.post(
            '/redfish/v1/Systems/xxxx-yyyy-zzzz/Actions/ComputerSystem.Reset',
            json=data)
        self.assertEqual(204, response.status_code)
        nova_conn_mock.compute.stop_server.assert_called_once_with(server.id)

    def test_system_reset_action_restart(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=1)
        nova_conn_mock.get_server.return_value = server

        data = {'ResetType': 'GracefulRestart'}
        response = self.app.post(
            '/redfish/v1/Systems/xxxx-yyyy-zzzz/Actions/ComputerSystem.Reset',
            json=data)
        self.assertEqual(204, response.status_code)
        nova_conn_mock.compute.reboot_server.assert_called_once_with(
            server.id, reboot_type='SOFT')

    def test_system_reset_action_forcerestart(self, nova_mock):
        nova_conn_mock = nova_mock.return_value
        server = mock.Mock(power_state=1)
        nova_conn_mock.get_server.return_value = server

        data = {'ResetType': 'ForceRestart'}
        response = self.app.post(
            '/redfish/v1/Systems/xxxx-yyyy-zzzz/Actions/ComputerSystem.Reset',
            json=data)
        self.assertEqual(204, response.status_code)
        nova_conn_mock.compute.reboot_server.assert_called_once_with(
            server.id, reboot_type='HARD')

    def test_get_bios(self, nova_mock):
        test_driver = OpenStackDriver('fake-cloud')
        self.assertRaises(
            NotImplementedError,
            test_driver.get_bios, 'xxx-yyy-zzz')

    def test_set_bios(self, nova_mock):
        test_driver = OpenStackDriver('fake-cloud')
        self.assertRaises(
            NotImplementedError,
            test_driver.set_bios,
            'xxx-yyy-zzz',
            {'attribute 1': 'value 1'})

    def test_reset_bios(self, nova_mock):
        test_driver = OpenStackDriver('fake-cloud')
        self.assertRaises(
            NotImplementedError,
            test_driver.reset_bios,
            'xxx-yyy-zzz')
