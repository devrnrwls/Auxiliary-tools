# DarkLabel

### Download Latest Executable
* [DarkLabel2.4](https://github.com/darkpgmr/DarkLabel/releases/download/darklabel-release/DarkLabel2.4.zip)
(currently, only binary executables can be downloaded)
### 프로그램 클래스 설정
1. darknet yolo
2. darklabel.yml 파일에서 coco_classes에서 원하는 클래스 추가
3. 라디오 박스 중 "Box"선택

### Basic Instruction

	Arrow/PgUp/PgDn/Home/End: 이미지 frame 이동
	
	Mouse: 왼쪽(box 생성), 오른쪽(가장 최근에 만든 box 취소)
	Shift+Mouse: 왼쪽(box 수정), Right(선택 박스 삭제 or 모든 박스 삭제)
	Shift+DoubleClick: box properties 수정(label, ID, difficulty)
	
	DoubleClick: select/deselect box 유사한 객체 추적
	*box trajectory: boxes connected across frames with the same ID and label
	
	Ctrl+'+'/'-': 줌 in/out
	Ctrl+Arrow: 줌된 화면 이동
	Ctrl+MouseWheel: 줌 in/out
	Ctrl+MouseDrag: 줌된 화면 이동
	
	Enter or Spacebar: 추적 적용하며 다음 화면
	Ctrl+'s': GT 저장
	F1: show help

 ** 작업 이미지를 학습 이미지 그대로 사용하려면 "NO BOX DRAWING"으로 해야 박스가 없음. [참고 설명 사이트](https://coddingjiwon.tistory.com/13)
 - (기본) box drawing :  바운딩 박스가 쳐져있는 사진을 저장하는 형식
 - (선택) no box drawing : 바운딩 박스 없이 사진만 저장하는 형식
 - (선택) mosaic the box area : 바운딩 박스 지역을 모자이크 처리하여 저장하는 형식

### Advanced Instruction
* Labeling by object tracking
  * By pressing 'Return' key, _newly created_ bounding boxes in the current frame are tracked in the next frame and labeled automatically.
    * _newly created boxes_: the boxes that are created after entering into the frame.
  * If there are selected trajectories in the frame (object trajectory can be selected by double clicking a box), only the trajectory boxes are tracked (newly created boxes are not tracked).
  * If tracking is applied to trajectories, it first deletes their tail parts (connected trajectory boxes after the current frame) and then continue the tracking, keeping their IDs and labels. This functionality can be used to correct previous wrong tracking.
  * Two trackers are embeded. (developed by darkpgmr)
    * tracker1 (robust): good for deformable objects (e.g., human, ..)
    * tracker2 (accurate): good for rigid/static object (e.g., vehicle, wall, house, ...)
* Data Sampling/gathering
  * If you want to sample images in a video and save them (e.g. gathering training samples), draw dummy boxes on the images and then export the annotation results as images with the "no box drawing" option selected and the "labeled frames only" checked.
* 프라이버시 모드
  * draw boxes on the privacy area (e.g. human faces) and then export the annotation results with the "mosaic the box area" option selected.
* Full 스크린
  * do annotation in full screen mode in case the image is too large to show in your monitor (double click the title bar of image window). You also can utilize zoom in functionality.
* Don't forget to save your annotation results as often as possible. You can just press Ctrl+S.

### Video/Image Labeling and Annotation Tool
This is a utility program that can label object bounding boxes with ID and name in videos and images. It also can be used to crop videos, sample traninig images in a video, and mosaic image region. Anyone can use it for non-commercial purposes.

※ Since this program is not code-signed, download and execution may be blocked by Windows and web browsers. This is a personally created program and a 100% safe program, but only for those who need it.

### Main Features
* Video/image object labeling & annotation tool (bounding box with ID and label)
  * automatic object labeling by visual tracking (multi-target)
  * semi-automatic labeling by linear interpolation
  * user-configurable hotkeys and zoom in / zoom out support
  * user-configurable data formats (pascal voc, darket yolo, xml/txt, any other user-defined formats)
* Video splitting (into images) & image merging (into a video file) tool
* Video cropping tool (cut and save only the selected section in the video)
* Video/image privacy masking tool (mosaic the box area in the image)
* Windows only (32/64 bits)

### Program Configuration
The program can be configured by modifying [darklabel.yml](https://github.com/darkpgmr/DarkLabel/blob/master/darklabel.yml) attached in the zipped archive.
* define and modify data formats
* change hotkeys (frame navigation, action keys)
* change video/image export setting (video codec, frame rate, image format)
* set default save/load directory
* define class labels
* adjust GUI drawing (box width, box color, ...)


