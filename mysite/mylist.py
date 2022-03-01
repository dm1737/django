from asyncio.windows_events import INFINITE


Arr = [-200, 100.00, 59.0, 36, 1000, 55, 25, 49, 90]

def second_larget(arr):
    max_val = float(-INFINITE)
    second_largest = float(-INFINITE) 
    for val in arr:
        if val > max_val:
            second_largest = max_val
            max_val = val
        elif val > second_largest:
            second_largest = val
    return second_largest

print(second_larget(Arr))
