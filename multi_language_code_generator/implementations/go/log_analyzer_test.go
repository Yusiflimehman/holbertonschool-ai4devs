package main

import "testing"

// Expected values come from Python's round(x, 2), the reference implementation.
// Cases like 3.125 are exact ties: Python rounds them to the even digit (3.12).
func TestRound2MatchesPython(t *testing.T) {
	cases := []struct {
		in   float64
		want float64
	}{
		{3.125, 3.12},
		{9.375, 9.38},
		{15.625, 15.62},
		{21.875, 21.88},
		{6.25, 6.25},
		{12.5, 12.5},
		{66.66666666666667, 66.67},
		{0.0, 0.0},
	}
	for _, c := range cases {
		if got := round2(c.in); got != c.want {
			t.Errorf("round2(%v) = %v, want %v", c.in, got, c.want)
		}
	}
}

func TestAnalyzeTieErrorRate(t *testing.T) {
	// 1 error out of 32 requests = 3.125% -> Python gives 3.12.
	lines := []string{`10.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /x HTTP/1.1" 500 10`}
	for i := 0; i < 31; i++ {
		lines = append(lines, `10.0.0.2 - - [10/Oct/2023:13:55:36 +0000] "GET / HTTP/1.1" 200 10`)
	}
	got := NewLogAnalyzer().Analyze(lines)
	if got.TotalRequests != 32 || got.ErrorRate != 3.12 {
		t.Errorf("got total=%d error_rate=%v, want 32 and 3.12", got.TotalRequests, got.ErrorRate)
	}
}

func TestAnalyzeEmptyAndInvalid(t *testing.T) {
	got := NewLogAnalyzer().Analyze([]string{"", "not a log line"})
	if got.TotalRequests != 0 || got.ErrorRate != 0.0 {
		t.Errorf("unexpected result for empty input: %+v", got)
	}
}
