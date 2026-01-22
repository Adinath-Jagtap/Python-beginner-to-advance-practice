def longest_unique_substring(s: str) -> str:
    """
    Returns the longest substring without repeating characters.
    Also returns the substring itself (not only length).
    Uses sliding window with a last-seen index map.
    Time: O(n)
    """
    last = {}          # char -> last index seen
    start = 0          # left index of window
    best_len = 0
    best_sub = ""
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            # move start just after previous occurrence
            start = last[ch] + 1
        last[ch] = i
        cur_len = i - start + 1
        if cur_len > best_len:
            best_len = cur_len
            best_sub = s[start:i+1]
    return best_sub

# Sample usage
sample = "abcabcbb"
print("Longest unique substring:", longest_unique_substring(sample))  # -> "abc"
sample2 = "pwwkew"
print("Longest unique substring:", longest_unique_substring(sample2)) # -> "wke"
