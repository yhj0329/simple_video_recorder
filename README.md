# simple_video_recorder
OpenCV를 이용한 간단한 동영상 녹화 프로그램이다.  
[![simple video recorder preview](http://img.youtube.com/vi/6Fll-Eeg1us/0.jpg)](https://youtu.be/6Fll-Eeg1us)

## 기능 소개
- 녹화 기능이 있다.
- 색상 반전 기능이 있다.
- 녹화된 파일은 mp4 형식이다.

## 조작키
- SPACE BAR : 녹화(Record) 기능 활성화 / 비활성화
- TAB : 색상 반전 기능 활성화  / 비활성화
- ESC : 프로그램 종료

---

---

## 동영상 확장자와 코덱(OpenCV)

~~~ python
cv.VideoWriter_fourcc(*'코덱의 종류') 
cv.VideoWriter('sample.확장자', fourCC, fps, (width, height))
~~~
코덱의 종류와 확장자가 맞지 않는다면 다음과 같은 오류가 발생한다.  
>OpenCV: FFMPEG: tag 0x44495658/'XVID' is not supported with codec id 12 and format 'mp4 / MP4 (MPEG-4 Part 14)'

그래서 알맞은 확장자와 코덱을 넣어줘야 한다.

|  동영상 확장자   |        코덱        |
|:----------:|:----------------:|
|    AVI     | XVID, DIVX, mp4v |
| MPEG4(MP4) |       mp4v       |
|    MOV     | XVID, DIVX, mp4v |
|    WMV     |    XVID, DIVX    |
|    ASF     | XVID, DIVX, mp4v |
확장자와 코덱의 종류는 더 많지만 이정도가 자주 사용될 것 같다.