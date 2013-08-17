package eclipse

import "fmt"

type eclipseVersion interface {
  MajorMinor() string
  MajorMinor_service() string
  FullVersion() string
}

type eclipseData struct {
  major     int
  minor     int
  service   int
  qualifier string
}

func (data eclipseData) MajorMinor() string {
  return fmt.Sprintf("%d.%d", data.major, data.minor)
}

func (data eclipseData) MajorMinorService() string {
  return fmt.Sprintf("%d.%d.%d", data.major, data.minor, data.service)
}

func (data eclipseData) FullVersion() string {
  return fmt.Sprintf("%d.%d.%d.%s", data.major, data.minor, data.service, data.qualifier)
}

func (data eclipseData) MajorMinorNoDot() string {
  return fmt.Sprintf("%d%d", data.major, data.minor)
}

func (data eclipseData) MajorMinorServiceNoDot() string {
  return fmt.Sprintf("%d%d%d", data.major, data.minor, data.service)
}

var Eclipse_43 = eclipseData{major: 4, minor: 3}
var Eclipse_42 = eclipseData{major: 4, minor: 2}
var Eclipse_37 = eclipseData{major: 3, minor: 7}
var Eclipse_36 = eclipseData{major: 3, minor: 6}
