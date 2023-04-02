class GameState:
    def handle_input(self, game, user_input):
        pass

    def update(self, game):
        pass


class RunningState(GameState):
    def handle_input(self, game, user_input):
        dx, dy, rotation = 0, 0, 0

        if user_input == 'a':
            dx = -1
        elif user_input == 'd':
            dx = 1
        elif user_input == 'w':
            rotation = -1
        elif user_input == 's':
            rotation = 1
        elif user_input == ' ':
            pass
        else:
            print("Invalid input. Try again.")
            return

        #   check if input is valid
        valid_movement = game.move_piece(dx, dy, rotation)

        if not valid_movement:
            print("Invalid move. Try again.")
        else:
            if not game.move_piece(0, 1, 0):
                game.update_board()

    def update(self, game):
        if game.game_over():
            game.set_state(GameOverState())


class GameOverState(GameState):
    def handle_input(self, game, user_input):
        print("Game Over. Press 'q' to quit.")

    def update(self, game):
        pass
