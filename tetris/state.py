class GameState:
    def handle_input(self, game, user_input):
        pass

    def update(self, game):
        pass


class RunningState(GameState):
    def handle_input(self, game, user_input):
        pass

    def update(self, game):
        pass


class GameOverState(GameState):
    def handle_input(self, game, user_input):
        print("Game Over. Press 'q' to quit.")

    def update(self, game):
        pass
