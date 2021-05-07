## GENERAL INFO ##
# map(function, iterator)
# python's map function returns an iterator of the results after applying the function to each item of the iterable

# ord(character)
# python's ord function takes a string of a Unicode character and returns its integer Unicode value

# chr(integer)
# python's chr function takes an integer from 0-1,114,111 and converts it to a Unicode character


## HELPER FUNCTIONS ##
def xor_lists(l1, l2):
  ret_list = []
  for i in range(len(l1)):
    ret_list.append(l1[i]^l2[i])
  return ret_list

def remove_last(l, idx):
  for i in range(len(l)):
    l[i][idx] = '-'

def guess(all_list, curr_list, idx_txt, idx_char, char_num):
  for i in range(len(all_list)):
    if i == idx_txt:
      curr_list[i][idx_char] = chr(char_num)
    else:
      curr_list[i][idx_char] = chr(char_num ^ all_list[idx_txt][idx_char] ^ all_list[i][idx_char])  # P1 ^ C1 ^ C2 = P2
 

## MAIN CODE ##
all_texts = []
size = 0
type_input = 0

# get number of ciphertexts
while True:
  try:
    size = int(input("How many messages are we using today? (2-10): "))
    if (size >= 2 and size <= 10):
      break
    print("That's not a nice number!")
  except:
    print("That's not a number!")

# check type of input
while True:
  try:
    type_input = int(input("Are the ciphertexts in 0) ASCII, 1) Hex, 2) Binary, or 3) Decimal? "))
    if (type_input >= 0 and type_input <= 3):
      break
    print("That's not a valid number!")
  except:
    print("That's not a number!")
print(f"Input the {size} messages")

# get the ciphertexts
max_len = 0
for i in range(size):
  msg = input()
  # if odd, pad a 0 at the front
  if (len(msg) % 2 == 1):
    msg = "0" + msg
  # DECIMAL
  if (type_input == 3):
    try:
      msg = int(msg)
      msg_arr = []
      while msg > 0:
        msg_arr.append(msg % 2**8)
        msg //= 2**8 
      max_len = max(max_len, len(msg_arr))
      all_texts.append(list(reversed(msg_arr)))
    except:
      print("Either you lied, or something went wrong :)")
  # BINARY
  elif (type_input == 2):
    try:
      all_texts.append([int(msg[i:i+8], 2) for i in range(0,len(msg), 8)])
      max_len = max(max_len, len(msg)//8)
    except:
      print("Either you lied, or something went wrong :)")
  # HEX
  elif (type_input == 1):
    # https://stackoverflow.com/questions/41848722/how-to-convert-hex-str-into-int-array
    try:
      all_texts.append([int(msg[i:i+2],16) for i in range(0,len(msg),2)])
      max_len = max(max_len, len(msg)//2)
    except:
      print("Either you lied, or something went wrong :)")
  # ASCII
  else:
    max_len = max(max_len, len(msg))
    all_texts.append(list(map(ord, msg))) # a list of list of numbers

# testing
print(all_texts)

print("Time to try and guess the messages!")
curr_index = 0
curr_letter = ''
curr_guess = []
blank = "-"*max_len

# initialize blank guesses
for _ in range(size):
  curr_guess.append(list(blank))

# keep guessing till finish
while True:
  print("\n===============\n\ncurrent progress:")
  for i in range(size):
    print(f"{str(i)}) {''.join(curr_guess[i])}")

  # celebrate!!
  if (curr_index == max_len):
    print("Congrats! You might've just done it!")
    exit_or_redo = input("Are you done? (y or n)")
    if exit_or_redo == "y":
      break
    
  idx_guess = input("Which message do you want to try and guess? (enter 'q' to quit, or 'd' to delete most recent character ")

  if (idx_guess == 'q'):
    break
  elif (idx_guess == 'd'):
    curr_index = max(curr_index - 1, 0)
    remove_last(curr_guess, curr_index)
    continue
  else:
    try:
      idx_guess = int(idx_guess)
      if (idx_guess >= size or idx_guess < 0):
        print("Invalid index!")
        continue
    except:
      print("That's not a valid input!")
      continue

  curr_letter = input("Input your guess for the next letter (enter 'q' to quit): ")
  if not curr_letter: # empty
    print("You inputted nothing!")
    continue
  elif (curr_letter == 'q'):
    break
  elif (len(curr_letter) > 1)
    print("You inputted more than 1 letter!")
    continue
  
  try:
    num_val = ord(curr_letter)
    guess(all_texts, curr_guess, idx_guess, curr_index, num_val)
    curr_index += 1
  except:
    print("Something went wrong with guessing the letter!")
