package eclipse

import "testing"

func TestMajorMinor(t *testing.T) {
     const expect = "4.2"

     if result := Eclipse_42.MajorMinor(); result != expect {
     	t.Errorf("Eclipse_42.MajorMinor() = %v, want %v", result, expect)
     }
}

func TestMajorMinorService(t *testing.T) {
     const expect = "4.2.0"

     if result := Eclipse_42.MajorMinorService(); result != expect {
     	t.Errorf("Eclipse_42.MajorMinorService() = %v, want %v", result, expect)
     }
}

func TestFullVersion(t *testing.T) {
     var data = EclipseData{4, 3, 2, "abc"}
     var expect = "4.3.2.abc"

     if result := data.FullVersion(); result != expect {
     	t.Errorf("data.FullVersion() = %v, want %v", result, expect)
     }
}