#! /usr/bin/env python3
# Author: Mahendran Moorthy
#Version: 1.0
# Description: This is lotto excerise.

import random
lotto = []

while len(lotto) < 6:
    num = random.randint( 1,50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Dumplicate number:", num)

print("Lottery numbers =", lotto)
