package main

func lengthOfLongestSubstring(s string) int {
	longest := 0
	for i := range s {
		chars := make(map[int32]bool)

		currentLongest := 0
		for _, char := range s[i:] {
			exists, _ := chars[char]

			if exists {
				break
			} else {
				chars[char] = true
			}

			currentLongest++
		}

		if currentLongest > longest {
			longest = currentLongest
		}
	}

	return longest
}
