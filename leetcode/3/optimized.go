package main

func lengthOfLongestSubstring(s string) int {
	currentChars := make(map[byte]bool)

	start := 0
	end := 0
	longest := 0
	for start < len(s) && end < len(s) {
		startChar := s[start]
		endChar := s[end]
		charPresent, _ := currentChars[endChar]

		if !charPresent {
			currentChars[endChar] = true
			end++
		} else {
			currentChars[startChar] = false
			start++
		}

		currentLen := end - start
		if currentLen > longest {
			longest = currentLen
		}
	}

	return longest
}
