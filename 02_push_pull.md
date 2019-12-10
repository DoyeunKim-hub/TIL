# Push & Pull(clone) 정리

## 1. Push 

> 새롭게 만든 파일이나 수정한 파일을 github에 올릴 때 사용한다.

- `touch new.md`(파일 이름)으로 파일을 추가한다.
- `ls`로 확인 
  - 새로운 `new.md`가 추가 됨을 확인
- `git status`하면 빨간색으로 ` new.md`가 뜰 것이다.
- `git add new.md` 를 이용하여 `new.md` 파일을 commit 할수 있는 공간으로 추가한다.
- `git status`로 확인하면 빨간색이었던 것이 초록색으로 바뀌었을 것이다.
- 이제 `git commit -m "Add new.md"`로 commit을 한다.
- `git log --oneline`으로 log를 보기 쉽게 확인한다. 
  -  `git log`로 확인하면 길게 나온다.
  - `git log -1`은 가장 최근 파일(마지막)을 보여준다
- `ls`으로도 확인 가능하다.
- 최종적으로 `git push origin master`으로 github에 올린다.



## 2. Pull(clone)

### 1) clone

> 새로운 저장공간에 처음으로 github의 자료를 복제할 때 사용한다.

- `mkdir house`는 house라는 폴더를 새로 만든다.
- `git clone  https://github.com/DoyeunKim-hub/TIL.git`(파일위치의 주소) github의 자료(TIL이라는 폴더에 포함된 자료)를 이 폴더(house)에 복제한다.



### 2) pull

> github의 자료를 내려받을 때(당겨올 때) 사용한다.

- 당겨 받을 폴더에 위치한다. 
  - 확인은 `pwd`로 가능
- 현재 깔끔한 상태(오류가 안나는지)인지 확인한다.
  - `git status`으로 "nothing to commit, working tree clean"을 확인한다.
- 최종적으로 `git pull origin master`으로 자료를 당겨온다.

