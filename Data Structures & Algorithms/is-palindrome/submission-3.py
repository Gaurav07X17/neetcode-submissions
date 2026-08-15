class Solution:

  def isPalindrome(self, s: str) -> bool:
    Alpnum = set(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    )
    l, r = 0, len(s) - 1

    while l < r:
      # Skip non-alphanumeric characters from left
      while l < r and s[l] not in Alpnum:
        l += 1

      # Skip non-alphanumeric characters from right
      while l < r and s[r] not in Alpnum:
        r -= 1

      # Compare characters in lowercase
      if s[l].lower() != s[r].lower():
        return False

      l += 1
      r -= 1

    return True