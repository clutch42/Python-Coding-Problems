class PlayNim:
    def __init__(self, list):
        self.list = list
        self.one_stack = False
        self.more_than_one = False
        self.find_stacks_greater_than_one()
        print(f"Numbers: {self.list}")
        print(f"At least one stack greater than one: {self.one_stack}")
        print(f"More than one stack greater than one: {self.more_than_one}")

    def find_stacks_greater_than_one(self):
        for num in self.list:
            if num > 1 and self.one_stack is False:
                self.one_stack = True
            elif num > 1 and self.more_than_one is False:
                self.more_than_one = True
                break

    def nim_sum_list(self):
        result = 0
        for num in self.list:
            result ^= num
            print(result)
        return result

    def current_player_wins(self):
        if not self.one_stack:
            if len(self.list) % 2 == 0:
                return True
            else:
                return False
        if self.one_stack and not self.more_than_one:
            return True
        total_xor = self.nim_sum_list()
        if total_xor > 0:
            return True
        return False
