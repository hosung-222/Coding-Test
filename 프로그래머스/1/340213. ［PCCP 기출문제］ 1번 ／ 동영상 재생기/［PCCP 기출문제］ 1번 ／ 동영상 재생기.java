class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int totalSeconds = timeToSeconds(video_len);
        int currentSeconds = timeToSeconds(pos);
        int opStartSeconds = timeToSeconds(op_start);
        int opEndSeconds = timeToSeconds(op_end);
        
        if (isInOpening(currentSeconds, opStartSeconds, opEndSeconds)) {
            currentSeconds = opEndSeconds;
        }
        
        for (String command : commands) {
            if (command.equals("prev")) {
                // 10초 전으로 (0초 미만이면 0초로)
                currentSeconds = Math.max(0, currentSeconds - 10);
            } else if (command.equals("next")) {
                // 10초 후로 (총 길이보다 크면 끝으로)
                currentSeconds = Math.min(totalSeconds, currentSeconds + 10);
            }
            
            // 명령 수행 후 위치가 오프닝 구간인지 확인
            if (isInOpening(currentSeconds, opStartSeconds, opEndSeconds)) {
                currentSeconds = opEndSeconds;
            }
        }
        
        return secondsToTime(currentSeconds);
    }
    
    // mm:ss -> seconds
    private int timeToSeconds(String time) {
        String[] parts = time.split(":");
        return Integer.parseInt(parts[0]) * 60 + Integer.parseInt(parts[1]);
    }
    
    // seconds -> mm:ss
    private String secondsToTime(int seconds) {
        return String.format("%02d:%02d", seconds / 60, seconds % 60);
    }
    
    // 현재 위치가 오프닝 구간인지 확인
    private boolean isInOpening(int current, int start, int end) {
        return current >= start && current <= end;
    }
}