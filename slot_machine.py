# before starting off the slot machine we rquire two input 
# player input money and its bet money
# lets create a function for that
MAX_LINES=3 # GLOBAL VARIABELS CAN BE USED ANYWHERE IN THE PROGRAM
MAX_AMOUNT=100
MIN_AMOUNT=1


import random
ROW=3
COLS=3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winings(lines, columns, symbol_value,bet):
    winnings=0
    winnings_lines = []
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            check_symbol=column[line]
            if check_symbol!=symbol:
                
                break
        else:
            winnings+=symbol_value[symbol] * bet
            winnings_lines.append(line+1)
    return winnings,winnings_lines
def get_slot_machine_spin(rows, cols, symbols_count):
    all_symbols = []
    for symbol, symbol_count in symbols_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
            amount=input("Eneter your amount.$")
            if amount.isdigit():
                amount=int(amount)
                if amount>0:
                    break 
                else:
                    print("amount must be greater than zero")
            else:
                print("Pleae enter a number")
    return amount   
# function for number of lines to bet on
def get_number_lines():
    while True:
        lines=input("Enter number lines to bet on (1-"+ str(MAX_LINES)+")")
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Inter valid number of lines")
        else:
            print("please enter a number")
    return lines
# function to check total amount
def get_bet():
    while True:
        bet=input("Enter the amount you want to bet:")
        if bet.isdigit():
            bet=int(bet)
            if MIN_AMOUNT<= bet <= MAX_AMOUNT:
                break
            else:
                print(f"bet must be between: {MIN_AMOUNT} {MAX_AMOUNT}")
        else:
            print("Please enter a number")       
    return bet

def play_game(balance):
    lines=get_number_lines()
    while True: 
        bet=get_bet()
        total_bet=bet*lines
        if total_bet > balance:
            print(f"Your balance is not enough to bet, your current balance is {balance}")
        else:
            break
    print( f"your betting {bet} on lines {lines} and your total bet {total_bet}")
    slot=get_slot_machine_spin(ROW,COLS,symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines=check_winings(lines, slot,symbol_value,bet)
    print(f"You won ${winnings}.")
    print(f"You win on lines", *winning_lines)
        
    return winnings-total_bet 
