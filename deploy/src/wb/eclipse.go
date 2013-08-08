package eclipse

import "fmt"

type eclipse interface {
     major_minor() string
     major_minor_service() string
     full_version() string
}

type eclipse_data struct {
     major int
     minor int
     service int
     qualifier string
}

func (data eclipse_data) major_minor() string {
      return fmt.Sprintf("%d.%d", data.major, data.minor)
}

func (data eclipse_data) major_minor_service() string {
      return fmt.Sprintf("%d.%d.%d", data.major, data.minor, data.service)
}

func main() {
  fmt.Printf("Hello, world.\n")
}
