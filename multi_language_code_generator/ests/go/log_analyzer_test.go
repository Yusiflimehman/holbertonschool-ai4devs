package main

import (
	"encoding/json"
	"os"
	"os/exec"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
)

// The Go implementation is a "package main" program, so these tests build it
// once and run it as a command, then compare its JSON output with the shared
// expected results used by the Python and JavaScript tests.

type repeatSpec struct {
	Line  string `json:"line"`
	Count int    `json:"count"`
}

type testCase struct {
	Name     string                 `json:"name"`
	Lines    []string               `json:"lines"`
	Repeat   *repeatSpec            `json:"repeat"`
	Expected map[string]interface{} `json:"expected"`
}

var binaryPath string

func TestMain(m *testing.M) {
	dir, err := os.MkdirTemp("", "log_analyzer_test")
	if err != nil {
		panic(err)
	}
	binaryPath = filepath.Join(dir, "log_analyzer")
	build := exec.Command("go", "build", "-o", binaryPath,
		filepath.Join("..", "..", "implementations", "go", "log_analyzer.go"))
	if out, err := build.CombinedOutput(); err != nil {
		panic(string(out))
	}
	code := m.Run()
	os.RemoveAll(dir)
	os.Exit(code)
}

func buildLines(c testCase) []string {
	lines := append([]string{}, c.Lines...)
	if c.Repeat != nil {
		for i := 0; i < c.Repeat.Count; i++ {
			lines = append(lines, c.Repeat.Line)
		}
	}
	return lines
}

func runAnalyzer(t *testing.T, lines []string) map[string]interface{} {
	t.Helper()
	file := filepath.Join(t.TempDir(), "access.log")
	if err := os.WriteFile(file, []byte(strings.Join(lines, "\n")), 0o644); err != nil {
		t.Fatal(err)
	}
	out, err := exec.Command(binaryPath, file).Output()
	if err != nil {
		t.Fatalf("analyzer failed: %v", err)
	}
	var result map[string]interface{}
	if err := json.Unmarshal(out, &result); err != nil {
		t.Fatalf("invalid JSON output: %v\n%s", err, out)
	}
	return result
}

func TestSharedCases(t *testing.T) {
	data, err := os.ReadFile(filepath.Join("..", "test_cases.json"))
	if err != nil {
		t.Fatal(err)
	}
	var cases []testCase
	if err := json.Unmarshal(data, &cases); err != nil {
		t.Fatal(err)
	}
	for _, c := range cases {
		c := c
		t.Run(c.Name, func(t *testing.T) {
			got := runAnalyzer(t, buildLines(c))
			if !reflect.DeepEqual(got, c.Expected) {
				t.Errorf("got %v, want %v", got, c.Expected)
			}
		})
	}
}

func TestMissingFileFails(t *testing.T) {
	if err := exec.Command(binaryPath, "does_not_exist.log").Run(); err == nil {
		t.Error("expected a non-zero exit code for a missing file")
	}
}
