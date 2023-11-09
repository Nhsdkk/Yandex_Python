package utils

func Sum(arr []int) int {
	res := 0
	for _, item := range arr {
		res += item
	}
	return res
}
