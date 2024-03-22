// Date 23.03.2024
// Url: https://stepik.org/lesson/917013/step/4?unit=922792

package main
import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	var text string
	
	scanner := bufio.NewScanner(os.Stdin)
	_ = scanner.Scan()

	text = scanner.Text()
	fmt.Print(text, " - лучшая книга!")
}