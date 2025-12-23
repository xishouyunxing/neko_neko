import os
import time
import msvcrt

def clear_screen():
    # ANSI escape codes for clearing screen and moving cursor to top-left
    # \033[2J clear entire screen, \033[H move cursor to home
    print('\033[2J\033[H', end='', flush=True)

def get_key():
    if msvcrt.kbhit():
        return msvcrt.getch()
    return None

def main():
    # Enable ANSI escape sequences on Windows
    os.system('') 
    
    # Hide cursor
    print('\033[?25l', end='')
    
    # Art assets - Pure ASCII
    cat_art_normal = [
        "  /\\_/\\  ",
        " ( o.o ) ",
        "  > ^ <  "
    ]
    
    cat_art_happy = [
        "  /\\_/\\  ",
        " ( ^w^ ) ",
        "  > ~ <  "
    ]
    
    # ASCII Items
    # Tissue Box:
    #    ___
    #   (   )
    #  [~T~ ]
    #  [____]
    
    # Carrot:
    #   ///
    #   \ \
    #    \ \
    #     V
    
    player = "~~~~~~"
    step_size = 3
    
    # Initial state
    width = 40
    player_x = width // 2
    
    # Happy state tracking
    happy_end_time = 0
    
    #print("Use Left/Right arrow keys to move. 'q' to quit.")
    time.sleep(2)
    
    print('\033[2J', end='')

    try:
        while True:
            output_buffer = "\033[H"

            output_buffer += "\n" 
            
            current_art = cat_art_happy if time.time() < happy_end_time else cat_art_normal
            
            
            for line in current_art:
                output_buffer += line.center(width) + "\n"
            output_buffer += "\n"
            
        
            line1 = "    ___          ///   "
            line2 = "   (   )         \\ \\   "
            line3 = "  [~T~ ]          \\ \\  "
            line4 = "  [____]           V   "
            
            label_line = "   纸巾          萝卜  "
            
            output_buffer += line1.center(width) + "\n"
            output_buffer += line2.center(width) + "\n"
            output_buffer += line3.center(width) + "\n"
            output_buffer += line4.center(width) + "\n"
            output_buffer += label_line.center(width) + "\n"
            
            output_buffer += "\n" * 2
            
            # 用户
            padding = " " * player_x
            line_content = padding + player
            output_buffer += line_content.ljust(width) + "\n"
            output_buffer += "\n按q结束训练" 
            
            # 清屏
            output_buffer += "\033[J"
            
            # 打印内容
            print(output_buffer, end='', flush=True)
            
            # 输入
            key = get_key()
            if key:
                if key == b'q':
                    break
                elif key == b' ': 
                    happy_end_time = time.time() + 1.0
                elif key == b'\xe0': 
                    special = msvcrt.getch()
                    if special == b'K': 
                        player_x = max(0, player_x - step_size)
                    elif special == b'M': 
                        player_x = min(width - len(player), player_x + step_size)
            
            time.sleep(0.016) #  60 FPS
            
    except KeyboardInterrupt:
        pass
    finally:
        
        print('\033[?25h')
    
    print("\n哈基米驯化完成")

if __name__ == "__main__":
    main()
