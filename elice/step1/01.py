def main():
    blue = list( map( int, input().split(' ') ) )
    white = list( map( int, input().split(' ') ) )
    #input.split(' ') input 값을 공백을 기준으로 나눠서 리스트로 반환
    #map(함수, 반복가능한 객체) : 객체의 요소를 해당 함수로 처리함
    #int() : 타입을 Integer로 반환  
    #list() : 현재 map 오브젝트인 값을 배열로 변환시킴
    
    print(max(sum(blue),sum(white)))
    #max(a,b) : a와 b 중 더 큰 값을 반환
    #sum(list) : list의 합 반환
if __name__ == "__main__":
    main()
