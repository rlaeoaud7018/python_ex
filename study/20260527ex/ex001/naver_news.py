import urllib.request      
import datetime
import json

client_id = '2zV6BDooSZuWdmKXR5zO'
client_secret = 'L6WBjryRFU'


# NAVER에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)                          # url 주소로 서버에 요청할 준비 객체 생성
    req.add_header('X-Naver-Client-Id', client_id)             # 네이버에 요청 보낼때 인증을 위한 ID값을 더함
    req.add_header('X-Naver-Client-Secret', client_secret)     # 네이버에 요청 보낼때 인증을 위한 PW값을 더함
    
# 클라이언트는 내가 담당하기에 오류가 발생해도 수정할 수 있지만 서버는 아니기에 오류가 발생할 수 있음
# 그래서 외부 요청할 때는 항상 try ~ except 사용

    try:                                            
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')   
            # print(f'response data: {response.read().decode("utf-8")}')
            # decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것
            return response.read().decode("utf-8")

    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None


# NAVER에서 데이터 검색하는 녀석
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'      # news.json => 뉴스를 주고받을때 json 형태로 진행하라는 것
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'
    
    url = base + node + parameters                             # URL 구성
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)


# 도메인에서 검색을 할때 요청 값을 파라미터라고 함
# https://search.naver.com/search.naver   => 도메인
# where=nexearch&                        |  
# sm=top_hty&                            |
# fbm=0&                                 | => 파라미터
# ie=utf8&                               |
# query=weather&                         |
# ackey=yhm6rao2                         |


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    # pDate = datetime.datetime.strftime(post['pubDate'], '%Y-%m-%d %H:%M:%S')
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')


    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pDate': pDate
    })

def main():
    node = 'news'       # 크롤링 하는 대상
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = []    

# JSON = 데이터 교환 형식
# 프로그램끼리 데이터를 주고받기 쉽게 만든 텍스트 형식
# 중괄호 {} 사용, 딕셔너리 형식으로 키와 밸류를 나눔

    jsonResponse = getNaverSearch(node, srcText, 1, 100)    # node(뉴스), srcText(검색어), 1번째부터, 100개까지 가져와
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')

    while jsonResponse != None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    # 파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}.json', 'w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)

if __name__ == '__main__':
    main()

