def checkmate(board_text: str):
    #กระดาน
    board_rows = [row.replace(" ","").upper() for row in board_text.splitlines()] # <<< ใช้ตัวเล็กได้ ใช้ space ไว้เว่้นได้
    board_size = len(board_rows)

    if board_size == 0 or board_size > 8: # <<< Board หย่ายเกิน
        print("Board too big or No board Na bro")
        return

    if any(len(row) != board_size for row in board_rows): # <<< Board ไม่เหลี่ยม
        print("Board no เหลี่ยม ni")
        return
    
    # ตรวจอักษร << กัน เอ๋อ ตัวแปลก
    allowed_pieces = set("KPRBQ.")  #<<< allow หมาก

    cleaned_rows = []
    for row in board_rows:
        new_row = ""
        for piece in row:
            if piece in allowed_pieces:
                new_row += piece
            else:
                new_row += "."   # ตัวแปลก กลายเป็นช่องว่าง
        cleaned_rows.append(new_row)

    board_rows = cleaned_rows

    # หา King
    king_positions = [
        (row_index, col_index)
        for row_index in range(board_size)
        for col_index in range(board_size)
        if board_rows[row_index][col_index] == "K"
    ]

    if len(king_positions) == 0: # <<< K ไม่มี
        print("ไหน King Bro")
        return

    if len(king_positions) > 1: # <<< K เกิน
        print("เห้ยไมมีหลาย King")
        return

    king_row, king_col = king_positions[0]

    #ขอบกระดาน
    def korb_board(row, col):
        return 0 <= row < board_size and 0 <= col < board_size

    # Pawn attack อยู่ล่าง ยิงขึ้น \/
    for col_offset in (-1, 1):
        pawn_row = king_row + 1
        pawn_col = king_col + col_offset

        if korb_board(pawn_row, pawn_col) and board_rows[pawn_row][pawn_col] == "P":
            print("Success")
            return

    # Scan (Rook / Bishop / Queen)
    def scan_directions(directions, target_pieces):
        for row_step, col_step in directions:
            scan_row = king_row + row_step
            scan_col = king_col + col_step

            while korb_board(scan_row, scan_col):
                piece = board_rows[scan_row][scan_col]

                if piece != ".":
                    return piece in target_pieces

                scan_row += row_step
                scan_col += col_step

        return False

    # Rook / Queen (ตรง)
    if scan_directions(
        directions=[(-1,0),(1,0),(0,-1),(0,1)],
        target_pieces="RQ"
    ):
        print("Success")
        return

    # Bishop / Queen (ทแยง)
    if scan_directions(
        directions=[(-1,-1),(-1,1),(1,-1),(1,1)],
        target_pieces="BQ"
    ):
        print("Success")
        return

    print("Fail")
