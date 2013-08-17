package main

import "fmt"
import "flag"
import "os"

const default_tool = ""
const default_env = "integration"

var list_tool = []string{"wbpro", "gwtd"}
var list_env = []string{"stage", default_env, "release"}
var set_tool = make(map[string]bool)
var set_env = make(map[string]bool)

type productS struct {
	tool string
	env string
	base string
	location string
	versions []EclipseVersion
}

func init() {
  for _, v := range list_tool {
    set_tool[v] = true
  }

  for _, v := range list_env {
    set_env[v] = true
  }
}

func main() {
	product := processArgs()
  fmt.Printf("Preparing %s from environment %s\n\tfrom base directory %s\n", 
		product.tool, product.env, product.base)

}

func processArgs() productS {
  toolPtr := flag.String("tool", default_tool, "the tool to stage. (wbpro|gwtd)")
  envPtr := flag.String("env", default_env, 
		"the stage to use. (staging|integration|release)")
	baseDirPtr := flag.String("base", "/usr/local/google/kalamath/builds",
		"base directory for builds")

  flag.Parse()
	var product productS
	
  product.tool = *toolPtr
  product.env = *envPtr
	product.base = *baseDirPtr

  if product.tool == default_tool {
		fmt.Printf("No tool defined.\nUsage:\n")
		flag.PrintDefaults()
		os.Exit(1)
	} else if !set_tool[product.tool] {
    fmt.Printf("Invalid tool defined: %s.\nUsage:\n", product.tool)
    flag.PrintDefaults()
    os.Exit(2)
  } else if !set_env[product.env] {
    fmt.Printf("Invalid environment defined: %s.\nUsage:\n", product.env)
    flag.PrintDefaults()
    os.Exit(3)
  } else if _, err := os.Stat(product.base); os.IsNotExist(err) {
    fmt.Printf("Base directory does not exist: %s", product.base)
    os.Exit(4)
	} else if len(flag.Args()) > 0 {
		fmt.Printf("Unknown arguments: %v\n", flag.Args())
		os.Exit(5)
	}
	return product
}