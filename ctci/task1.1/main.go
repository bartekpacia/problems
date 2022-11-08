package main

func main() {
}

// Implement an algorithm to determine if a string has all unique characters.

func unique1(s string) bool {
	chars := make(map[byte]struct{})

	for i := 0; i < len(s); i++ {
		_, ok := chars[s[i]]
		if ok {
			return false
		}

		chars[s[i]] = struct{}{}

	}

	return true
}

// What if you cannot use additional data structures?

func unique2(s string) bool {
	for i := 0; i < len(s); i++ {
		for j := 0; j < len(s); j++ {
			if i == j {
				continue
			}

			if s[i] == s[j] {
				return false
			}
		}
	}

	return true
}
