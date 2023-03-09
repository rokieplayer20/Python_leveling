from open_source import GifConverter as gfc


# 객체 생성
c = GifConverter('./project/images/*.png',
                 './project/image_out/result.gif', (320, 240))

# 실행
c.convert_gif()

"""
package 배포 순서 (PyPI)

1. https://pypi.org 회원 가입
2. 프로젝트 구조 확인
3. __init__.py 작성
4. 프로젝트 Root file 작성
    - README.md
    - setup.py
    - gitignore
    - setup.cfg(optional)
    - LICENSE
    - MANIFEST.in

5. pip install setuptools wheel 설치 후 빌드 업 -> 설치판 생성
    설치1 : python -m pip install --upgrade setuptools wheel
    설치2 : python -m pip install --user --upgrade setuptools wheel
    빌드 : python setpu.py sdist bdist_wheel

6. PyPI 배포
    설치: pip install twine
    업로드: python -m twine upload dist/*

    만일 version-up이 이루어지면 빌드부터 정보를 갱신하고 다시 하면 된다.

7. 설치 확인: pip install 패키지이름

"""


"""
Github

1. github 가입
2. git 설치 확인 -> gitignore 파일 고려해야 해서
3. git add -> commit -> push
    - git repository 생성
    - git init
    - git add.
    - git status
    - git commit -m 'message'
    - git remote add origin 'your repository'
    - git push origin master

4. PyPI 형태의 패키지 구조를 github repository에 Push
5. 설치 확인: pip install git+URL


"""
