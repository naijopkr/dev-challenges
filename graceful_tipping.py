from math import ceil

def graceful_tipping(total_bill):
    include_tip = ceil(1.15*total_bill)

    if include_tip <= 10:
        return include_tip

    tip_magnitude = 1
    while include_tip / 10 ** tip_magnitude > 10:
        tip_magnitude += 1

    tip_coeficient = 5 * 10 ** (tip_magnitude - 1)

    return include_tip + tip_coeficient - include_tip % tip_coeficient

if __name__ == '__main__':
    while True:
        try:
            bill = float(input('Insert the total bill: '))
        except ValueError:
            print('Invalid value. Try again.')
        else:
            with_tip = graceful_tipping(bill)
            print(f'Bill + Tip = {with_tip}')
            break
