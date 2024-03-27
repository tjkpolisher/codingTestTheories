def solution(genres, plays):
    genre_play_count = {}  # 각 장르별 총 재생 횟수
    song_list_by_genre = {}  # 각 장르별 노래 리스트

    # 장르별 총 재생 횟수와 노래 리스트를 구성
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_play_count:
            genre_play_count[genre] = play
            song_list_by_genre[genre] = [[i, play]]
        else:
            genre_play_count[genre] += play
            song_list_by_genre[genre].append([i, play])

    # 장르를 총 재생 횟수 기준으로 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for genre, _ in sorted_genres:
        # 각 장르별 노래를 재생 횟수(내림차순), 고유 번호(오름차순) 기준으로 정렬
        sorted_songs = sorted(song_list_by_genre[genre], key=lambda x: (-x[1], x[0]))
        # 최대 2곡까지만 선택
        for song in sorted_songs[:2]:
            answer.append(song[0])
    
    return answer