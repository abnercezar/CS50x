# TODO
# Library cs50
import cs50
# Main role


def main():
    # Loop to get the change amount
    while True:

        # Print amount due
        print("Change owed: ", end="")
        change = cs50.get_float("Change owed: ")
        if change >= 0:
            break
# Convert the value to cents and multiply by 100
    cents = round(change * 100)
    coins = 0

    coins += cents // 25
    cents = cents % 25

    coins += cents // 10
    cents = cents % 10
    coins += cents // 5
    cents = cents % 5
    coins += cents

    print(coins)

    
# Call main function
if __name__ == "__main__":
    main()
