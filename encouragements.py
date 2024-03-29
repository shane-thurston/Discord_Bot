#code to view the starter encouragements
if msg.startswith('$view'):
    await message.channel.send(starter_encouragements)

#code to create helper function add encouragements to our existing list
def update_encouragements(enc_msg):
  if enc_msg not in starter_encouragements:
    starter_encouragements.append(enc_msg)
    return True
  else:
    return False

#code to send encouragements to the helper function
if msg.startswith('$new'):
    encouraging_message = msg.split('$new ',1)[1]
    if update_encouragements(encouraging_message):
      await message.channel.send("New encouraging message added.")
    else:
      await message.channel.send("Sorry couldn't add that.")

#code to create helper function remove encouragements to our existing list
def remove_encouragements(enc_msg):
  if enc_msg in starter_encouragements:
    starter_encouragements.remove(enc_msg)
    return True
  else:
    return False

#code to send remove encouragements to the helper function
if msg.startswith('$delete'):
    remove_message = msg.split('$delete ',1)[1]
    if remove_encouragements(remove_message):
      await message.channel.send("Message deleted.")
    else:
      await message.channel.send("Sorry couldn't delete that.")

#Textblob code for checking sentiment analysis
from textblob import TextBlob

#check the msg entered by the user.
blob = TextBlob(msg)
pol = blob.polarity
#polarity lies between -1 and 1 where 1 means positive and -1 means negative
if pol < 0:
  await message.channel.send('That was a negative comment! Are you ok?')
else:
  await message.channel.send('That was a positive thing to say. You must be feeling good.')
