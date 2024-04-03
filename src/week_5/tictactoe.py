import random

# 보드판 출력
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# 승자 체크 함수
def check_winner(board, player):
    # 행 일치
    for row in board:
        if row.count(player) == 3:
            return True
    # 열 일치
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # 대각선 일치
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# 보드가 꽉 찼는지 확인 => 게임 종료 여부 판단
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
        
    return True

# 빈 공간의 위치를 배열로 반환
def get_empty_positions(board):
    empty_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_positions.append((i, j))

    return empty_positions

# 플레이어 턴
def player_move(board):
    while True:
        try:
            row = int(input("행 입력 (0, 1, 또는 2): "))
            col = int(input("열 입력 (0, 1, 또는 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("해당 위치는 이미 마커가 표시돼있습니다. 다른 위치에 시도하세요!")
        except (ValueError, IndexError):
            print("유효하지 않은 입력값입니다. 다시 시도해주세요!")

# 컴퓨터 턴
def computer_move(board):
    # 빈 공간 위치를 담은 배열 중 랜덤한 위치의 (행, 열)의 위치에 마커 표시
    empty_positions = get_empty_positions(board)
    if empty_positions:
        row, col = random.choice(empty_positions)
        board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("축하합니다~ 당신이 승리했어요!")
            break
        if is_board_full(board):
            print("무승부!")
            break

        print("컴퓨터 차례:")
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("컴퓨터 승리! 다음에는 꼭 이기길 바래요.")
            break
        if is_board_full(board):
            print("무승부!")
            break

if __name__ == "__main__":
    main()
