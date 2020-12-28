# Git 특강-Basic



## git 설치

1. 구글에 github를 검색 후, 링크에서 버전에 맞게 다운로드한다.
2. 설치 시, 모두 next



## git 사용법

### git 기초 단어

1. CLI : command line Interface

2. GUI : graphic user interface (<->CLI)

3. $: 명령을 받을 준비

4. ~ :홈 폴더

   

### git 초기 설정

1. 사용자 이름, 이메일을 설정한다.

```
사용자 이름 설정
$ git config --global user.name "Ryu"

사용자 이메일 설정 
$ git config --global user.email "bei04048@gmail.com"
```



2. 초기화는 `git init`을 통해 진행한다. 

```
git init
```



### git 기초

#### 1. 초기화

1. 원하는 디렉토리	를 만든다(생략가능)

   ```
   $ mkdir CIL
   ```

2. 작업할 디렉토리에 들어간다.

	  ```
	$ cd CIL
	```
	
3. 디렉토리에서  초기화는 `git init`을 통해 진행한다. 

     ```
     $ git init
     ```

이 과정에서 .git 이라는 하위 디렉토리를 만든다. 

.git 디렉토리에는 저장소에 필요한 뼈대 파일이 들어있다. (아직까지는 아무  파일도 없는 상태)

#### 2. add

1. 디렉토리에 commit하고자 하는 파일을 생성한다.

   ```
   $ touch summary.md 
   ```

   

2.  `git status`를 통해 git 저장소의 현재 상태를 확인해보면, summary.md는 untracked file 임을 알 수 있다.

   ```
   $ git status
   ```

3. 이 파일을 stage에 보내기 위해 `git add`를 이용한다.

   ```
   $ git add summary.md
   ```


4. 추가적인 add의 기능 : 아래의 코드는 unstacked 상태인 모든 파일을 stage에 올린다.

   ```
   $ git add -A
   $ git add .
   ```

   



#### 3. Commit

1. 다시 한번 상태를 확인해보면 new file으로 등록되었음을 알 수 있다.

   ```
   $ git status
   ```

   

2. stage에 있는 파일을 commit하면 저장소에 보관된다.

   ```
   $ git commit -m 'first commit'
   ```

   

3. `git log`를 통해 commit의 기록을 알 수 있다.

   ```
   $ git log
   ```



#### 4. Modified

1. GUI환경에서 summary.md 파일을 수정한 뒤, bash에서 `$git status`하면,

   modified로 변경된 것을 확인할 수 있다. 

   

2. 변경된 파일을 stage로 보내기 위해서, `add`를 사용한다

   ```
   $ git add summary.md
   ```





3. stage로 보내기 위해, add 다음에는 항상 commit을 한다.

   ```
   $ git commit -m "summary.md 수정"
   ```


#### 5. Remote

1. local(현재 나의 pc)와 remote(git-hub등 저장소)를 동기화해야한다. (local에 있는 파일을 remote로 동기화)

	```
	$ git remote add origin <url>  #remote와 local동기화됨, 아직 파일이 		local에만 있는 상태)
	```

2. local의  commit한 파일을 `push`를 통해 remote로 보낸다. 

   ```
   $ git push origin master
   ```
   
   

​    +)  remote에 있는 파일 삭제하는 법

​	```  $ git remote rm <remote_repo_name> ```

​        삭제된 것 확인

​	```  $ git remote -v```

#### 6. 기타

1. 커밋 히스토리 조회

   -log를 n개까지만 보고싶을 때

	```
	$ git log -2   #log를 2개까지 확인
	```

​	   -online옵션은 각 커밋을 하나의  라인으로 보여준다.

​		아래의 코드 실행 결과, 노란색으로 뜨는 것은 커밋 고유번호

​		```$ git log --pretty=online```

   2. -rf는 강력한 제거 수단

      `rm -rf <file name or directory name>` 

      





### Summary

| 명령어                     | 의미                                                |
| -------------------------- | --------------------------------------------------- |
| `$ git init`               | 빈 디렉터리를 git의 저장소(repo)로 초기화한다       |
| `$ mkdir <폴더이름>`       | 현재 위치에 폴더를 생성한다.                        |
| `$ touch <파일명>`         | 현재 위치에 파일을 생성한다.                        |
| `$ ls`                     | 현재 위치한 디렉토리에 존재하는 모든 것을 보여준다. |
| `$ cd ..`                  | 상위 폴더로 이동한다.                               |
| `$ cd ~`                   | 현재 위치가 ~로 바뀐다.                             |
| `$ git add <파일명>`       | 파일을 stage로 올린다.                              |
| `$ git status`             | 현재 상태를 보여준다.                               |
| `$ git commit -m "mesage"` | stage에 있는 것을 commit한다.                       |

| `$ git remote add origin <url>` | remote와  local을 동기화한다           |
| ------------------------------- | -------------------------------------- |
| `$ git push origin master`      | local의  commit한 파일을 push로 보낸다 |









