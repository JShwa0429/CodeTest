def main():
    second_len = int(input())
    second = list(map(int,input().split()))
    first = []
    for i in range(second_len):
            first.append(second[i] * (i+1) - second[i-1] * i);
    #오늘치 생산량을 구해서 first에 넣어준다
    #오늘의 생산량 = 총 생산량 - 전일까지의 생산량
    #총 생산량 = 평균 생산량 * 생산일
    
    #i+1의 이유는 i가 0부터 시작하기 때문이다

    print(" ".join(map(str,first)))
    #map(str,first) :  first의 요소들을 문자열로 반환
    #" ".join(반복가능한 객체) : 객체의 요소(문자열)을 " "으로 나눈 뒤 합침

if __name__ == "__main__":
    main()
