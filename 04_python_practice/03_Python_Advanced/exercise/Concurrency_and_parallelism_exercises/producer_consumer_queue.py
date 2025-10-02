import threading
import queue


def pipeline(nums):
    q = queue.Queue()
    results = []

    def worker():
        while True:
            item = q.get()
            if item is None:  # Sentinel to stop
                q.task_done()  # important!
                break
            results.append(item * item)
            q.task_done()

    thread = threading.Thread(target=worker)
    thread.start()

    for num in nums:
        q.put(num)
    q.put(None)  # Sentinel

    q.join()     # Wait until all tasks done
    thread.join()

    return results


res = pipeline([1, 2, 3, 4])
assert sorted(res) == [1, 4, 9, 16]
print("Results:", res)
