"""Educational in-memory demonstration. NOT a production lease or GitHub fence."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Claim:
    issue: str
    run_id: str
    epoch: int


class ToyBroker:
    """A single-process stand-in for a trusted mutation broker."""
    def __init__(self):
        self.epoch_by_issue = {}
        self.owner_by_issue = {}
        self.approved = set()
        self.published = set()

    def approve(self, issue):
        self.approved.add(issue)

    def revoke(self, issue):
        self.approved.discard(issue)

    def claim(self, issue, run_id):
        if issue not in self.approved:
            raise PermissionError('Issue not approved')
        epoch = self.epoch_by_issue.get(issue, 0) + 1
        self.epoch_by_issue[issue] = epoch
        self.owner_by_issue[issue] = run_id
        return Claim(issue, run_id, epoch)

    def publish(self, claim, idempotency_key):
        if claim.issue not in self.approved:
            raise PermissionError('Approval revoked')
        if self.epoch_by_issue.get(claim.issue) != claim.epoch:
            raise PermissionError('Stale epoch')
        if self.owner_by_issue.get(claim.issue) != claim.run_id:
            raise PermissionError('Wrong run owner')
        if idempotency_key in self.published:
            return False  # idempotent duplicate; no additional effect
        self.published.add(idempotency_key)
        return True


def demo():
    b = ToyBroker()
    b.approve('GTM-DEMO')
    a = b.claim('GTM-DEMO', 'run-A')  # epoch 1
    worker_a_pauses = True
    assert worker_a_pauses
    newer = b.claim('GTM-DEMO', 'run-B')  # epoch 2
    assert newer.epoch > a.epoch
    assert b.publish(newer, 'op-B-1') is True
    assert b.publish(newer, 'op-B-1') is False
    try:
        b.publish(a, 'op-A-1')
        raise AssertionError('Stale A unexpectedly published')
    except PermissionError as ex:
        assert str(ex) == 'Stale epoch'
    b.revoke('GTM-DEMO')
    try:
        b.publish(newer, 'op-B-2')
        raise AssertionError('Revoked B unexpectedly published')
    except PermissionError as ex:
        assert str(ex) == 'Approval revoked'
    print('PASS: stale run and revoked issue denied; repeated operation idempotent')


if __name__ == '__main__':
    demo()
