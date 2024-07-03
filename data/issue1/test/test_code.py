def create_list(values):
    head = temp = ListNode()
    for val in values:
        temp.next = ListNode(val)
        temp = temp.next
    return head.next


def parse_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def run_test(lists):

    solution = Solution()

    lists = [create_list(l) for l in lists]

    merged_list = solution.mergeKLists(lists)
    res = parse_list(merged_list)
    return res
