package eclipse

import "testing"

func TestFullVersion(t *testing.T) {
  var data = EclipseData{4, 3, 2, "abc"}
  var expect = "4.3.2.abc"

  if result := data.FullVersion(); result != expect {
    t.Errorf("data.FullVersion() = %v, want %v", result, expect)
  }
}

/*
func TestMajorMinor(t *testing.T) {
  const expect = "4.2"

  if result := Eclipse_43.MajorMinor(); result != expect {
    t.Errorf("Eclipse_42.MajorMinor() = %v, want %v", result, expect)
  }
}

func TestMajorMinorService(t *testing.T) {
  const expect = "4.2.0"

  if result := Eclipse_42.MajorMinorService(); result != expect {
    t.Errorf("Eclipse_42.MajorMinorService() = %v, want %v", result, expect)
  }
}

func TestMajorMinorNoDot(t *testing.T) {
  const expect = "42"

  if result := Eclipse_42.MajorMinorNoDot(); result != expect {
    t.Errorf("Eclipse_42.MajorMinorNoDot() = %v, want %v", result, expect)
  }
}

func TestMajorMinorServiceNoDot(t *testing.T) {
  const expect = "420"

  if result := Eclipse_42.MajorMinorServiceNoDot(); result != expect {
    t.Errorf("Eclipse_42.MajorMinorServiceNoDot() = %v, want %v", result, expect)
  }
}
*/

