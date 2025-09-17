def is_win(game):
    """检查游戏是否有获胜者"""
    # 定义所有可能的获胜模式
    win_patterns = [
        # 行
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # 列
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # 对角线
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    
    # 检查每种获胜模式
    for pattern in win_patterns:
        (i1, j1), (i2, j2), (i3, j3) = pattern
        cell_value = game[i1][j1]
        # 确保单元格已被X或O占据且三个单元格值相同
        if cell_value in ('X', 'O') and cell_value == game[i2][j2] == game[i3][j3]:
            return True, cell_value  # 返回获胜状态和获胜者
    
    return False, None  # 没有获胜者

def print_board(game):
    """打印当前游戏棋盘"""
    print("\n当前棋盘:")
    for row in game:
        print(" | ".join(row))
        print("-" * 9)
    print()

def get_valid_move(game):
    """获取并验证玩家的移动"""
    while True:
        try:
            i, j = map(int, input("请输入要标记的单元格 (i:[1..3], j:[1..3]): ").split())
            # 转换为0-based索引
            i -= 1
            j -= 1
            
            # 检查坐标是否在有效范围内
            if not (0 <= i < 3 and 0 <= j < 3):
                print("错误: 坐标必须在1-3之间，请重新输入。")
                continue
            
            # 检查单元格是否已被占用
            if game[i][j] != ' ':
                print("错误: 该单元格已被占用，请选择其他单元格。")
                continue
            
            return i, j  # 返回有效的坐标
        
        except ValueError:
            print("错误: 请输入两个整数，用空格分隔。")

def main():
    # 游戏常量定义
    PLAYER1 = 'X'
    PLAYER2 = 'O'
    EMPTY = ' '
    
    # 初始化游戏棋盘
    game = [[EMPTY for _ in range(3)] for _ in range(3)]
    
    print("井字棋游戏")
    print(f"{PLAYER1} = 玩家1")
    print(f"{PLAYER2} = 玩家2")
    print("玩家1先行\n")
    
    # 显示初始棋盘
    print_board(game)
    
    # 游戏主循环
    for turn in range(9):  # 最多9步
        # 确定当前玩家
        current_player = PLAYER1 if turn % 2 == 0 else PLAYER2
        print(f"玩家{1 if current_player == PLAYER1 else 2}的回合 ({current_player})")
        
        # 获取有效移动
        i, j = get_valid_move(game)
        
        # 记录移动
        game[i][j] = current_player
        
        # 显示更新后的棋盘
        print_board(game)
        
        # 检查是否有获胜者
        has_winner, winner = is_win(game)
        if has_winner:
            print(f"恭喜玩家{1 if winner == PLAYER1 else 2} ({winner})获胜！")
            return
    
    # 如果所有格子都填满了仍无获胜者，则为平局
    print("游戏结束，平局！")

if __name__ == "__main__":
    main()
