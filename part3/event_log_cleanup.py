def maximum_removals(source, pattern, target_indices):
    """
    Returns:
        maximum number of removals
        original indices that were removed
    """
    target_indices = set(target_indices)

    n = len(source)
    m = len(pattern)

    dp = [[float("-inf")] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 0

    for i in range(1, n + 1):
        source_index = i - 1
        source_character = source[source_index]

        for j in range(m + 1):
            # keep this character without matching
            dp[i][j] = dp[i - 1][j]

            # delete this character to match the pattern
            if source_index in target_indices:
                if dp[i - 1][j] != float("-inf"):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)

            # keep this character to match the pattern
            if(j > 0 and source_character == pattern[j - 1] and dp[i - 1][j - 1] != float("-inf")):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

    removed_indices = []

    i = n
    j = m

    while i > 0:
        source_index = i - 1

        # check whether this character was deleted
        if(source_index in target_indices and dp[i][j] == dp[i - 1][j] + 1):
            removed_indices.append(source_index)
            i -= 1

        # check whether this character matched the pattern
        elif(j > 0 and source[source_index] == pattern[j - 1] and dp[i][j] == dp[i - 1][j - 1]):
            i -= 1
            j -= 1

        # otherwise, the character was kept without matching
        else:
            i -= 1

    removed_indices.reverse()
    
    return dp[n][m], removed_indices

if __name__ == "__main__":
    source = "abbaa"
    pattern = "aba"
    target_indices = [0,1,2]

    removal_count, removed_indices = maximum_removals(source, pattern, target_indices)

    print("Max removals:", removal_count)
    print("Removed indices:", removed_indices)