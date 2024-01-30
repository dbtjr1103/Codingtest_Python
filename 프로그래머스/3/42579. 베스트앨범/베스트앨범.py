def solution(genres, plays):
    genre_total_play = {}
    song_list_by_genre = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_total_play:
            genre_total_play[genre] = play
            song_list_by_genre[genre] = [(play, i)]
        else:
            genre_total_play[genre] += play
            song_list_by_genre[genre].append((play, i))

    # 장르별 총 재생 횟수에 따라 정렬
    sorted_genres = sorted(genre_total_play, key=genre_total_play.get, reverse=True)

    result = []
    for genre in sorted_genres:
        # 각 장르 내에서 노래를 재생 횟수와 고유 번호에 따라 정렬
        sorted_songs = sorted(song_list_by_genre[genre], key=lambda x: (-x[0], x[1]))
        # 장르별로 최대 두 곡 선택
        result.extend([song[1] for song in sorted_songs[:2]])

    return result
