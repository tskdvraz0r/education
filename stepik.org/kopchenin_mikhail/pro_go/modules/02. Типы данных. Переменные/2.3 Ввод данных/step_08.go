// Date: 23.03.2024
// Url: https://stepik.org/lesson/917013/step/8?unit=922792

package main
import (
	"os"
	"bufio"
	"fmt"
)

func main() {
	var separator string
	var word1 string
	var word2 string
	var word3 string

	scanner := bufio.NewScanner(os.Stdin)
	
	_ = scanner.Scan()
	separator = scanner.Text()

	_ = scanner.Scan()
	word1 = scanner.Text()

	_ = scanner.Scan()
	word2 = scanner.Text()

	_ = scanner.Scan()
	word3 = scanner.Text()

	fmt.Print(word1, separator, word2, separator, word3)
}