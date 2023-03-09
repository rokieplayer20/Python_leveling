# requests는 서버에서 정보를 가져오는 패키지이다.
# !pip install requests
import requests
import time

# 실행함수1 다운로드


def request_site(url, session):
    # session 확인
    print(session)
    print(session.headers)
    """
    SSLError: HTTPSConnectionPool
    신뢰할 수 있는 SSL 인증서로 인해서 발생한다.
    get에 verify를 false로 바꾼다.
    
    또는 

    openssl의 버전이 맞지 않기 때문일 수 있다.
    """
    with session.get(url, verify=False) as response:
        print(
            f'[Read contents: {len(response.content)}, Status Code: {response.status_code}] from {url}')


# 실행함수2 요청
def request_all_sites(urls):
    # 서버에 접속한 시점에서 웹브라우저에서 정보를 가져옴
    with requests.Session() as session:
        for url in urls:

            request_site(url, session)


# sync blocking IO
def main():
    # test URLs
    urls = [
        'https://www.jython.org',
        'https://olympus.realpython.org',
        'https://realpython.com',
    ] * 3

    # 실행시간 측정
    start_time = time.time()

    # 실행
    request_all_sites(urls)

    # 실행 시간 종료
    duration = time.time() - start_time

    # 결과 출력
    print()
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


if __name__ == '__main__':
    main()
