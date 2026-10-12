import unittest
from fencing_demo import ToyBroker


class FencingDemoTests(unittest.TestCase):
    def test_stale_worker_cannot_publish(self):
        broker = ToyBroker()
        broker.approve('ISSUE')
        a = broker.claim('ISSUE', 'a')
        b = broker.claim('ISSUE', 'b')
        with self.assertRaisesRegex(PermissionError, 'Stale epoch'):
            broker.publish(a, 'a-publish')
        self.assertTrue(broker.publish(b, 'b-publish'))

    def test_revocation(self):
        broker = ToyBroker()
        broker.approve('ISSUE')
        claim = broker.claim('ISSUE', 'a')
        broker.revoke('ISSUE')
        with self.assertRaisesRegex(PermissionError, 'Approval revoked'):
            broker.publish(claim, 'write')

    def test_idempotency(self):
        broker = ToyBroker()
        broker.approve('ISSUE')
        claim = broker.claim('ISSUE', 'a')
        self.assertTrue(broker.publish(claim, 'write'))
        self.assertFalse(broker.publish(claim, 'write'))


if __name__ == '__main__':
    unittest.main()
