# Implement an Ordered Array of Records structure using recursive
# binary search

# Define the identity function
def identity(x):
    return x

# OrderedRecordArray class for managing ordered records
class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0                # No items in array initially
        self.__key = key                 # Key function gets record key

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if n >= 0 and n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index " + str(n) + " is out of range")

    def find(self, key, lo=0, hi=None):
        if hi is None:
            hi = self.__nItems - 1
        if lo > hi:
            return lo
        mid = (lo + hi) // 2
        if self.__key(self.__a[mid]) == key:
            return mid

        if self.__key(self.__a[mid]) < key:
            return self.find(key, mid + 1, hi)
        else:
            return self.find(key, lo, mid - 1)

    def search(self, key):
        idx = self.find(key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]

    def insert(self, item):
        j = self.find(self.__key(item))
        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k-1]
        self.__a[j] = item
        self.__nItems += 1

    def delete(self, item):
        j = self.find(self.__key(item))
        if j < self.__nItems and self.__a[j] == item:
            self.__nItems -= 1
            for k in range(j, self.__nItems):
                self.__a[k] = self.__a[k+1]
            return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans
