REFUND_THRESHOLD = 500


def can_refund(order):
    if order.status != "delivered":
        return False
    return order.amount >= REFUND_THRESHOLD
