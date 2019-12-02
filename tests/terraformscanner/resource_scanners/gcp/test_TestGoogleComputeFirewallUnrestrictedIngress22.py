import unittest

from bridgecrew.terraformscanner.models.enums import ScanResult
from bridgecrew.terraformscanner.resource_scanners.gcp.GoogleComputeFirewallUnrestrictedIngress22 import scanner, PORT


class TestGoogleComputeFirewallUnrestrictedIngress22(unittest.TestCase):

    def test_failure(self):
        resource_conf = {'name': ['${var.name}-${var.region}-mesos-ssh'],
                         'network': ['${google_compute_network.mesos-global-net.name}'],
                         'allow': [{'protocol': ['tcp'], 'ports': [[PORT]]}], 'target_tags': [['ssh']],
                         'source_ranges': [['0.0.0.0/0']]}

        scan_result = scanner.scan_resource_conf(conf=resource_conf)
        self.assertEqual(ScanResult.FAILURE, scan_result)

    def test_success(self):
        resource_conf = {'name': ['${var.name}-${var.region}-mesos-ssh'],
                         'network': ['${google_compute_network.mesos-global-net.name}'],
                         'allow': [{'protocol': ['tcp'], 'ports': [[
                             PORT]]}], 'target_tags': [['ssh']], 'source_ranges': [['172.1.2.3/32']]}
        scan_result = scanner.scan_resource_conf(conf=resource_conf)
        self.assertEqual(ScanResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()