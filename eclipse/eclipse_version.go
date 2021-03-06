package eclipse

import "fmt"

type EclipseVersion interface {
  MajorMinor() string
  MajorMinorService() string
  FullVersion() string
  MajorMinorNoDot() string
  MajorMinorServiceNoDot() string
}

type EclipseData struct {
  major     int
  minor     int
  service   int
  qualifier string
}

func (data EclipseData) MajorMinor() string {
  return fmt.Sprintf("%d.%d", data.major, data.minor)
}

func (data EclipseData) MajorMinorService() string {
  return fmt.Sprintf("%d.%d.%d", data.major, data.minor, data.service)
}

func (data EclipseData) FullVersion() string {
  return fmt.Sprintf("%d.%d.%d.%s", data.major, data.minor, data.service, data.qualifier)
}

func (data EclipseData) MajorMinorNoDot() string {
  return fmt.Sprintf("%d%d", data.major, data.minor)
}

func (data EclipseData) MajorMinorServiceNoDot() string {
  return fmt.Sprintf("%d%d%d", data.major, data.minor, data.service)
}

var Eclipse_43 = EclipseData{major: 4, minor: 3}
var Eclipse_42 = EclipseData{major: 4, minor: 2}
var Eclipse_37 = EclipseData{major: 3, minor: 7}
var Eclipse_36 = EclipseData{major: 3, minor: 6}
